#!/usr/bin/env python

import args
import sys
import os
from fabric.operations import env
from fabric.main import main


env.user = args.user()
env.password = args.password()


def task(script):
    __import__(os.path.splitext(script)[0]).main()


if __name__ == '__main__':
    hosts = reduce(lambda x, y: x + ';' + y, args.parse_targets(sys.argv[1]))
    sys.argv = ['fab',
                '-f', __file__,
                'task:{0},hosts={1}'.format(sys.argv[2], hosts)]
    main()
