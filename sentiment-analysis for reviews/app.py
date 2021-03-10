from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import json
f = open ('reviews.json', "r") 
data = json.loads(f.read()) 
tempList=[]
def findReview(arr, colour,rating,storage):
    for x in arr:
        if x["colour"] == colour and x["rating"] == rating and x["storage"] == storage:
            tempList.append(x)
    return tempList

app = Flask(__name__)

# classifier pickel file 
model = open('sentimentAnalysis.pkl','rb')
classifier = pickle.load(model)

# tfidf vector pickel file
model = open('vector.pkl','rb')
vectorizer= pickle.load(model)

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")

@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        colour = str(request.form["colour"])
        rating = str(request.form["rating"])
        storage = str(request.form["storage"])
        print("colour:",colour)
        print("rating:",rating)
        print("storage:",storage)
        output=findReview(data ,colour,rating,storage)
        print("length :",len(output))
        return render_template('home.html',prediction_text_list=output)
    return render_template("home.html")

@app.route("/predictReview", methods = ["GET", "POST"])
@cross_origin()
def predictReview():
    if request.method == "POST":
        new_review = str(request.form["review"])
        all_text=[]
        all_text.append(new_review)
        tfidf = vectorizer.transform(all_text)
        pred_out = classifier.predict(tfidf) 
        return render_template('home.html',reviews_out="Your Sentimetal Analysis output is {}".format(pred_out[0]),review_text=new_review)
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
