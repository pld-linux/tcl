Summary:	Tool Command Language embeddable scripting language, with shared libraries
Summary(fr):	Tool Command Language, langage de script avec biblioth�ques partag�es
Summary(pl):	Tool Command Language - j�zyk skryptowy z bibliotekami dynamicznymi
Summary(tr):	TCL ile kullan�labilen betik dili
Name:		tcl
Version:	8.0.5
Release:	37
License:	BSD
Group:		Development/Languages/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
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
Applikationen vorgesehen ist. Dieses Paket umfa�t tclsh, ein einfaches
Beispiel einer tcl-Applikation. TCL wird gern zum Schreiben kleiner
grafischer Anwendungen benutzt, weil das TK-Widget-Set eng damit
verkn�pft ist.

%description -l fr
TCL est un langage simple de script, con�u pour �tre int�gr� dans
d'autres applications. Ce paquetage contient tclsh, un exemple simple
d'application tcl. TCL est tr�s utilis� pour �crire de petites
applications graphiques gr�ce � l'ensemble de widgets TK qui lui est
tr�s li�.

%description -l pl 
TCL jest prostym j�zykiem skryptowym, przeznaczonym do wsp�pracy z
innymi aplikacjami. W pakiecie znajduje si� r�wnie� tclsh - prosty
przyk�ad program�w. TCL jest bardzo popularnym j�zykiem do pisania
ma�ych program�w graficzych.

%description -l tr
TCL, ba�ka uygulamalar�n i�ine g�m�lmesi hedeflenerek geli�tirilmi�
basit bir betimleme dilidir. Bu paket basit bir tcl uygulamas� �rne�i
olan tclsh kabu�unu i�erir. TCL, kendisi ile s�k�ca ilintili olan TK
aray�z eleman� k�mesinin de deste�iyle k���k grafik uygulamalar yazma
konusunda son derece yayg�n kullan�lmaktad�r.

%package devel
Summary:	Tool Command Language header files and development documentation
Summary(pl):	Pliki nag��wkowe oraz dokumentacja dla tcl (Tool Command Language)
Group:		Development/Languages/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Requires:	%{name} = %{version}

%description devel
Tool Command Language embeddable scripting language header files and
develppment documentation.

%description -l pl devel
Pliki nag��wkowe oraz dokumentacja dla tcl (Tool Command Language).

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
