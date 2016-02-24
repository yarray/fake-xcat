#!/usr/bin/env python

import args
import sys
from fabric.operations import put, env
from fabric.main import main


env.user = args.user()
env.password = args.password()


def _parse(target_desc, dest_desc):
    return (target_desc, dest_desc.split(':')[-1],
            dest_desc[:dest_desc.rindex(':')])


if __name__ == '__main__':
    target, dest, host_desc, mode = _parse(sys.argv[1], sys.argv[2])
    hosts = reduce(lambda x, y: x + ';' + y, args.parse_targets(host_desc))
    sys.argv = ['fab',
                '-f', __file__,
                'put:{0},{1},hosts={2}'.format(target, dest, hosts)]
    main()
