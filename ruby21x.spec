%define rubyver         2.1.5

Name:           ruby
Version:        %{rubyver}
Release:        2%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       readline ncurses gdbm glibc openssl libyaml libffi zlib
BuildRequires:  readline-devel ncurses-devel gdbm-devel glibc-devel gcc openssl-devel make libyaml-devel libffi-devel zlib-devel
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/ruby-%{rubyver}.tar.gz
Summary:        An interpreter of object-oriented scripting language
Group:          Development/Languages
Provides: ruby(abi) = 2.1
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Provides: rubygems
Obsoletes: ruby
Obsoletes: ruby-libs
Obsoletes: ruby-irb
Obsoletes: ruby-rdoc
Obsoletes: ruby-devel
Obsoletes: rubygems

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
* Fri Nov 14 2014 Takashi Masuda <masutaka@feedforce.jp> - 2.1.5
- Update ruby version to 2.1.5
- Remove dependency unzip

* Wed Nov  5 2014 Takashi Masuda <masutaka@feedforce.jp> - 2.1.4-2
- Remove dependency db4 and db4-devel

* Fri Oct 31 2014 Takashi Masuda <masutaka@feedforce.jp> - 2.1.4
- Update ruby version to 2.1.4

* Wed Oct 29 2014 Takashi Masuda <masutaka@feedforce.jp> - 2.1.2
- Remove dependencies on tcl-devel and byacc

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
