#!/bin/env bash
HOME=/var/tmp

cd $HOME/rpmbuild/SOURCES && curl -LO https://cache.ruby-lang.org/pub/ruby/2.2/ruby-$(cat ruby-version).tar.gz

rpmbuild -ba $HOME/rpmbuild/SPECS/ruby22x.spec

cp $HOME/rpmbuild/RPMS/x86_64/* /shared/
