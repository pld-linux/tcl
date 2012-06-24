Summary:	Tool Command Language embeddable scripting language, with shared libraries
Summary(fr):	Tool Command Language, langage de script avec biblioth�ques partag�es
Summary(pl):	Tool Command Language - j�zyk skryptowy z bibliotekami dynamicznymi
Summary(tr):	TCL ile kullan�labilen betik dili
Name:		tcl
Version:	8.0.5
Release:	2
Group:		Development/Languages/Tcl
Group(pl):	Programowanie/J�zyki/Tcl
Copyright:	BSD
Source0:	ftp://ftp.scriptics.com/pub/tcl/tcl8_0/%{name}%{version}.tar.gz
Patch0:		tcl-ieee.patch
Patch1:		tcl-glibc21.patch
Patch2:		tcl-tmpfix.patch
Patch3:		tcl-manlnk.patch
Patch4:		tcl-64bit.patch
Patch5:		tcl-readline.patch
Icon:		tcl.gif
URL:		http://www.scriptics.com/
BuildPrereq:	ncurses-devel
BuildPrereq:	readline-devel
Buildroot:	/tmp/%{name}-%{version}-root

%description
TCL is a simple scripting language that is designed to be embedded in
other applications. This package includes tclsh, a simple example of a
tcl application. TCL is very popular for writing small graphical applications
because of the TK widget set which is closely tied to it.

%description -l de
TCL ist eine einfache Skriptsprache, die zur Ingegration in andere 
Applikationen vorgesehen ist. Dieses Paket umfa�t tclsh, ein einfaches
Beispiel einer tcl-Applikation. TCL wird gern zum Schreiben kleiner 
grafischer Anwendungen benutzt, weil das TK-Widget-Set eng damit 
verkn�pft ist. 

%description -l fr
TCL est un langage simple de script, con�u pour �tre int�gr� dans d'autres
applications. Ce paquetage contient tclsh, un exemple simple d'application
tcl. TCL est tr�s utilis� pour �crire de petites applications graphiques
gr�ce � l'ensemble de widgets TK qui lui est tr�s li�.

%description -l pl 
TCL jest prostym j�zykiem skryptowym, przeznaczonym do wsp�pracy z innymi
aplikacjami. W pakiecie znajduje si� r�wnie� tclsh - prosty przyk�ad program�w.
TCL jest bardzo popularnym j�zykiem do pisania ma�ych program�w graficzych.

%description -l tr
TCL, ba�ka uygulamalar�n i�ine g�m�lmesi hedeflenerek geli�tirilmi� basit
bir betimleme dilidir. Bu paket basit bir tcl uygulamas� �rne�i olan tclsh
kabu�unu i�erir. TCL, kendisi ile s�k�ca ilintili olan TK aray�z eleman�
k�mesinin de deste�iyle k���k grafik uygulamalar yazma konusunda son derece
yayg�n kullan�lmaktad�r.

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
Pliki nag��wkowe oraz dokumentacja dla tcl (Tool Command Language) 

%prep
%setup  -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
cd unix
autoconf
CFLAGS="$RPM_OPT_FLAGS -D_REENTRANT" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=%{_prefix} \
	--enable-shared \
	--enable-gcc
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr

cd unix
make install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT%{_mandir}

ln -sf libtcl8.0.so $RPM_BUILD_ROOT%{_libdir}/libtcl.so
ln -sf tclsh8.0 $RPM_BUILD_ROOT%{_bindir}/tclsh

install ../generic/{tclMath,tclInt}.h $RPM_BUILD_ROOT%{_includedir}

strip $RPM_BUILD_ROOT{%{_bindir}/*,%{_libdir}/libtcl8*.so}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man?/* \

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/tcl*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/tclConfig.sh
%{_includedir}/*
%{_mandir}/man[3n]/*

%changelog
* Sun May 30 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [8.0.5-2]
- based on RH spec,
- added patches:
-- tcl-glibc21.patch - fiix problems on glibc 2.1 (RH 6.0),
-- tcl-tmpfix.patch - fix tmp race (from Debian),
-- tcl-manlnk.patch - make some ,man pages as *roff include,
-- tcl-64bit.patch - fix problems on 64-bit architectures,
-- tcl-readline.patch -- add ability to use readline in tclsh,
- spec rewrited by PLD team.
