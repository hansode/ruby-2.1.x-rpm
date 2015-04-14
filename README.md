# What is this spec?

Forked from hansode's ruby-2.1.x-rpm project at https://github.com/hansode/ruby-2.1.x-rpm and updated for 2.2.2.

# Example to build SRPM and RPM

You need to install [VirtualBox](https://www.virtualbox.org/) and [Vagrant](http://www.vagrantup.com/).

```
$ vagrant up centos7
$ vagrant ssh centos7
$ mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}
$ (cd ~/rpmbuild/SOURCES && curl -LO http://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.2.tar.gz)
$ cp /vagrant/ruby22x.spec ~/rpmbuild/SPECS
$ sudo yum update -y
$ sudo yum install -y rpm-build
$ rpmbuild -ba ~/rpmbuild/SPECS/ruby22x.spec
エラー: ビルド依存性の失敗:
        readline-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        ncurses-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        gdbm-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        glibc-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        gcc は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        openssl-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        libyaml-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        libffi-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        zlib-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
$ sudo yum install -y readline-devel ncurses-devel gdbm-devel glibc-devel gcc openssl-devel libyaml-devel libffi-devel zlib-devel
$ rpmbuild -ba ~/rpmbuild/SPECS/ruby22x.spec
(省略)
書き込み完了: /home/vagrant/rpmbuild/SRPMS/ruby-2.2.2-1.el7.centos.src.rpm
書き込み完了: /home/vagrant/rpmbuild/RPMS/x86_64/ruby-2.2.2-1.el7.centos.x86_64.rpm
書き込み完了: /home/vagrant/rpmbuild/RPMS/x86_64/ruby-debuginfo-2.2.2-1.el7.centos.x86_64.rpm
```

## How to build RPM from SRPM

```
$ vagrant up centos7
$ vagrant ssh centos7
$ sudo yum update -y
$ sudo yum install -y rpm-build
$ curl -LO https://github.com/feedforce/ruby-rpm/releases/download/2.2.2/ruby-2.2.2-1.el7.centos.src.rpm
$ rpmbuild --rebuild ruby-2.2.2-1.el7.centos.src.rpm
ruby-2.2.2-1.el7.centos.src.rpm をインストール中です。
エラー: ビルド依存性の失敗:
        readline-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        ncurses-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        gdbm-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        glibc-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        gcc は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        openssl-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        libyaml-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        libffi-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
        zlib-devel は ruby-2.2.2-1.el7.centos.x86_64 に必要とされています
$ sudo yum install -y readline-devel ncurses-devel gdbm-devel glibc-devel gcc openssl-devel libyaml-devel libffi-devel zlib-devel
$ rpmbuild --rebuild ruby-2.2.2-1.el7.centos.src.rpm
(省略)
書き込み完了: /home/vagrant/rpmbuild/RPMS/x86_64/ruby-2.2.2-1.el7.centos.x86_64.rpm
書き込み完了: /home/vagrant/rpmbuild/RPMS/x86_64/ruby-debuginfo-2.2.2-1.el7.centos.x86_64.rpm
```
