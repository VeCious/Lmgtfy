#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @version : 0.1
    # TODO
'''

import sys, os, time

'''  '''
ScriptName = 'Lmgtfy'
Description = 'Posts a link to lmgtfy.com'
Website = ''
Creator = 'Ve'
Version = '0.1'

'''  '''

'''  '''
Log = lambda x, *args: Parent.Log(ScriptName, x.format(*args)) #pylint: disable=E0602


'''  '''
def Init():
    return

def Tick():
    return

def Unload():
    return

def ReloadSettings(data):
    return

'''  '''
def Execute(data):
    if not data.IsChatMessage() or data.GetParam(0) != '!lmgtfy':
        return
    else:
        Log('Data: {0}', data.GetParam(0))
        Log('Count: {0}', data.GetParamCount())
        args_count = data.GetParamCount()

        if args_count <= 1:
            return 
        
        args = []
        for i in range(1, args_count):
            args.append(data.GetParam(i))
        user = '@' + data.UserName
        url = 'http://lmgtfy.com/?q={0}'.format('+'.join(args))
        msg = 'Let me Google that for your {0}. {1}'.format(user, url)
        Parent.SendStreamMessage(msg) #pylint: disable=E0602
    return