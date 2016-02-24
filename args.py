import ConfigParser
import doctest
import os


def _replace_with_multi(container, old, new_items):
    i = container.index(old)
    container.remove(old)
    for item in reversed(new_items):
        container.insert(i, item)


def _parse_nodes(nodes_abbrev, all_nodes):
    node_range = [all_nodes.index(node) for node in nodes_abbrev.split(':')]
    if len(node_range) > 1:
        return all_nodes[node_range[0]:node_range[1] + 1]
    else:
        return [nodes_abbrev]


def _parse_targets(desc, cfg):
    '''
    >>> cfg = ConfigParser.ConfigParser()
    >>> l = cfg.read(['test_nodes.cfg'])
    >>> _parse_targets('carto', cfg)
    ['node02', 'node03', 'node04', 'node05']

    >>> _parse_targets('node01,node02,node03', cfg)
    ['node01', 'node02', 'node03']

    >>> _parse_targets('node01:node03,node04:node06', cfg)
    ['node01', 'node02', 'node03', 'node04', 'node05', 'node06']

    >>> _parse_targets('compute', cfg)
    ['node07', 'node08', 'node09']

    >>> _parse_targets('compute,database', cfg)
    ['node07', 'node08', 'node09', 'node06']

    >>> _parse_targets('node100', cfg)
    ['node100']
    '''
    all_nodes = cfg.get('groups', 'all').split(',')

    # split targets
    targets = desc.split(',')

    for t in targets:
        if t in cfg.options('groups'):
            _replace_with_multi(targets, t, cfg.get('groups', t).split(','))

    # parse abbrevation
    for t in targets:
        if ':' in t:
            _replace_with_multi(targets,
                                t,
                                _parse_nodes(t, all_nodes))

    return targets


cfg = ConfigParser.ConfigParser()
if os.path.isfile('nodes.cfg'):
    cfg.read(['nodes.cfg'])
else:
    cfg.read([os.path.join(os.path.expanduser('~'), '.nodes.cfg')])


def parse_targets(nodes):
    return _parse_targets(nodes, cfg)


def parse_test(nodes):
    cfg = ConfigParser.ConfigParser()
    cfg.read(['test_nodes.cfg'])

    return _parse_targets(nodes, cfg)


def user():
    return cfg.get('users', 'name')


def password():
    return cfg.get('users', 'password')


if __name__ == '__main__':
    doctest.testmod()
