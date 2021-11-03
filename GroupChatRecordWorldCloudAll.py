import json
import re
import jieba
from PIL import Image
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt


def check(str):
    my_re = re.compile(r'[A-Za-z]', re.S)
    res = re.findall(my_re, str)
    if len(res):
        return False
    else:
        return True


# 聊天记录json所在位置
with open("/Users/zhangyunfan/Desktop/123.json", 'r') as content_j:
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
    # 设置背景形状
    coloring = np.array(Image.open("testmask.jpeg"))
    # 初始化词云组建，字体用爱心字体，也可以用普通的字体——simsun.ttf
    w = WordCloud(width=800, height=400, font_path='sweet.ttf', background_color="white",
                  max_words=500, mask=coloring, max_font_size=200, random_state=200, stopwords=stopwords)
    # 注入我们分好词了的内容
    w.generate(target)
    # 设置字体颜色和整体颜色
    image_colors = ImageColorGenerator(coloring)
    plt.figure(figsize=(20, 10))
    plt.imshow(
        w.recolor(color_func=image_colors),
        interpolation='bilinear'
    )
    plt.axis("off")
    plt.show()
    # 输出png格式的图片
    w.to_file("/Users/zhangyunfan/Desktop/qiaoqiao.png")
