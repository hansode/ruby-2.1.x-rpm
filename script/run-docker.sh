#!/bin/sh -xe

CENTOS_VERSION=$1
docker_image=centos${CENTOS_VERSION}/ruby-rpm
docker run -u rpmbuilder -v $CIRCLE_ARTIFACTS:/shared:rw $docker_image ./rubybuild.sh
