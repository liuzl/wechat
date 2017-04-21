# -*- encoding: utf-8 -*-
import itchat
from itchat.content import *
import json

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    print(json.dumps(msg, ensure_ascii=False))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    print '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    #msg.user.verify()
    #msg.user.send('Nice to meet you!')
    print(json.dumps(msg, ensure_ascii=False))

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    print(json.dumps(msg, ensure_ascii=False))

itchat.auto_login(hotReload=True)
itchat.run()
itchat.dump_login_status()
