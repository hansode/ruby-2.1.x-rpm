#!/bin/sh -xe

VERSION=$1

docker_archive=$HOME/cache/centos$VERSION-ruby-rpm.tar.gz
docker_image=centos$VERSION/ruby-rpm
docker_file=Dockerfile-$VERSION
md5_digest_file=$HOME/cache/dockerfile$VERSION.digest

can_use_cache() {
  md5sum --status --quiet --check $md5_digest_file> /dev/null 2>&1
}

if can_use_cache; then
  docker load < $docker_archive
else
  mkdir -p $HOME/cache
  md5sum $HOME/$CIRCLE_PROJECT_REPONAME/$docker_file > $md5_digest_file
  docker build -t $docker_image -f $docker_file .
  docker save $docker_image | gzip -c > $docker_archive
fi

docker info

docker run -v $CIRCLE_ARTIFACTS:/shared:rw $docker_image /bin/sh ./rubybuild.sh
