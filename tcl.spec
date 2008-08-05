%define	major	8.4
Summary:	Tool Command Language embeddable scripting language, with shared libraries
Summary(fr.UTF-8):	Tool Command Language, langage de script avec bibliothèques partagées
Summary(pl.UTF-8):	Tool Command Language - język skryptowy z bibliotekami dynamicznymi
Summary(ru.UTF-8):	Tool Command Language - встраиваемый язык скриптов
Summary(tr.UTF-8):	Tcl ile kullanılabilen betik dili
Summary(uk.UTF-8):	Tool Command Language - вбудовувана мова скриптів
Name:		tcl
Version:	%{major}.19
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://dl.sourceforge.net/tcl/%{name}%{version}-src.tar.gz
# Source0-md5:	ade2c033a7b545ee108f3fdfeb629fcf
Source1:	%{name}-pl-man-pages.tar.bz2
# Source1-md5:	dd3370f2b588763758787831a4bf48fc
Patch0:		%{name}-glibc21.patch
Patch3:		%{name}-opt.patch
Patch4:		%{name}-ac25x.patch
Patch5:		%{name}-mannames.patch
Patch6:		%{name}-soname_fix.patch
Patch7:		%{name}-norpath.patch
URL:		http://www.tcl.tk/
BuildRequires:	autoconf
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 5.0
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

%description -l de.UTF-8
Tcl ist eine einfache Skriptsprache, die zur Ingegration in andere
Applikationen vorgesehen ist. Dieses Paket umfaßt tclsh, ein einfaches
Beispiel einer tcl-Applikation. Tcl wird gern zum Schreiben kleiner
grafischer Anwendungen benutzt, weil das Tk-Widget-Set eng damit
verknüpft ist.

%description -l fr.UTF-8
Tcl est un langage simple de script, conçu pour être intégré dans
d'autres applications. Ce paquetage contient tclsh, un exemple simple
d'application tcl. Tcl est très utilisé pour écrire de petites
applications graphiques grâce à l'ensemble de widgets Tk qui lui est
très lié.

%description -l ja.UTF-8
Tcl は他のアプリケーションに埋め込むためにデザインされた簡単なスクリプ
ト言語です。Tclはウィジッド・セットであるTkとともに用いるようにデザイン
しています。このパッケージにはTclの簡単な例として、tclsh
も含んでいます。

%description -l pl.UTF-8
Tcl jest prostym językiem skryptowym, przeznaczonym do współpracy z
innymi aplikacjami. W pakiecie znajduje się również tclsh - prosty
przykład programów. Tcl jest bardzo popularnym językiem do pisania
małych programów graficznych.

%description -l ru.UTF-8
Tcl - это простой интерпретируемый язык, предназначенный для
встраивания в другие программы. Этот пакет включает tclsh, простой
пример программы на tcl. Tcl очень популярен для написания небольших
графических программ из-за набора экранных примитивов Tk, который
очень тесно с ним связан.

%description -l tr.UTF-8
Tcl, başka uygulamaların içine gömülmesi hedeflenerek geliştirilmiş
basit bir betimleme dilidir. Bu paket basit bir Tcl uygulaması örneği
olan tclsh kabuğunu içerir. Tcl, kendisi ile sıkıca ilintili olan Tk
arayüz elemanı kümesinin de desteğiyle küçük grafik uygulamalar yazma
konusunda son derece yaygın kullanılmaktadır.

%description -l uk.UTF-8
Tcl - це проста інтерпретована мова, призначена для вбудови в інші
програми. Цей пакет містить також tclsh, простий приклад програми на
tcl. Tcl дуже популярний для написання простих графічних програм
завдяки набору екранних примітивів Tk, котрий з ним дуже тісно
зв'язаний.

%package devel
Summary:	Tool Command Language header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe oraz dokumentacja dla Tcl (Tool Command Language)
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}

%description devel
Tool Command Language embeddable scripting language header files and
develpment documentation.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz dokumentacja dla Tcl (Tool Command Language).

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
cd unix
sed -e "s/^CFLAGS_OPTIMIZE.*/CFLAGS_OPTIMIZE=%{rpmcflags} -D__NO_STRING_INLINES -D__NO_MATH_INLINES -D_REENTRANT/" \
	Makefile.in > Makefile.in.new
mv -f Makefile.in.new Makefile.in
%{__autoconf}
%configure \
	--enable-shared \
	--enable-threads \
	--enable-64bit \
	--enable-gcc
%{__make} \
	TCL_PACKAGE_PATH="%{_libdir} %{_libdir}/tcl%{major} %{_ulibdir} %{_ulibdir}/tcl%{major}"

sed -i -e "s#%{_builddir}/%{name}%{version}/unix#%{_libdir}#; \
	s#%{_builddir}/%{name}%{version}#%{_includedir}/tcl-private#" tclConfig.sh

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
