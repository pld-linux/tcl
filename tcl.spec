Summary:	Tool Command Language embeddable scripting language, with shared libraries
Summary(fr):	Tool Command Language, langage de script avec bibliothХques partagИes
Summary(pl):	Tool Command Language - jЙzyk skryptowy z bibliotekami dynamicznymi
Summary(ru):	Tool Command Language - встраиваемый язык скриптов
Summary(tr):	Tcl ile kullanЩlabilen betik dili
Summary(uk):	Tool Command Language - вбудовувана мова скрипт╕в
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
Applikationen vorgesehen ist. Dieses Paket umfaъt tclsh, ein einfaches
Beispiel einer tcl-Applikation. Tcl wird gern zum Schreiben kleiner
grafischer Anwendungen benutzt, weil das Tk-Widget-Set eng damit
verknЭpft ist.

%description -l fr
Tcl est un langage simple de script, conГu pour Йtre intИgrИ dans
d'autres applications. Ce paquetage contient tclsh, un exemple simple
d'application tcl. Tcl est trХs utilisИ pour Иcrire de petites
applications graphiques grБce Ю l'ensemble de widgets Tk qui lui est
trХs liИ.

%description -l ja
Tcl ╓об╬╓н╔╒╔в╔Й╔╠║╪╔╥╔Г╔С╓ккД╓А╧Ч╓Ю╓©╓А╓к╔г╔╤╔╓╔С╓╣╓Л╓©╢йц╠╓й╔╧╔╞╔Й╔в
╔х╦ю╦Л╓г╓╧║ёTcl╓о╔╕╔ё╔╦╔ц╔и║╕╔╩╔ц╔х╓г╓╒╓КTk╓х╓х╓Б╓кмя╓╓╓К╓Х╓╕╓к╔г╔╤╔╓╔С
╓╥╓ф╓╓╓ч╓╧║ё╓Ё╓н╔я╔ц╔╠║╪╔╦╓к╓оTcl╓н╢йц╠╓йнЦ╓х╓╥╓ф║╒tclsh
╓Б╢ч╓С╓г╓╓╓ч╓╧║ё

%description -l pl
Tcl jest prostym jЙzykiem skryptowym, przeznaczonym do wspСЁpracy z
innymi aplikacjami. W pakiecie znajduje siЙ rСwnie© tclsh - prosty
przykЁad programСw. Tcl jest bardzo popularnym jЙzykiem do pisania
maЁych programСw graficznych.

%description -l ru
Tcl - это простой интерпретируемый язык, предназначенный для
встраивания в другие программы. Этот пакет включает tclsh, простой
пример программы на tcl. Tcl очень популярен для написания небольших
графических программ из-за набора экранных примитивов Tk, который
очень тесно с ним связан.

%description -l tr
Tcl, baЧka uygulamalarЩn iГine gЖmЭlmesi hedeflenerek geliЧtirilmiЧ
basit bir betimleme dilidir. Bu paket basit bir Tcl uygulamasЩ ЖrneПi
olan tclsh kabuПunu iГerir. Tcl, kendisi ile sЩkЩca ilintili olan Tk
arayЭz elemanЩ kЭmesinin de desteПiyle kЭГЭk grafik uygulamalar yazma
konusunda son derece yaygЩn kullanЩlmaktadЩr.

%description -l uk
Tcl - це проста ╕нтерпретована мова, призначена для вбудови в ╕нш╕
програми. Цей пакет м╕стить також tclsh, простий приклад програми на
tcl. Tcl дуже популярний для написання простих граф╕чних програм
завдяки набору екранних прим╕тив╕в Tk, котрий з ним дуже т╕сно
зв'язаний.

%package devel
Summary:	Tool Command Language header files and development documentation
Summary(pl):	Pliki nagЁСwkowe oraz dokumentacja dla Tcl (Tool Command Language)
Group:		Development/Languages/Tcl
Requires:	%{name} = %{version}-%{release}

%description devel
Tool Command Language embeddable scripting language header files and
develpment documentation.

%description devel -l pl
Pliki nagЁСwkowe oraz dokumentacja dla Tcl (Tool Command Language).

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
