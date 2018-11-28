#!/usr/bin/env python3

import os

class Command():
    def __init__(self, args):
        pass

class ListProcs(Command):
    def __init__(self, args):
        pass

    def run(self):
        proc = "/proc"
        for d in os.listdir("/proc"):
            if os.path.isdir(proc + "/" + d) and d.isdigit():
                print(d)
                
class SendSignal(Command): // added by Marius
    def __init__(self, args):
        pass

    def run(self, pid):
        os.kill(pid, signal.SIGUSR1)

class showMem:
    def __init__(self, args):
        self.arg = args

    def run(self):
        DIR = '/proc/'
        process = self.arg[0]
        path = DIR + process + '/status'
        exst = False
        for n,line in enumerate(open(path)):
            if line[:6] == 'VmSize':
                exst = True
                print (line[10:])
        if not exst: 
                print ('No status')    
  
commands = {
    "list" : lambda args: ListProcs(args), 
    "sm": lambda args: showMem(args)
    "send_signal": lambda pid: SendSignal(pid) // added by Marius
}



def get_command():
    strs = input("> ").split()
    try:
        cmd = commands[strs[0]](strs[1:])
    except KeyError as e:
        print("Unknown command")
    return cmd

while True:
    cmd = get_command()
    cmd.run()
