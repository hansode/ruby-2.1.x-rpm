# What is this spec?

Forked from imeyer's ruby-1.9.2-rpm project at https://github.com/imeyer/ruby-1.9.2-rpm and updated for 2.0.0.

This spec is an attempt to push for a stable replacement of Ruby 1.8.x with 1.9.2+ on RHEL based systems. The original author based it off of the work of [FrameOS](http://www.frameos.org) specs for Ruby 1.9.2 and Ruby Enterprise Edition.

# Example to build SRPM and RPM

You need to install [VirtualBox](https://www.virtualbox.org/) and [Vagrant](http://www.vagrantup.com/).

```
$ vagrant up
$ vagrant ssh
$ mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
$ (cd ~/rpmbuild/SOURCES && curl -LO http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.5.tar.gz)
$ cp /vagrant/ruby21x.spec ~/rpmbuild/SPECS
$ sudo yum update -y
$ sudo yum install -y rpm-build
$ rpmbuild -ba ~/rpmbuild/SPECS/ruby21x.spec
エラー: ビルド依存性の失敗:
        readline-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        ncurses-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        gdbm-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        glibc-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        gcc は ruby-2.1.5-2.el6.x86_64 に必要とされています
        openssl-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        libyaml-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        libffi-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        zlib-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
$ sudo yum install -y readline-devel ncurses-devel gdbm-devel glibc-devel gcc openssl-devel libyaml-devel libffi-devel zlib-devel
$ rpmbuild -ba ~/rpmbuild/SPECS/ruby21x.spec
(snip)
書き込み完了: /home/vagrant/rpmbuild/SRPMS/ruby-2.1.5-2.el6.src.rpm
書き込み完了: /home/vagrant/rpmbuild/RPMS/x86_64/ruby-2.1.5-2.el6.x86_64.rpm
```

## How to build RPM from SRPM

```
$ vagrant up
$ vagrant ssh
$ sudo yum update -y
$ sudo yum install -y rpm-build
$ curl -LO https://github.com/feedforce/ruby-2.1.x-rpm/releases/download/2.1.5/ruby-2.1.5-2.el6.src.rpm
$ rpmbuild --rebuild ruby-2.1.5-2.el6.src.rpm
ruby-2.1.5-2.el6.src.rpm をインストール中です。
エラー: ビルド依存性の失敗:
        readline-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        ncurses-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        gdbm-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        glibc-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        gcc は ruby-2.1.5-2.el6.x86_64 に必要とされています
        openssl-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        libyaml-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        libffi-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
        zlib-devel は ruby-2.1.5-2.el6.x86_64 に必要とされています
$ sudo yum install -y readline-devel ncurses-devel gdbm-devel glibc-devel gcc openssl-devel libyaml-devel libffi-devel zlib-devel
$ rpmbuild --rebuild ruby-2.1.5-2.el6.src.rpm
(snip)
書き込み完了: /home/vagrant/rpmbuild/RPMS/x86_64/ruby-2.1.5-2.el6.x86_64.rpm
```
