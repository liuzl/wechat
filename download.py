# -*- encoding: utf-8 -*-
import itchat
from itchat.content import *
import json

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

#个人消息系列

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    print '\n\nDOWNLOAD\n\n'
    print msg['Text']
    ret = msg['Text']("./media/"+msg['FileName'])
    print ret
    #msg.download(msg.fileName)
    #typeSymbol = {
    #    PICTURE: 'img',
    #    VIDEO: 'vid', }.get(msg.type, 'fil')
    #print '@%s@%s' % (typeSymbol, msg.fileName)
    print msg


itchat.auto_login(hotReload=True)
itchat.run()
itchat.dump_login_status()
