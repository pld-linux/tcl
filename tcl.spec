Summary:	Tool Command Language embeddable scripting language, with shared libraries
Summary(fr):	Tool Command Language, langage de script avec bibliothèques partagées
Summary(pl):	Tool Command Language - jêzyk skryptowy z bibliotekami dynamicznymi
Summary(tr):	TCL ile kullanýlabilen betik dili
Name:		tcl
Version:	8.0.5
Release:	37
License:	BSD
Group:		Development/Languages/Tcl
Group(pl):	Programowanie/Jêzyki/Tcl
Source0:	ftp://ftp.scriptics.com/pub/tcl/tcl8_0/%{name}%{version}.tar.gz
Patch0:		tcl-ieee.patch
Patch1:		tcl-glibc21.patch
Patch2:		tcl-tmpfix.patch
Patch3:		tcl-manlnk.patch
Patch4:		tcl-64bit.patch
Patch5:		tcl-readline.patch
Patch6:		tcl-headers_fix.patch
Patch7:		tcl-sigpwr.patch
Patch8:		tcl-autoconf.patch
Icon:		tcl.gif
URL:		http://www.scriptics.com/
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TCL is a simple scripting language that is designed to be embedded in
other applications. This package includes tclsh, a simple example of a
tcl application. TCL is very popular for writing small graphical
applications because of the TK widget set which is closely tied to it.

%description -l de
TCL ist eine einfache Skriptsprache, die zur Ingegration in andere
Applikationen vorgesehen ist. Dieses Paket umfaßt tclsh, ein einfaches
Beispiel einer tcl-Applikation. TCL wird gern zum Schreiben kleiner
grafischer Anwendungen benutzt, weil das TK-Widget-Set eng damit
verknüpft ist.

%description -l fr
TCL est un langage simple de script, conçu pour être intégré dans
d'autres applications. Ce paquetage contient tclsh, un exemple simple
d'application tcl. TCL est très utilisé pour écrire de petites
applications graphiques grâce à l'ensemble de widgets TK qui lui est
très lié.

%description -l pl 
TCL jest prostym jêzykiem skryptowym, przeznaczonym do wspó³pracy z
innymi aplikacjami. W pakiecie znajduje siê równie¿ tclsh - prosty
przyk³ad programów. TCL jest bardzo popularnym jêzykiem do pisania
ma³ych programów graficzych.

%description -l tr
TCL, baþka uygulamalarýn içine gömülmesi hedeflenerek geliþtirilmiþ
basit bir betimleme dilidir. Bu paket basit bir tcl uygulamasý örneði
olan tclsh kabuðunu içerir. TCL, kendisi ile sýkýca ilintili olan TK
arayüz elemaný kümesinin de desteðiyle küçük grafik uygulamalar yazma
konusunda son derece yaygýn kullanýlmaktadýr.

%package devel
Summary:	Tool Command Language header files and development documentation
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja dla tcl (Tool Command Language)
Group:		Development/Languages/Tcl
Group(pl):	Programowanie/Jêzyki/Tcl
Requires:	%{name} = %{version}

%description devel
Tool Command Language embeddable scripting language header files and
develppment documentation.

%description -l pl devel
Pliki nag³ówkowe oraz dokumentacja dla tcl (Tool Command Language).

%prep
%setup  -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
cd unix
sed -e "s/^CFLAGS_OPTIMIZE=.*/CFLAGS_OPTIMIZE=\'%{optflags} -D_REENTRANT\'/" \
	configure.in > configure.in.new
mv -f configure.in.new configure.in
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-shared \
	--enable-gcc
%{__make}

sed -e "s#%{_builddir}/%{name}%{version}/unix#%{_libdir}#; \
	s#%{_builddir}/%{name}%{version}#%{_includedir}#" tclConfig.sh > tclConfig.sh.new
mv -f tclConfig.sh.new tclConfig.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

cd unix
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT%{_mandir}

ln -sf libtcl8.0.so $RPM_BUILD_ROOT%{_libdir}/libtcl.so
ln -sf tclsh8.0 $RPM_BUILD_ROOT%{_bindir}/tclsh

strip $RPM_BUILD_ROOT%{_bindir}/*
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man?/*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/tcl8.0
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/tclConfig.sh
%{_includedir}/*
%{_mandir}/man[3n]/*
