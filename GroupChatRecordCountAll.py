import json

# 聊天记录json所在位置
with open("/Users/zhangyunfan/Desktop/123.json", 'r') as content_j:
    load_dict = json.load(content_j)
member_dict = {}
for key in load_dict["member"].keys():
    member_dict[key] = load_dict["member"][key]['name']
d = {}
for message in load_dict['message']:
    key = ''
    if message['m_nsRealChatUsr'] in member_dict:
        key = member_dict[message['m_nsRealChatUsr']]
        if member_dict[message['m_nsRealChatUsr']] == '':
            key = '自己的账号'
    else:
        key = '未知用户'
    if key in d:
        d[key] = d[key] + 1
    else:
        d[key] = 1

a = sorted(d.items(), key=lambda kv: (kv[1], kv[0]))
print(a)
for key in a:
    print('用户名是'+key[0]+'发言数是'+str(key[1]))
