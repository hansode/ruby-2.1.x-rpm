FROM centos:6.6
MAINTAINER hirokazu SUGIUCHI

# setup
RUN yum update -y
RUN yum install -y rpm-build tar

# ruby depends
RUN yum -y install readline-devel ncurses-devel gdbm-devel glibc-devel gcc openssl-devel libyaml-devel libffi-devel zlib-devel

# build
RUN mkdir -p /var/tmp/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
WORKDIR /var/tmp/rpmbuild
ADD rubybuild.sh /var/tmp/rpmbuild/rubybuild.sh
ADD ruby22x.spec /var/tmp/rpmbuild/SPECS/ruby22x.spec
