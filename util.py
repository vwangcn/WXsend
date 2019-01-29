import os

ROOTDIR = '.'
DATADIR = 'data'

def get_message_file(nickname):
    dir = "{1}{0}{2}".format(os.sep, ROOTDIR, DATADIR)
    if not os.path.exists(dir):
        os.mkdir(dir)
    fsname = "{1}{0}{2}-msg.txt".format(os.sep, dir, nickname)
    return fsname

def get_friend_file(nickname):
    dir = "{1}{0}{2}".format(os.sep, ROOTDIR, DATADIR)
    if not os.path.exists(dir):
        os.mkdir(dir)
    fsname = "{1}{0}{2}.txt".format(os.sep, dir, nickname)
    return fsname

def read_message(fsname='msg.txt'):
    with open(fsname, encoding='utf-8') as handler:
        content = handler.read()
    return content

def read_friends(fsname):
    dct = {}
    if not os.path.exists(fsname): return dct
    
    with open(fsname, encoding='utf-8') as handler:
        lines = handler.readlines()
    
    for line in lines:
        line = line.strip()
        if len(line) == 0: continue
        if line[0] == '#': continue
        items = line.split('$')
        dct[items[0]] = items[1]
    #for
    return dct

def write_friends(fsname, dct):
    with open(fsname, 'a+', encoding='utf-8') as handler:
        for key, value in dct.items():
            line = "{}${}\n".format(key, value)
            handler.write(line)
        #for
    #with

def load_friends(friends):
    dct = {}
    for friend in friends:
        dct[friend['NickName']] = friend['RemarkName'] or friend['DisplayName'] or friend['NickName']
    #for
    return dct