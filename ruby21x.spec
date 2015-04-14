%define rubyver         2.1.5
%define rubyabi         2.1

Name:           ruby
Version:        %{rubyver}
Release:        2%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  readline readline-devel ncurses ncurses-devel gdbm gdbm-devel glibc-devel tcl-devel gcc unzip openssl-devel db4-devel byacc make libyaml libyaml-devel libffi libffi-devel
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages
Provides: ruby(abi) = %{rubyabi}
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Provides: rubygems
Obsoletes: ruby < %{rubyabi}
Obsoletes: ruby-libs < %{rubyabi}
Obsoletes: ruby-irb < %{rubyabi}
Obsoletes: ruby-rdoc < %{rubyabi}
Obsoletes: ruby-devel < %{rubyabi}
Obsoletes: rubygems < %{rubyabi}

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --enable-shared \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir}

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

#we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}/*
%{_includedir}/*
%{_datadir}/*
%{_libdir}/*

%changelog
* Tue Apr 14 2015 Johnson Earls <johnson.earls@oracle.com> - 2.1.5-2
- Fix Obsoletes header lines to allow for ruby package updates

* Fri Dec  5 2014 Tony Doan <tdoan@tdoan.com> - 2.1.5
- Update ruby version to 2.1.5

* Fri May  9 2014 Masahito Yoshida <masahito@axsh.net> - 2.1.2
- Update ruby version to 2.1.2

* Thu Dec 26 2013 Masahito Yoshida <masahito@axsh.net> - 2.1.0
- Update ruby version to 2.1.0

* Sat Nov 23 2013 Masahito Yoshida <masahito@axsh.net> - 2.0.0-p353
- Update ruby version to 2.0.0-p353

* Tue Jul  2 2013 Masahito Yoshida <masahito@axsh.net> - 2.0.0-p247
- Update ruby version to 2.0.0-p247

* Sun May 19 2013 Masahito Yoshida <masahito@axsh.net> - 2.0.0-p195
- Update ruby version to 2.0.0-p195

* Sat Mar 23 2013 Masahito Yoshida <masahito@axsh.net> - 2.0.0-p0
- Update ruby version to 2.0.0-p0

* Sun Feb 24 2013 Masahito Yoshida <masahito@axsh.net> - 1.9.3-p392
- Update ruby version to 1.9.3-p392

* Tue Jan 29 2013 Carlos Villela <cv@lixo.org> - 1.9.3-p374
- Update ruby version to 1.9.3-p374

* Tue Jan 15 2013 Carlos Villela <cv@lixo.org> - 1.9.3-p362
- Update ruby version to 1.9.3-p362

* Thu Nov 15 2012 Rajat Vig <rajat.vig@gmail.com> - 1.9.3-p327
- Update ruby version to 1.9.3-p327

* Mon Oct 22 2012 Carlos Villela <cv@lixo.org> - 1.9.3-p286
- Update ruby version to 1.9.3-p286

* Wed Jul 4 2012 Carlos Villela <cv@lixo.org> - 1.9.3-p194
- Update ruby version to 1.9.3-p194

* Wed Jan 18 2012 Mandi Walls <mandi.walls@gmail.com> - 1.9.3-p0
- Update ruby version to 1.9.3-p0

* Mon Aug 29 2011 Gregory Graf <graf.gregory@gmail.com> - 1.9.2-p290
- Update ruby version to 1.9.2-p290

* Sat Jun 25 2011 Ian Meyer <ianmmeyer@gmail.com> - 1.9.2-p180-2
- Remove non-existant --sitearchdir and --vedorarchdir from %configure
- Replace --sitedir --vendordir with simpler --libdir
- Change %{_prefix}/share to %{_datadir}

* Tue Mar 7 2011 Robert Duncan <robert@robduncan.co.uk> - 1.9.2-p180-1
- Update prerequisites to include make
- Update ruby version to 1.9.2-p180
- Install /usr/share documentation
- (Hopefully!?) platform agnostic

* Sun Jan 2 2011 Ian Meyer <ianmmeyer@gmail.com> - 1.9.2-p136-1
- Initial spec to replace system ruby with 1.9.2-p136
