# -*- coding: utf-8 -*-

from FakeClient.core import client

class command_handler(object):

    def __init__(self, sys_args):
        self.sys_args = sys_args
        if len(self.sys_args) < 2:
            exit(self.help_msg())
        self.command_allowcator()
    # 分拣用户输入的不同指令
    def command_allowcator(self):
        print(self.sys_args)

        if hasattr(self, self.sys_args[1]):
            func = getattr(self, self.sys_args[1])
            return func()
        else:
            print("command does not exist!")
            self.help_msg()

    def help_msg(self):
        valid_commands = '''
        start   start monitor client
        stop    stop monitor client
        '''
        exit(valid_commands)

    def start(self):
        print("start!")

        Client = client.ClientHandle()
        Client.forever_run()

    def stop(self):
        print("stop!")