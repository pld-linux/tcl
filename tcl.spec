Summary:     Tool Command Language embeddable scripting language, with shared libraries
Summary(fr): Tool Command Language, langage de script avec bibliothèques partagées
Summary(tr): TCL ile kullanýlabilen betik dili
Name:        tcl
Version:     8.0p2
Release:     3
Source0:     ftp://ftp.scriptics.com/pub/tcl/tcl8_0/%{name}%{version}.tar.gz
Patch:       tcl-8.0-ieee.patch
Copyright:   BSD
URL:         http://www.scriptics.com/
Group:       Development/Languages/Tcl
Icon:        tcl.gif
Buildroot:   /tmp/%{name}-%{version}-root

%description
TCL is a simple scripting language that is designed to be embedded in
other applications. This package includes tclsh, a simple example of a
tcl application. TCL is very popular for writing small graphical applications
because of the TK widget set which is closely tied to it.

%description -l de
TCL ist eine einfache Skriptsprache, die zur Ingegration in andere 
Applikationen vorgesehen ist. Dieses Paket umfaßt tclsh, ein einfaches
Beispiel einer tcl-Applikation. TCL wird gern zum Schreiben kleiner 
grafischer Anwendungen benutzt, weil das TK-Widget-Set eng damit 
verknüpft ist. 

%description -l fr
TCL est un langage simple de script, conçu pour être intégré dans d'autres
applications. Ce paquetage contient tclsh, un exemple simple d'application
tcl. TCL est très utilisé pour écrire de petites applications graphiques
grâce à l'ensemble de widgets TK qui lui est très lié.

%description -l tr
TCL, baþka uygulamalarýn içine gömülmesi hedeflenerek geliþtirilmiþ basit
bir betimleme dilidir. Bu paket basit bir tcl uygulamasý örneði olan tclsh
kabuðunu içerir. TCL, kendisi ile sýkýca ilintili olan TK arayüz elemaný
kümesinin de desteðiyle küçük grafik uygulamalar yazma konusunda son derece
yaygýn kullanýlmaktadýr.

%package devel
Summary:     Tool Command Language header files and development documentation
Group:       Development/Languages/Tcl
Requires:    %{name} = %{version}

%description devel
Tool Command Language embeddable scripting language header files and
develppment documentation.

%prep
%setup -q -n %{name}8.0
%patch -p1
cd unix
autoconf

%build
cd unix
./configure --prefix=/usr --enable-shared --enable-gcc
make CFLAGS="$RPM_OPT_FLAGS -D_REENTRANT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr

cd unix
make INSTALL_ROOT=$RPM_BUILD_ROOT install
ln -sf libtcl8.0.so $RPM_BUILD_ROOT/usr/lib/libtcl.so
ln -sf tclsh8.0 $RPM_BUILD_ROOT/usr/bin/tclsh

install ../generic/{tclMath,tclInt}.h $RPM_BUILD_ROOT/usr/include

strip $RPM_BUILD_ROOT/usr/{bin/*,lib/lib*.so}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /usr/bin/*
%attr(644, root, root) /usr/man/man1/*
%attr(755, root, root) /usr/lib/lib*.so

%files devel
%defattr(644, root, root, 755)
/usr/include/*
/usr/lib/tclConfig.sh
%attr(644, root, root) /usr/man/man3/*
%attr(644, root, root) /usr/man/mann/*

%changelog
* Thu Sep  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [8.0pl2-3]
- added "Requires: %{name} = %%{version}" for devel,
- added tclInt.h to devel (required on compile expect).

* Mon Aug 24 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [8.0pl2-2]
- added tclMath.h to devel (required on compile tk).

* Sat Aug 22 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [8.0pl2-1]
- tcl is now separated source package from orher tcl/tk stuff,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- fixed using $RPM_OPT_FLAGS during compile (curren tcl configure script don't
  accept passing CFLAGS in enviroment variable),
- added striping shared libraries and tclsh binary,
- added devel subpackage,
- added URL,
- added package icon,
- updated Source Url to based on ftp://ftp.scriptics.com/,
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- fixed expect binaries exec permissions

* Thu Apr 09 1998 Erik Troan <ewt@redhat.com>
- updated to Tix 4.1.0.006
- updated version numbers of tcl/tk to relflect includsion of p2

* Wed Mar 25 1998 Cristian Gafton <gafton@redhat.com>
- updated tcl/tk to patch level 2
- updated tclX to 8.0.2

* Thu Oct 30 1997 Otto Hammersmith <otto@redhat.com>
- fixed filelist for tix... replacing path to the expect binary in scripts
  was leaving junk files around.

* Wed Oct 22 1997 Otto Hammersmith <otto@redhat.com>
- added patch to remove libieee test in configure.in for tcl and tk.
  Shoudln't be needed anymore for glibc systems, but this isn't the "proper" 
  solution for all systems
- fixed src urls

* Mon Oct 06 1997 Erik Troan <ewt@redhat.com>
- removed version numbers from descriptions

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- updated to tcl/tk 8.0 and related versions of packages

* Tue Jun 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- fixed dangling tclx/tkx symlinks
