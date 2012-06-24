Summary:	Tool Command Language embeddable scripting language, with shared libraries
Summary(fr):	Tool Command Language, langage de script avec biblioth�ques partag�es
Summary(pl):	Tool Command Language - j�zyk skryptowy z bibliotekami dynamicznymi
Summary(ru):	Tool Command Language - ������������ ���� ��������
Summary(tr):	Tcl ile kullan�labilen betik dili
Summary(uk):	Tool Command Language - ����������� ���� �����Ԧ�
Name:		tcl
%define	major	8.5
Version:	%{major}
%define	rel	a3
Release:	0.%{rel}.2
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcl/%{name}%{version}%{rel}-src.tar.gz
# Source0-md5:	ff4a9fa2f0b23c139e78a7b33313954c
Source1:	%{name}-pl-man-pages.tar.bz2
# Source1-md5:	dd3370f2b588763758787831a4bf48fc
Patch0:		%{name}-glibc21.patch
Patch1:		%{name}-ieee.patch
Patch2:		%{name}-readline.patch
Patch4:		%{name}-opt.patch
Patch6:		%{name}-mannames.patch
Patch7:		%{name}-soname_fix.patch
Patch8:		%{name}-norpath.patch
Patch9:		%{name}-shell-quotes.patch
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
Applikationen vorgesehen ist. Dieses Paket umfa�t tclsh, ein einfaches
Beispiel einer tcl-Applikation. Tcl wird gern zum Schreiben kleiner
grafischer Anwendungen benutzt, weil das Tk-Widget-Set eng damit
verkn�pft ist.

%description -l fr
Tcl est un langage simple de script, con�u pour �tre int�gr� dans
d'autres applications. Ce paquetage contient tclsh, un exemple simple
d'application tcl. Tcl est tr�s utilis� pour �crire de petites
applications graphiques gr�ce � l'ensemble de widgets Tk qui lui est
tr�s li�.

%description -l ja
Tcl ��¾�Υ��ץꥱ�������������ि��˥ǥ����󤵤줿��ñ�ʥ������
�ȸ���Ǥ���Tcl�ϥ������åɡ����åȤǤ���Tk�ȤȤ���Ѥ���褦�˥ǥ�����
���Ƥ��ޤ������Υѥå������ˤ�Tcl�δ�ñ����Ȥ��ơ�tclsh
��ޤ�Ǥ��ޤ���

%description -l pl
Tcl jest prostym j�zykiem skryptowym, przeznaczonym do wsp�pracy z
innymi aplikacjami. W pakiecie znajduje si� r�wnie� tclsh - prosty
przyk�ad program�w. Tcl jest bardzo popularnym j�zykiem do pisania
ma�ych program�w graficznych.

%description -l ru
Tcl - ��� ������� ���������������� ����, ��������������� ���
����������� � ������ ���������. ���� ����� �������� tclsh, �������
������ ��������� �� tcl. Tcl ����� ��������� ��� ��������� ���������
����������� �������� ��-�� ������ �������� ���������� Tk, �������
����� ����� � ��� ������.

%description -l tr
Tcl, ba�ka uygulamalar�n i�ine g�m�lmesi hedeflenerek geli�tirilmi�
basit bir betimleme dilidir. Bu paket basit bir Tcl uygulamas� �rne�i
olan tclsh kabu�unu i�erir. Tcl, kendisi ile s�k�ca ilintili olan Tk
aray�z eleman� k�mesinin de deste�iyle k���k grafik uygulamalar yazma
konusunda son derece yayg�n kullan�lmaktad�r.

%description -l uk
Tcl - �� ������ �������������� ����, ���������� ��� ������� � ��ۦ
��������. ��� ����� ͦ����� ����� tclsh, ������� ������� �������� ��
tcl. Tcl ���� ���������� ��� ��������� ������� ���Ʀ���� �������
������� ������ �������� ���ͦ��צ� Tk, ������ � ��� ���� Ԧ���
��'������.

%package devel
Summary:	Tool Command Language header files and development documentation
Summary(pl):	Pliki nag��wkowe oraz dokumentacja dla Tcl (Tool Command Language)
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}

%description devel
Tool Command Language embeddable scripting language header files and
develpment documentation.

%description devel -l pl
Pliki nag��wkowe oraz dokumentacja dla Tcl (Tool Command Language).

%prep
%setup -q -n %{name}%{version}%{rel}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
cd unix
sed -i -e "s/^CFLAGS_OPTIMIZE.*/CFLAGS_OPTIMIZE=%{rpmcflags} -D__NO_STRING_INLINES -D__NO_MATH_INLINES -D_REENTRANT/" \
	Makefile.in
%{__autoconf}
%configure \
	--enable-langinfo \
	--enable-shared \
	--enable-threads \
	--enable-64bit \
	--enable-gcc
%{__make} \
	TCL_PACKAGE_PATH="%{_libdir} %{_libdir}/tcl%{major} %{_ulibdir} %{_ulibdir}/tcl%{major}"

sed -i -e "s#%{_builddir}/%{name}%{version}%{rel}/unix#%{_libdir}#; \
	s#%{_builddir}/%{name}%{version}%{rel}#%{_includedir}/tcl-private#" tclConfig.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_mandir}/man1}

%{__make} -C unix install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	TCL_PACKAGE_PATH="%{_libdir} %{_libdir}/tcl%{major} %{_ulibdir} %{_ulibdir}/tcl%{major}" \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT%{_mandir}

install -d $RPM_BUILD_ROOT%{_includedir}/%{name}-private/{generic,unix}
find generic unix -name "*.h" -exec cp -p '{}' $RPM_BUILD_ROOT%{_includedir}/%{name}-private/'{}' ';'
for h in $RPM_BUILD_ROOT%{_includedir}/*.h; do
	rh=$(basename "$h")
	if [ -f "$RPM_BUILD_ROOT%{_includedir}/%{name}-private/generic/$rh" ]; then
		ln -sf "../../$rh" $RPM_BUILD_ROOT%{_includedir}/%{name}-private/generic
	fi
done

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
