#!/usr/bin/env python

import args
import sys
import os
#import subprocess
from fabric.operations import run, env
from fabric.main import main


env.user = args.user()
env.password = args.password()


def ssh(task):
    run(task)
    #for machine in target_parser.parse(sys.argv[1]):
        #process = subprocess.Popen([machine] + sys.argv[2:],
                                   #executable='ssh')

if __name__ == '__main__':
    hosts = reduce(lambda x, y: x + ';' + y, args.parse_targets(sys.argv[1]))

    if len(sys.argv) < 3:
        cmdline = reduce(lambda x, y: x.rstrip() + ' && ' + y,
                         sys.stdin.readlines())
    else:
        cmdline = reduce(lambda x, y: x + ' ' + y, sys.argv[2:])
    sys.argv = ['fab',
                '-f', __file__,
                'ssh:{0},hosts={1}'.format(cmdline, hosts)]
    if os.environ.get('SER_PSH') is None:
        sys.argv.append('-P')
    main()
