#!/bin/env bash
HOME=/var/tmp
RUBY_VERSION=$(cat ruby-version)
RUBY_MINOR_VER=$(echo $test | sed -e "s/\([0-9]\.[0-9]\).*/\1/")

cd $HOME/rpmbuild/SOURCES && curl -LO https://cache.ruby-lang.org/pub/ruby/$RUBY_MINOR_VER/ruby-$RUBY_VERSION.tar.gz

rpmbuild -ba $HOME/rpmbuild/SPECS/ruby.spec

cp $HOME/rpmbuild/RPMS/x86_64/* /shared/
