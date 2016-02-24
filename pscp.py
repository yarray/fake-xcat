#!/usr/bin/env python

import args
import sys
from fabric.operations import put, get, env
from fabric.main import main


env.user = args.user()
env.password = args.password()


def ssh(target, dest, mode):
    if mode == 'put':
        put(target, dest)
    else:
        get(target, dest)


def _parse(target_desc, dest_desc):
    print dest_desc
    to_remote = (':' in dest_desc)

    if to_remote:
        return (target_desc, dest_desc.split(':')[1],
                dest_desc.split(':')[0], 'put')
    else:
        return (target_desc.split(':')[1], dest_desc,
                target_desc.split(':')[0], 'get')


if __name__ == '__main__':
    target, dest, host_desc, mode = _parse(sys.argv[1], sys.argv[2])
    hosts = reduce(lambda x, y: x + ';' + y, args.parse_targets(host_desc))
    sys.argv = ['fab',
                '-f', __file__,
                'ssh:{0},{1},{2},hosts={3}'.format(target,
                                                   dest, mode, hosts)]
    main()
