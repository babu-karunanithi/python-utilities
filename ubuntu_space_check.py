#!/usr/bin/python3
import requests
import subprocess
from datetime import datetime
from importsHelper import *
threshold =75
child = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE)
output = child.communicate()[0].strip().split(b"\n")
for x in output[3:4]:
    if int(x.split()[-2][:-1]) >= threshold:
        message=str(x)
        url = your slack url
        payload = "{'text': '"+message+"'}"
        headers = { 'Content-Type': 'text/plain'}
        response = requests.request("POST", url, headers=headers, data = payload)
