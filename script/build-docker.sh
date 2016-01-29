#!/bin/sh -xe

CENTOS_VERSION=$1

docker_archive=$HOME/cache/centos${CENTOS_VERSION}-ruby-rpm.tar.gz
docker_image=centos${CENTOS_VERSION}/ruby-rpm
docker_file=Dockerfile-${CENTOS_VERSION}

md5_digest_source=md5_digest.source-${CENTOS_VERSION}
md5_digest_path=$HOME/cache/dockerfile${CENTOS_VERSION}.digest

can_use_cache() {
  test -e $docker_archive &&
    md5sum --status --quiet --check $md5_digest_file > /dev/null 2>&1
}

md5_digest_source() {
  # Consider Dockerfile and the related files
  cat $DOCKER_FILE $(grep '^ADD ' $DOCKER_FILE | awk '{$1=""; $NF=""; print $0}')
}

if [ ! -f "$docker_file" ]; then
  echo "$docker_file is not exist." >&2
  exit 1
fi

cd $HOME/$CIRCLE_PROJECT_REPONAME

md5_digest_source > $md5_digest_source

if can_use_cache; then
  docker load < $docker_archive
else
  mkdir -p $HOME/cache
  md5sum $md5_digest_source > $md5_digest_path
  docker build -t $docker_image -f $docker_file .
  docker save $docker_image | gzip -c > $docker_archive
fi

docker info
