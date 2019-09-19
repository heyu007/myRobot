#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
自定义一个简易的对话机器人 v0.1
"""

__author__ = 'heyu <18781085152@163.com>'

import random, datetime, requests

ask1 = ['你好', '您好', '你好！', '你好？', '你好啊', '你好呀', 'hello', 'hi']

answer1 = ['你好啊，亲', '今天，也是美丽的一天哟，你奋斗的样子真美', '奈奈酱，钢巴得']

ask2 = ['你叫什么啊', '你叫什么', '你的名字', '名字']

answer2 = ['程序员爸爸给我取了个，特响亮的名字，尼古拉斯.多罗夫斯基.菲菲，也可以叫我，聪明睿智长发肤白大波的菲菲', '尼古拉斯.多罗夫斯基.菲菲,来和我聊天吧']

time = ['time', '几点了', '几点钟了', '几点', '时间', '现在几点钟了']

weather = ['天气', 'weather', '今天的天气', '气温', '气候', 'tq', 'w']


# 当前时间
def answer(answeres):
    print('\n老王：' + answeres[random.randint(0, len(answeres) - 1)] + '\n')


# 阿里云 天气预报接口
def get_weather(city):
    url = 'https://jisutqybmf.market.alicloudapi.com/weather/query?city=' + city
    appcode = 'a19a7b24cf7a4691b8a8259be845ffaa'
    header = {'Authorization': 'APPCODE ' + appcode}
    content = requests.get(url=url, headers=header)
    if content.json() and content.json()['status'] == 0:
        result = content.json()['result']
        return '\n ' + result['city'] + ' ' + \
               result['date'] + ' ' + \
               result['week'] + ' ' + \
               '\n 天气：' + result['weather'] + \
               '\n 气温：' + result['temp'] + \
               '\n 最高气温：' + result['temphigh'] + \
               '\n 最低气温：' + result['templow']
    else:
        return '没有找到对应的城市信息QAQ'


# 青云客智能聊天机器人
def qingyunke(keywords):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + keywords
    response = requests.get(url=url)
    if response and response.json() and response.json()['result'] == 0:
        return response.json()['content']


# 对于词库中没有的问题 用户百度知道搜索答案

# 最近热门各大网站头条

while True:
    print('\n 小菲菲：欢迎您回来！来和我聊天吧 \n')
    ask = input('\n我说:')
    if ask and ask == 'heyu':
        print('\n 爸爸，你来了啊，菲菲可想你了，么么哒！\n')
    elif ask in ask1:
        answer(answer1)
    elif ask in ask2:
        answer(answer2)
    elif ask in time:
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('\n菲菲：' + current_time + '\n')
    elif ask in weather:
        city = input('\n 您想要查询的天气预报：')
        current_weather = get_weather(city)
        print('\n 菲菲小贴士：\n' + current_weather + '\n')
    else:
        qyk_result = qingyunke(ask)
        print('\n菲菲：' + qyk_result + '\n')
