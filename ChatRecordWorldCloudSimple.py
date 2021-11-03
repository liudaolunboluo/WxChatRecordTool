import json
import re
import jieba
from PIL import Image
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import sys


def check(str):
    my_re = re.compile(r'[A-Za-z]', re.S)
    res = re.findall(my_re, str)
    if len(res):
        return False
    else:
        return True


if len(sys.argv) < 3:
    print("请输入参数")
    exit()
message_path = sys.argv[1]
output_path = sys.argv[2]
if len(message_path) == 0:
    print("请输入聊天记录的路径")
    exit()
if len(output_path) == 0:
    print("请输入输出图片的路径")
    exit()
with open(message_path, 'r') as content_j:
    load_dict = json.load(content_j)
    # 从导出的聊天记录中剥离出聊天内容
    content = ''
    for message in load_dict['message']:
        if check(message['m_nsContent']):
            content = content + ' ' + message['m_nsContent']
    # 将聊天记录分词
    seg_list = jieba.cut(content, cut_all=True)
    target = "/ ".join(seg_list)
    # 停词，主要是去掉一些语气词，比如"了"、"的"
    stopwords = open("stopwords.txt").read().split("\n")
    # 初始化词云组建
    w = WordCloud(width=800, height=400, font_path='simsun.ttf', background_color="white",
                  max_words=500, max_font_size=200, random_state=200, stopwords=stopwords)
    # 注入我们分好词了的内容
    w.generate(target)
    # 输出png格式的图片
    w.to_file(output_path + '/simpleresult.png')