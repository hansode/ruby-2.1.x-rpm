#!/bin/sh

set -xe

RUBY_X_Y_Z_VERSION=$(grep "%define \+rubyver" $HOME/rpmbuild/SPECS/ruby.spec | awk '{print $3}')
RUBY_X_Y_VERSION=$(echo $RUBY_X_Y_Z_VERSION | sed -e 's@\.[0-9]$@@')

cd $HOME/rpmbuild/SOURCES && curl -LO https://cache.ruby-lang.org/pub/ruby/$RUBY_X_Y_VERSION/ruby-$RUBY_X_Y_Z_VERSION.tar.gz

rpmbuild -ba $HOME/rpmbuild/SPECS/ruby.spec

cp $HOME/rpmbuild/RPMS/x86_64/* /shared
cp $HOME/rpmbuild/SRPMS/* /shared
