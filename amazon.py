# -*- coding:utf-8 -*-
import json, config,random
from requests_oauthlib import OAuth1Session

CK = "bpEgeegoD2rTDGqzS2QuQEHq5"
CS = "nqSIy0DMGvfYd4Eleel8zpkJdtaU4a0PxXdsOFqzRl014UETxU"
AT = "717934172459798529-JWgH6f0FSj2ue0KQAxBCxE3ZpOfVKZX"
ATS = "qNGj63NXX7VkWxrAE3i3V1YykgJbGwc3L9QiBewBrv3Xo"
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/statuses/update.json"
tweet = random.randint(1,100)
params = {"status" : tweet}

req = twitter.post(url, params = params)

if req.status_code == 200:
    print("Succeed!")
else:
    print("ERROR : %d"% req.status_code)