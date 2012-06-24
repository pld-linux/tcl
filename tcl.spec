Summary:	Tool Command Language embeddable scripting language, with shared libraries
Summary(fr):	Tool Command Language, langage de script avec biblioth�ques partag�es
Summary(pl):	Tool Command Language - j�zyk skryptowy z bibliotekami dynamicznymi
Summary(ru):	Tool Command Language - ������������ ���� ��������
Summary(tr):	TCL ile kullan�labilen betik dili
Summary(uk):	Tool Command Language - ����������� ���� �����Ԧ�
Name:		tcl
%define	major	8.4
Version:	%{major}.5
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcl/%{name}%{version}-src.tar.gz
# Source0-md5:	3fb354dba28166a1004f9103553a3974
Source1:	%{name}-pl-man-pages.tar.bz2
# Source1-md5:	dd3370f2b588763758787831a4bf48fc
Patch0:		%{name}-glibc21.patch
Patch1:		%{name}-64bit.patch
Patch2:		%{name}-readline.patch
Patch3:		%{name}-headers_fix.patch
Patch4:		%{name}-opt.patch
Patch5:		%{name}-ac25x.patch
Patch6:		%{name}-mannames.patch
Patch7:		%{name}-soname_fix.patch
Patch8:		%{name}-norpath.patch
Icon:		tcl.gif
URL:		http://www.tcl.tk/
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_ulibdir /usr/lib

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

%description -l ja
Tcl ��¾�Υ��ץꥱ�������������ि��˥ǥ����󤵤줿��ñ�ʥ������
�ȸ���Ǥ���Tcl�ϥ������åɡ����åȤǤ���Tk�ȤȤ���Ѥ���褦�˥ǥ�����
���Ƥ��ޤ������Υѥå������ˤ�Tcl�δ�ñ����Ȥ��ơ�tclsh
��ޤ�Ǥ��ޤ���

%description -l pl
TCL jest prostym j�zykiem skryptowym, przeznaczonym do wsp�pracy z
innymi aplikacjami. W pakiecie znajduje si� r�wnie� tclsh - prosty
przyk�ad program�w. TCL jest bardzo popularnym j�zykiem do pisania
ma�ych program�w graficznych.

%description -l ru
TCL - ��� ������� ���������������� ����, ��������������� ���
����������� � ������ ���������. ���� ����� �������� tclsh, �������
������ ��������� �� tcl. TCL ����� ��������� ��� ��������� ���������
����������� �������� ��-�� ������ �������� ���������� TK, �������
����� ����� � ��� ������.

%description -l tr
TCL, ba�ka uygulamalar�n i�ine g�m�lmesi hedeflenerek geli�tirilmi�
basit bir betimleme dilidir. Bu paket basit bir tcl uygulamas� �rne�i
olan tclsh kabu�unu i�erir. TCL, kendisi ile s�k�ca ilintili olan TK
aray�z eleman� k�mesinin de deste�iyle k���k grafik uygulamalar yazma
konusunda son derece yayg�n kullan�lmaktad�r.

%description -l uk
TCL - �� ������ �������������� ����, ���������� ��� ������� � ��ۦ
��������. ��� ����� ͦ����� ����� tclsh, ������� ������� �������� ��
tcl. TCL ���� ���������� ��� ��������� ������� ���Ʀ���� �������
������� ������ �������� ���ͦ��צ� TK, ������ � ��� ���� Ԧ���
��'������.

%package devel
Summary:	Tool Command Language header files and development documentation
Summary(pl):	Pliki nag��wkowe oraz dokumentacja dla tcl (Tool Command Language)
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}

%description devel
Tool Command Language embeddable scripting language header files and
develppment documentation.

%description devel -l pl
Pliki nag��wkowe oraz dokumentacja dla tcl (Tool Command Language).

%prep
%setup -q -n %{name}%{version}
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
sed -e "s/^CFLAGS_OPTIMIZE.*/CFLAGS_OPTIMIZE=%{rpmcflags} -D__NO_STRING_INLINES -D__NO_MATH_INLINES -D_REENTRANT/" \
	Makefile.in > Makefile.in.new
mv -f Makefile.in.new Makefile.in
%{__autoconf}
%configure \
	--enable-shared \
	--disable-threads \
	--enable-64bit \
	--enable-gcc
%{__make}

sed -e "s#%{_builddir}/%{name}%{version}/unix#%{_libdir}#; \
	s#%{_builddir}/%{name}%{version}#%{_includedir}#" tclConfig.sh > tclConfig.sh.new
mv -f tclConfig.sh.new tclConfig.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_mandir}/man1}

%{__make} -C unix install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT%{_mandir}

ln -sf libtcl%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtcl.so
ln -sf libtcl%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtcl%{major}.so
mv -f $RPM_BUILD_ROOT%{_bindir}/tclsh%{major} $RPM_BUILD_ROOT%{_bindir}/tclsh
mv $RPM_BUILD_ROOT%{_libdir}/tclConfig.sh $RPM_BUILD_ROOT%{_ulibdir}/tclConfig.sh

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_ulibdir}/tcl%{major}
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
