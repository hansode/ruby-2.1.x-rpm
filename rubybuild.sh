#!/bin/sh
WORK_DIR=/var/tmp
RUBY_VERSION=$(cat $WORK_DIR/rpmbuild/SOURCES/ruby-version)
RUBY_MINOR_VER=$(echo $RUBY_VERSION | sed -e 's@\.[0-9]$@@')

cd $HOME/rpmbuild/SOURCES && curl -LO https://cache.ruby-lang.org/pub/ruby/$RUBY_MINOR_VER/ruby-$RUBY_VERSION.tar.gz

rpmbuild -ba $HOME/rpmbuild/SPECS/ruby.spec

cp $HOME/rpmbuild/RPMS/x86_64/* /shared/
