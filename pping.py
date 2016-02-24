#!/usr/bin/env python

from args import parse_targets
import sys
import subprocess
from threading import Thread


class ping(Thread):
    def __init__(self, ip):
        Thread.__init__(self)
        self.ip = ip
        self.status = False

    def run(self):
        self.status = subprocess.call(['ping', '-q', '-c1', self.ip]) == 0


tasks = []


for host in parse_targets(sys.argv[1]):
    current = ping(host)
    tasks.append(current)
    current.start()


for task in tasks:
    task.join()
    print task.ip + ': ' + ('ping' if task.status else 'noping')
