# -*- coding:utf-8 -*-
import json, config,random
from requests_oauthlib import OAuth1Session

CK = なし
CS = なし
AT = なし
ATS = なし
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/update.json"
tweet = random.randint(1,100)
params = {"status" : tweet}

req = twitter.post(url, params = params)

if req.status_code == 200:
    print("Succeed!")
else:
    print("ERROR : %d"% req.status_code)
