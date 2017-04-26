# -*- encoding: utf-8 -*-
import itchat
from itchat.content import *
import json
import time

data_dir = "./data/"
media_dir = "./media/"

'''
TEXT    文本    文本内容
MAP    地图    位置文本
CARD    名片    推荐人字典
NOTE    通知    通知文本
SHARING    分享    分享名称
PICTURE    图片/表情    下载方法
RECORDING    语音    下载方法
ATTACHMENT    附件    下载方法
VIDEO    小视频    下载方法
FRIENDS    好友邀请    添加好友所需参数
SYSTEM    系统消息    更新内容的用户或群聊的UserName组成的列表
'''

def save(msg):
    file_name = "%s%s.json" % (data_dir, time.strftime('%Y%m%d', time.localtime()))
    out = open(file_name,'a')
    line = "%s\n" % json.dumps(msg, ensure_ascii=False)
    print type(line)
    out.write(line.encode('utf-8'))
    out.flush()
    out.close()

#个人消息系列

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    save(msg)

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text']("%s%s" % (media_dir, msg['FileName']))
    save(msg)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    #msg.user.verify()
    #msg.user.send('Nice to meet you!')
    save(msg)

@itchat.msg_register(SYSTEM)
def system_msg(msg):
    #msg.user.verify()
    #msg.user.send('Nice to meet you!')
    save(msg)

#群消息系列

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING], isGroupChat=True)
def qun_text_reply(msg):
    save(msg)

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def qun_download_files(msg):
    #msg.download(msg.fileName)
    #typeSymbol = {
    #    PICTURE: 'img',
    #    VIDEO: 'vid', }.get(msg.type, 'fil')
    #print '@%s@%s' % (typeSymbol, msg.fileName)
    msg['Text']("%s%s" % (media_dir, msg['FileName']))
    save(msg)

itchat.auto_login(hotReload=True)
itchat.run()
itchat.dump_login_status()
