# Swarm Charm

This subordinate charm turns a set of docker hosts (deployed with the
docker charm) into a swarm cluster.

## How to use

Let's deploy from this repo:

    mkdir trusty && pushd . && cd trusty
    git clone http://github.com/whitmo/swarm-charm.git swarm
    pop
    export JUJU_REPOSITORY=`pwd`

Deploy the cluster:

    juju deploy docker && juju set docker latest=true
    juju deploy cs:~hazmat/etcd
    juju deploy local:trusty/swarm
    juju add-relation swarm docker
    juju add-relation etcd swarm

Scale the cluster:

    juju add-unit -n3 docker


## Caveats

Currently

 - only supports discovery w/ etcd
 - does not implement TLS

Adding discovery from file, ip, zookeeper and consul should be
relatively easy.
