#!/bin/sh
WORK_DIR=/var/tmp
RUBY_VERSION=$(cat ruby-version)
RUBY_MINOR_VER=$(echo $RUBY_VERSION | sed -e "s@\.[0-9]$@@")

cd $WORK_DIR/rpmbuild/SOURCES && curl -LO https://cache.ruby-lang.org/pub/ruby/$RUBY_MINOR_VER/ruby-$RUBY_VERSION.tar.gz

rpmbuild -ba $WORK_DIR/rpmbuild/SPECS/ruby.spec

cp $WORK_DIR/rpmbuild/RPMS/x86_64/* /shared/
