#!/bin/sh

set -xe

CENTOS_MAJOR_VERSION=$1
DOCKER_IMAGE=centos${CENTOS_MAJOR_VERSION}/ruby-rpm
docker run -u builder -v $CIRCLE_ARTIFACTS:/shared:rw $DOCKER_IMAGE ./build-ruby.sh
