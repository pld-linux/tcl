Summary:	Tool Command Language embeddable scripting language, with shared libraries
Summary(fr):	Tool Command Language, langage de script avec bibliothèques partagées
Summary(pl):	Tool Command Language - jêzyk skryptowy z bibliotekami dynamicznymi
Summary(ru):	Tool Command Language - ×ÓÔÒÁÉ×ÁÅÍÙÊ ÑÚÙË ÓËÒÉÐÔÏ×
Summary(tr):	Tcl ile kullanýlabilen betik dili
Summary(uk):	Tool Command Language - ×ÂÕÄÏ×Õ×ÁÎÁ ÍÏ×Á ÓËÒÉÐÔ¦×
Name:		tcl
%define	major	8.5
Version:	%{major}
%define	rel	a2
Release:	0.%{rel}.2
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcl/%{name}%{version}%{rel}-src.tar.gz
# Source0-md5:	95c9d614538a9918f51e948386702bb4
Source1:	%{name}-pl-man-pages.tar.bz2
# Source1-md5:	dd3370f2b588763758787831a4bf48fc
Patch0:		%{name}-glibc21.patch
Patch1:		%{name}-64bit.patch
Patch2:		%{name}-readline.patch
Patch3:		%{name}-headers_fix.patch
Patch4:		%{name}-opt.patch
Patch6:		%{name}-mannames.patch
Patch7:		%{name}-soname_fix.patch
Patch8:		%{name}-norpath.patch
Icon:		tcl.gif
URL:		http://www.tcl.tk/
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ulibdir	/usr/lib

%if "%{_libdir}" != "%{_ulibdir}"
%define		have_ulibdir	1
%endif

%description
Tcl is a simple scripting language that is designed to be embedded in
other applications. This package includes tclsh, a simple example of a
tcl application. Tcl is very popular for writing small graphical
applications because of the Tk widget set which is closely tied to it.

%description -l de
Tcl ist eine einfache Skriptsprache, die zur Ingegration in andere
Applikationen vorgesehen ist. Dieses Paket umfaßt tclsh, ein einfaches
Beispiel einer tcl-Applikation. Tcl wird gern zum Schreiben kleiner
grafischer Anwendungen benutzt, weil das Tk-Widget-Set eng damit
verknüpft ist.

%description -l fr
Tcl est un langage simple de script, conçu pour être intégré dans
d'autres applications. Ce paquetage contient tclsh, un exemple simple
d'application tcl. Tcl est très utilisé pour écrire de petites
applications graphiques grâce à l'ensemble de widgets Tk qui lui est
très lié.

%description -l ja
Tcl ¤ÏÂ¾¤Î¥¢¥×¥ê¥±¡¼¥·¥ç¥ó¤ËËä¤á¹þ¤à¤¿¤á¤Ë¥Ç¥¶¥¤¥ó¤µ¤ì¤¿´ÊÃ±¤Ê¥¹¥¯¥ê¥×
¥È¸À¸ì¤Ç¤¹¡£Tcl¤Ï¥¦¥£¥¸¥Ã¥É¡¦¥»¥Ã¥È¤Ç¤¢¤ëTk¤È¤È¤â¤ËÍÑ¤¤¤ë¤è¤¦¤Ë¥Ç¥¶¥¤¥ó
¤·¤Æ¤¤¤Þ¤¹¡£¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤Ë¤ÏTcl¤Î´ÊÃ±¤ÊÎã¤È¤·¤Æ¡¢tclsh
¤â´Þ¤ó¤Ç¤¤¤Þ¤¹¡£

%description -l pl
Tcl jest prostym jêzykiem skryptowym, przeznaczonym do wspó³pracy z
innymi aplikacjami. W pakiecie znajduje siê równie¿ tclsh - prosty
przyk³ad programów. Tcl jest bardzo popularnym jêzykiem do pisania
ma³ych programów graficznych.

%description -l ru
Tcl - ÜÔÏ ÐÒÏÓÔÏÊ ÉÎÔÅÒÐÒÅÔÉÒÕÅÍÙÊ ÑÚÙË, ÐÒÅÄÎÁÚÎÁÞÅÎÎÙÊ ÄÌÑ
×ÓÔÒÁÉ×ÁÎÉÑ × ÄÒÕÇÉÅ ÐÒÏÇÒÁÍÍÙ. üÔÏÔ ÐÁËÅÔ ×ËÌÀÞÁÅÔ tclsh, ÐÒÏÓÔÏÊ
ÐÒÉÍÅÒ ÐÒÏÇÒÁÍÍÙ ÎÁ tcl. Tcl ÏÞÅÎØ ÐÏÐÕÌÑÒÅÎ ÄÌÑ ÎÁÐÉÓÁÎÉÑ ÎÅÂÏÌØÛÉÈ
ÇÒÁÆÉÞÅÓËÉÈ ÐÒÏÇÒÁÍÍ ÉÚ-ÚÁ ÎÁÂÏÒÁ ÜËÒÁÎÎÙÈ ÐÒÉÍÉÔÉ×Ï× Tk, ËÏÔÏÒÙÊ
ÏÞÅÎØ ÔÅÓÎÏ Ó ÎÉÍ Ó×ÑÚÁÎ.

%description -l tr
Tcl, baþka uygulamalarýn içine gömülmesi hedeflenerek geliþtirilmiþ
basit bir betimleme dilidir. Bu paket basit bir Tcl uygulamasý örneði
olan tclsh kabuðunu içerir. Tcl, kendisi ile sýkýca ilintili olan Tk
arayüz elemaný kümesinin de desteðiyle küçük grafik uygulamalar yazma
konusunda son derece yaygýn kullanýlmaktadýr.

%description -l uk
Tcl - ÃÅ ÐÒÏÓÔÁ ¦ÎÔÅÒÐÒÅÔÏ×ÁÎÁ ÍÏ×Á, ÐÒÉÚÎÁÞÅÎÁ ÄÌÑ ×ÂÕÄÏ×É × ¦ÎÛ¦
ÐÒÏÇÒÁÍÉ. ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÔÁËÏÖ tclsh, ÐÒÏÓÔÉÊ ÐÒÉËÌÁÄ ÐÒÏÇÒÁÍÉ ÎÁ
tcl. Tcl ÄÕÖÅ ÐÏÐÕÌÑÒÎÉÊ ÄÌÑ ÎÁÐÉÓÁÎÎÑ ÐÒÏÓÔÉÈ ÇÒÁÆ¦ÞÎÉÈ ÐÒÏÇÒÁÍ
ÚÁ×ÄÑËÉ ÎÁÂÏÒÕ ÅËÒÁÎÎÉÈ ÐÒÉÍ¦ÔÉ×¦× Tk, ËÏÔÒÉÊ Ú ÎÉÍ ÄÕÖÅ Ô¦ÓÎÏ
Ú×'ÑÚÁÎÉÊ.

%package devel
Summary:	Tool Command Language header files and development documentation
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja dla Tcl (Tool Command Language)
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}

%description devel
Tool Command Language embeddable scripting language header files and
develpment documentation.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja dla Tcl (Tool Command Language).

%prep
%setup -q -n %{name}%{version}%{rel}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
cd unix
sed -e "s/^CFLAGS_OPTIMIZE.*/CFLAGS_OPTIMIZE=%{rpmcflags} -D__NO_STRING_INLINES -D__NO_MATH_INLINES -D_REENTRANT/" \
	Makefile.in > Makefile.in.new
mv -f Makefile.in.new Makefile.in
%{__autoconf}
%configure \
	--enable-langinfo \
	--enable-shared \
	--enable-threads \
	--enable-64bit \
	--enable-gcc
%{__make} \
	TCL_PACKAGE_PATH="%{_libdir} %{_libdir}/tcl%{major} %{_ulibdir} %{_ulibdir}/tcl%{major}"

sed -e "s#%{_builddir}/%{name}%{version}/unix#%{_libdir}#; \
	s#%{_builddir}/%{name}%{version}#%{_includedir}#" tclConfig.sh > tclConfig.sh.new
mv -f tclConfig.sh.new tclConfig.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_mandir}/man1}

%{__make} -C unix install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	TCL_PACKAGE_PATH="%{_libdir} %{_libdir}/tcl%{major} %{_ulibdir} %{_ulibdir}/tcl%{major}" \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT%{_mandir}

ln -sf libtcl%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtcl.so
ln -sf libtcl%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtcl%{major}.so
mv -f $RPM_BUILD_ROOT%{_bindir}/tclsh%{major} $RPM_BUILD_ROOT%{_bindir}/tclsh

%{?have_ulibdir:mv $RPM_BUILD_ROOT%{_libdir}/tclConfig.sh $RPM_BUILD_ROOT%{_ulibdir}/tclConfig.sh}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

install -d $RPM_BUILD_ROOT%{_libdir}/tcl%{major}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_ulibdir}/tcl[0-9]
%{_libdir}/tcl%{major}
%{?have_ulibdir:%{_ulibdir}/tcl%{major}}
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/tclConfig.sh
%{_libdir}/libtclstub%{major}.a
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man[3n]/*
%lang(pl) %{_mandir}/pl/mann/*
