#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib.request
from requests_oauthlib import OAuth1Session

from . import Utilities

MediaUrl    = "https://upload.twitter.com/1.1/media/upload.json"
TextUrl     = "https://api.twitter.com/1.1/statuses/update.json"
TimeLineUrl = "https://api.twitter.com/1.1/statuses/user_timeline.json"

FolderName = "./images/"

ConvertYearFormat = Utilities.MakeConvertDateFormat('%a %b %d %H:%M:%S %z %Y', '%Y')
ConvertMonthFormat = Utilities.MakeConvertDateFormat('%a %b %d %H:%M:%S %z %Y', '%m')
ConvertDayFormat = Utilities.MakeConvertDateFormat('%a %b %d %H:%M:%S %z %Y', '%d')


def run(Keys,Params,GetCount):
    Num = 0
    Twitter = SetAPI(Keys)
    if Params['max_id'] == '0':
        Params.pop('max_id')
    for i in range(1,GetCount):
        if (i==1):
            Params = Params
        else:
            Params.update({"max_id":Num})
        TimeLine = GetTimeLine(Twitter,Params)
        Num = SaveImages(TimeLine)
    return Params
        
def SetAPI(Keys):
    Twitter = OAuth1Session(Keys['API_KEY'], Keys['API_SECRET'], Keys['ACCESS_TOKEN'], Keys['ACCESS_SECRET'])
    return Twitter

def GetTimeLine(Twitter,Params):
    Req = Twitter.get(TimeLineUrl,params = Params)
    TimeLine = json.loads(Req.text)
    return TimeLine

def SaveImages(TimeLine):
    Num = 0
    for Content in TimeLine:
        if "extended_entities" in Content:
            if not "video_info" in Content:
                Count = 0
                for Image in Content["extended_entities"]["media"]:
                    Count += 1
                    Year = ConvertYearFormat(Content["created_at"])
                    Month = ConvertMonthFormat(Content["created_at"])
                    Day = ConvertDayFormat(Content["created_at"])
                    NewFolderName = FolderName + Year + "/" + Month + "/"
                    Utilities.CreateFolder(NewFolderName)
                    ImageTitle = NewFolderName+Day+Content["id_str"]+str(Count)+".jpg"
                    ImageUrl = Image["media_url"]
                    try:
                        Response = urllib.request.urlopen(ImageUrl)
                        with open(ImageTitle, "wb") as f:
                            f.write(Response.read())
                    except:
                        print("error")
        Num = Content["id"]
    return Num
