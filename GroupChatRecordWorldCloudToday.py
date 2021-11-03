import json
import re
import jieba
import time
import datetime
from wordcloud import WordCloud, ImageColorGenerator


def check(str):
    my_re = re.compile(r'[A-Za-z]', re.S)
    res = re.findall(my_re, str)
    if len(res):
        return False
    else:
        return True


def string_toTimestamp(st):
    return time.mktime(time.strptime(st, "%Y-%m-%d %H:%M:%S"))


# 聊天记录json所在位置
with open("/Users/zhangyunfan/Desktop/message.json", 'r') as content_j:
    load_dict = json.load(content_j)
    # 从导出的聊天记录中剥离出聊天内容
    content = ''
    for message in load_dict['message']:
        # 只统计今天的
        if int(message['m_uiCreateTime']) < string_toTimestamp(str(datetime.date.today()) + " 00:00:00"):
            continue
        if check(message['m_nsContent']):
            content = content + ' ' + message['m_nsContent']
    # 将聊天记录分词
    seg_list = jieba.cut(content, cut_all=True)
    target = "/ ".join(seg_list)
    # 停词，主要是去掉一些语气词，比如"了"、"的"
    stopwords = open("stopwords.txt").read().split("\n")
    # 初始化词云组建，字体用爱心字体，也可以用普通的字体——simsun.ttf
    w = WordCloud(width=800, height=400, font_path='simsun.ttf', background_color="white",
                  max_words=500, max_font_size=200, random_state=200, stopwords=stopwords)
    # 注入我们分好词了的内容
    w.generate(target)
    # 输出png格式的图片
    w.to_file("/Users/zhangyunfan/Desktop/message.png")
