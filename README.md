fake-xcat
=========

convenient tools for system management when xcat from IBM or similar tools are not available, or the ssh login without password is not set

## Basics

1. Define your own nodes definition files. Refer to nodes.cfg for examples. Nodes can be defined as follows:
    * node1,node2,node3
    * group1,node2
    * node1:node3 # will be resolved according to the "all" group
2. When execute the scripts, they will try to find local nodes.cfg. If there is none, they will use ~/.nodes.cfg
3. Parallel execution is default. Set SER_PSH to force a serialized execution

## Commands

### psh.py

`./psh.py <nodes> <command>`

The format of "nodes" are the same as those in nodes.cfg. It is highly recommended to wrap command in double quoates

Examples:

`./psh.py group "service network restart"`

`./psh.py node1,node2 "service network restart"`

`./psh.py node1:node3 "service network restart"`

`./psh.py group,node3 "service network restart"`

### psh-scripts.py

`./psh-scripts.py <nodes> <command>`

The psh-scripts tool push a script to remote machines and execute it locally.
It is highly useful when the commands are too complex and cannot be written inline.

### pscp-py

Push to multiple remote machines

`./pscp.py <file> <nodes>:<file>`

For getting please use normal scp
