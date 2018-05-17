# !/usr/bin/env python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import json
import datetime
import itchat
from threading import Timer

def send_wechat():
    hk_url = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=香港')
    hk_json = json.loads(hk_url.text)
    city_xianggang = hk_json["data"]["city"]

    week_date = hk_json["data"]["forecast"][0]["date"]
    fengxiang_hk = hk_json["data"]["forecast"][0]["fengxiang"]
    high_hk = hk_json["data"]["forecast"][0]["high"]
    low_hk = hk_json["data"]["forecast"][0]["low"]
    weather_hk = hk_json["data"]["forecast"][0]["type"]
    tixing_hk = hk_json["data"]["ganmao"]
    # a = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=深圳')
    # a = json.loads(a.text)
    # city_sz = a["data"]["city"]
    # fengxiang_sz = a["data"]["forecast"][0]["fengxiang"]
    # high_sz = a["data"]["forecast"][0]["high"]
    # low_sz = a["data"]["forecast"][0]["low"]
    # weather_sz = a["data"]["forecast"][0]["type"]
    # tixing_sz = a["data"]["ganmao"]


    now_date = datetime.datetime.now()
    now_month = now_date.month
    today = datetime.datetime.today()
    anniversary = datetime.datetime(2018, 1, 18)
    loving_days = (today - anniversary).days
    CONTENT_FORMAT = "你好，我的典典 😄 :\n\n\t" "今天是 %s月%s。\n\t""首先，今天已经是我们相恋的第 %s 天了喔 💓。然后我就要来播送天气预报了！！\n\n\t""%s今天%s，%s，天气%s，""需要注意的是%s\n\n\t---来自万能的python\n\n\t你的宝宝" % (now_month, week_date, loving_days,city_xianggang,high_hk, low_hk,weather_hk, tixing_hk)

    user = itchat.search_friends(name='典典')[0]["UserName"]
    itchat.send(CONTENT_FORMAT, toUserName=user)
itchat.auto_login(hotReload=True)
send_wechat()
# 开始后台监测
itchat.run()
