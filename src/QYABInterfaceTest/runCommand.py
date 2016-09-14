# -*- coding: UTF-8 -*-

'''
Created on 2016年9月10日

@author: NJNUGGET
'''
import threading
import os
from cmd import Cmd
class runCommand(threading.Thread):

    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        print('now in runServer.run')
        os.system(self.cmd)
        
    def exeCommand(self,caps):
        cmd = 'ab'+' -n'+caps['requestnum']+' -c'+caps['usersnum']+' '+caps['address']
#         os.system(cmd)
        runCommand(cmd)