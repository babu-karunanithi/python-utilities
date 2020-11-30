import requests
import re
import shutil
import os
import time

user_agent={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
searchs=['Rohit Sharma','Virat Kohli','yuvraj Singh','Sachin Tendulkar','Rahul dravid']
for search in searchs:
    url="https://www.google.com/search?q={}&source=lnms&tbm=isch".format(search)
    response=requests.get(url=url,headers=user_agent).text
    pattern="\[\"https://.*\.jpg\",[0-9]+,[0-9]+\]"
    images=re.findall(pattern,response)
    if images:
        path = r"C:\\Users\\welcome\\playersData\\{}".format(search)
        if not os.path.exists(path):
            os.makedirs(path)
            os.chdir(path)
        else:
            shutil.rmtree(path)
            os.makedirs(path)
            os.chdir(path)
        for image in images:
            try:
                image_url=eval(image)[0]
                response=requests.get(image_url).content
                image_name=image_url.split("/")[-1]
                with open(image_name,"wb+") as f:
                    f.write(response)
            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
                continue  
