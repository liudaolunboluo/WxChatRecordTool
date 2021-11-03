import json
import time
import datetime


def string_toTimestamp(st):
    return time.mktime(time.strptime(st, "%Y-%m-%d %H:%M:%S"))


# 聊天记录json所在位置
with open("/Users/zhangyunfan/Desktop/message.json", 'r') as content_j:
    load_dict = json.load(content_j)
member_dict = {}
for key in load_dict["member"].keys():
    member_dict[key] = load_dict["member"][key]['name']
member_count = {}
count = 0
for message in load_dict['message']:
    key = ''
    # 只统计今天的
    if int(message['m_uiCreateTime']) < string_toTimestamp(str(datetime.date.today()) + " 00:00:00"):
        continue
    if message['m_nsRealChatUsr'] in member_dict:
        key = member_dict[message['m_nsRealChatUsr']]
        if member_dict[message['m_nsRealChatUsr']] == '':
            key = '自己'
    else:
        key = '未知用户'
    count = count + 1
    if key in member_count:
        member_count[key] = member_count[key] + 1
    else:
        member_count[key] = 1

a = sorted(member_count.items(), key=lambda kv: (kv[1], kv[0]))
for key in a:
    print('用户名是' + key[0] + '发言数是' + str(key[1]))
print('今日发言总数：'+str(count))