# coding=utf-8
import os
import time
import itchat

import util

SINCERE_WISH =  u'🌙2019万事如意 春节快乐呀🌙 '

def save_friend(friends, fsname):
    dct = util.load_friends(friends[1:])
    util.write_friends(fsname, dct)
    print("您的friend列表文件已经创建成功，文件名：", fsname)
    time.sleep(.2)
    print("现在可以修改文件：1)$前的数据不要修改;2)可以修改$后面的称呼;3)如果不想发送，则注释或者删除均可;")
    time.sleep(.3)
    print("如果希望直接以称呼名为准，请在称呼名后加入‘-’，否则默认在称呼名后加上‘同学’二字!")
    time.sleep(.2)
    print("修改完成后，请重新运行当前脚本")

def send_msg(friends, fsname):
    dct = util.read_friends(fsname)
    print("total friends:", len(friends[1:]))
    # 发送数目统计
    Title = '同学'
    send_count, not_sends, sends= 0, [], []

    if dct:
        print(u"您要发送 %s 条数据" % len(dct))
        print("开始发送微信消息...")
        for friend in friends:
            # 如果是演示目的，把下面的方法改为print即可
            # 正式需要发送，把 itchat.send 那一行前面的＃删掉即可
            if dct.get(friend['NickName']):
                showname = dct[friend['NickName']]
                if friend['NickName'] in sends : continue
                # 如果showName包含“-”，则直接replace掉“-”，不添加Title
                if '-' in showname:
                    xmsg = SINCERE_WISH
                    showname = showname.replace('-', '')
                    Title = ''
                else:
                    xmsg = SINCERE_WISH
                    Title = '同学'
                msg = "{}! {}".format(xmsg, showname+Title) 
                print(msg, friend['UserName'])
                #itchat.send(msg, friend['UserName'])
                send_count = send_count + 1
                sends.append(friend['NickName'])
                time.sleep(.5)
            else:
                not_sends.append(friend['NickName'])
        #for
        info = "send count:{} not send:{} --".format(send_count, len(not_sends))
        print(info ) # , not_sends)

def main():
    itchat.auto_login(hotReload=True)
    
    friends = itchat.get_friends(update=True)
    fsname = util.get_friend_file(friends[0]['NickName'])
    if not os.path.exists(fsname):
        save_friend(friends, fsname)
    else:
        send_msg(friends, fsname)

if __name__ == "__main__":
    main()