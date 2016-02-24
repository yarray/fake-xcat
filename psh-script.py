#!/usr/bin/env python

import args
import os
import sys

from fabric.operations import run, env, put
from fabric.main import main
from fabric.context_managers import hide, settings
from fabric.contrib.files import exists


env.user = args.user()
env.password = args.password()
temp_dir = '/tmp/'


def task(script, params):
    with hide('output'):
        if not exists(temp_dir):
            run('mkdir {0} 2>/dev/null'.format(temp_dir))
        put(script, temp_dir)
        remote_script = os.path.join(temp_dir, os.path.basename(script))
        run('chmod +x ' + remote_script)

    with settings(warn_only=True):
        print remote_script + ' ' + params
        run(remote_script + ' ' + params)


if __name__ == '__main__':
    hosts = reduce(lambda x, y: x + ';' + y, args.parse_targets(sys.argv[1]))
    if len(sys.argv) > 3:
        params = reduce(lambda x, y: x + ' ' + y, sys.argv[3:])
    else:
        params = ''

    sys.argv = ['fab',
                '-f', __file__,
                '-P',
                'task:{0},{1},hosts={2}'.format(sys.argv[2], params, hosts)]
    main()
