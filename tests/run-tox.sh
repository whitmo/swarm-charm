#!/bin/bash
readonly PROGDIR=$(readlink -m $(dirname $0))

pushd .
tox -- $PROGDIR
popd
