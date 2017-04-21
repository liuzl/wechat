# -*- encoding: utf-8 -*-
import itchat
from itchat.content import *

itchat.auto_login(enableCmdQR=2)

@itchat.msg_register
def general_reply(msg):
    print msg
    return msg

itchat.run()
