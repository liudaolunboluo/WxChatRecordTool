import json
import time
import jieba
from collections import defaultdict
import re
from wordcloud import WordCloud, ImageColorGenerator
import sys


class WxRecord:

    def __init__(self, create_time, to_user, from_user):
        self.create_time = create_time
        # 我发给他
        self.to_user = to_user
        # 他发给我
        self.from_user = from_user


def convertTime(m_uiCreateTime):
    time_arr = time.localtime(m_uiCreateTime)
    result = time.strftime("%Y-%m-%d", time_arr)
    return result


def convertTimeWithMin(m_uiCreateTime):
    time_arr = time.localtime(m_uiCreateTime)
    result = time.strftime("%Y-%m-%d %H:%M:%S", time_arr)
    return result


def string_toTimestamp(st):
    return time.mktime(time.strptime(st, "%Y-%m-%d %H:%M:%S"))


def make_word_clound(content, output_path):
    # 将聊天记录分词
    seg_list = jieba.cut(content, cut_all=True)
    target = "/ ".join(seg_list)
    # 停词，主要是去掉一些语气词，比如"了"、"的"
    stopwords = open("stopwords.txt", encoding='UTF-8').read().split("\n")
    # 初始化词云组建
    w = WordCloud(width=800, height=400, font_path='simsun.ttf', background_color="white",
                  max_words=500, max_font_size=200, random_state=200, stopwords=stopwords)
    # 注入我们分好词了的内容
    w.generate(target)
    # 输出png格式的图片
    w.to_file(output_path + '/result.png')
    return output_path + '/result.png'


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
with open(message_path, 'r', encoding='UTF-8') as content_j:
    load_dict = json.load(content_j)
    # 聊天对象
    user_name = load_dict['owner']['name']
    content = ''
    wxRecord_list = []
    # 按照日期分组的聊天记录
    date_map = defaultdict(list)
    for message in load_dict['message']:
        # 只统计今年的
        if int(message['m_uiCreateTime']) > string_toTimestamp("2021-01-01 00:00:00"):
            record = WxRecord(message['m_uiCreateTime'], message['m_nsFromUsr'] == "", message['m_nsToUsr'] == "")
            wxRecord_list.append(record)
            date_map[convertTime(record.create_time)].append(record)
            if check(message['m_nsContent']):
                content = content + ' ' + message['m_nsContent']

    # 每天最晚的映射，key是年月日 value是时分秒
    late_record_map = {}
    # 每个日期对应聊天记录的数量
    date_count_map = {}
    for date in date_map:
        record_list = date_map[date]
        record_list.sort(key=lambda x: x.create_time, reverse=True)
        create_time = convertTimeWithMin(record_list[0].create_time)
        late_record_map[create_time.split(' ')[0]] = create_time.split(' ')[1]
        date_count_map[date] = len(date_map[date])

    to_user_list = [val for val in wxRecord_list if val.to_user]
    from_user_list = [val for val in wxRecord_list if val.from_user]
    date_count_map = sorted(date_count_map.items(), key=lambda item: item[1], reverse=True)
    late_record = ()
    # 遍历排序之后的可以少遍历几次
    late_record_map = sorted(late_record_map.items(), key=lambda item: item[1])
    for date in late_record_map:
        hms_str = date[1]
        # 取出小时数，小于6点的就算是凌晨晚上的消息，是最晚的消息
        if (int(hms_str.split(':')[0]) < 6):
            late_record = date
    # 输出结果
    print('今年，你和{}一共有{}天有过交流，你们一共互相发了{}条信息，你发给{}发了{}条消息，{}给你发了{}条消息。在{}这一天你们一共发了{}条消息，在{}这一天你们在深夜{}还在聊天'
          .format(user_name, len(date_map), len(wxRecord_list), user_name, len(to_user_list), user_name,
                  len(from_user_list), list(date_count_map)[0][0], list(date_count_map)[0][1], late_record[0],
                  late_record[1]))
    # 保留每个统计点的输出，便于后面扩展改造
    # print('今年你和{}一共有{}天有过交流'.format(user_name, len(date_map)))
    # print('你和{}一共互相发了{}条信息'.format(user_name, len(wxRecord_list)))
    # print('其中你发给{}{}条消息'.format(user_name, len(to_user_list)))
    # print('{}发给你{}条消息'.format(user_name, len(from_user_list)))
    # print('聊天最多的一天是{},这一天你们一共发了{}条消息'.format(list(date_count_map)[0][0], list(date_count_map)[0][1]))
    # print('{}这一天你们{}还在发消息'.format(late_record[0], late_record[1]))
    make_word_clound(content, output_path)
