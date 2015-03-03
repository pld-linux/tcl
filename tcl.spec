# TODO
# - why is tclConfig.sh in /usr/lib on lib64 platform?
#
# Conditional build:
%bcond_with	threads
%bcond_without	tests	# don't perform "make test"
#
%define		major	8.6
%define		minor	3
Summary:	Tool Command Language embeddable scripting language, with shared libraries
Summary(fr.UTF-8):	Tool Command Language, langage de script avec bibliothèques partagées
Summary(pl.UTF-8):	Tool Command Language - język skryptowy z bibliotekami dynamicznymi
Summary(ru.UTF-8):	Tool Command Language - встраиваемый язык скриптов
Summary(tr.UTF-8):	Tcl ile kullanılabilen betik dili
Summary(uk.UTF-8):	Tool Command Language - вбудовувана мова скриптів
Name:		tcl
Version:	%{major}.%{minor}
Release:	1
License:	BSD
Group:		Development/Languages/Tcl
Source0:	http://downloads.sourceforge.net/tcl/%{name}-core%{version}-src.tar.gz
# Source0-md5:	e7368802c8f75a86ef1e1b066cfec4c0
Source1:	%{name}-pl-man-pages.tar.bz2
# Source1-md5:	dd3370f2b588763758787831a4bf48fc
Patch0:		%{name}-ieee.patch

Patch2:		%{name}-opt.patch
Patch3:		%{name}-mannames.patch
Patch4:		%{name}-soname_fix.patch
Patch5:		%{name}-norpath.patch
Patch6:		%{name}-multilib.patch
Patch7:		%{name}-autopath.patch
Patch8:		%{name}-hidden.patch
Patch9:		%{name}-conf.patch
Patch10:	libc-version.patch
URL:		http://www.tcl.tk/
BuildRequires:	autoconf >= 2.59
BuildRequires:	ncurses-devel >= 5.2
Requires:	tzdata
Provides:	tcl(abi) = %{major}
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

%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
%if %{with threads}
# Make sure we have /proc mounted - otherwise pthread_getattr_np will fail
# https://sourceforge.net/tracker/index.php?func=detail&aid=1815573&group_id=10894&atid=110894
if [ ! -r /proc/self/maps ]; then
		echo "You need to have /proc mounted in order to build this package!"
		exit 1
fi
%endif

cd unix
%{__autoconf}
%configure \
	OPTFLAGS="%{rpmcflags} %{rpmcppflags}" \
	--enable-langinfo \
	--enable-shared \
	--%{?with_threads:en}%{!?with_threads:dis}able-threads \
	--enable-64bit \
	--without-tzdata
%{__make}

cp -a tclConfig.sh tclConfig.sh-orig
sed -i -e "s#%{_builddir}/%{name}%{version}/unix#%{_libdir}#; \
	s#%{_builddir}/%{name}%{version}#%{_includedir}/tcl-private#" tclConfig.sh
if cmp -s tclConfig.sh tclConfig.sh-orig; then
	echo "tclConfig.sh fix rule didn't change anything. Please verify it."
fi

%if %{with tests}
# tests that are problematic on builders; some probably could be fixed
rm ../tests/{http,httpold,socket,unixInit}.test
# problematic
rm ../tests/{clock,async}.test

%{__make} test 2>&1 | tee make-test.log
FAILED=$(grep 'Files with failing tests:' make-test.log | sed -e 's#Files with failing tests: ##g' | sort | xargs)
if [ -n "$FAILED" ]; then
	echo "Files with failing tests: $FAILED"
	exit 1
fi
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/tcl%{major},%{_prefix},%{_mandir}/man1}

%{__make} -C unix install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	MAN_INSTALL_DIR=$RPM_BUILD_ROOT%{_mandir}

# avoid Tcl_SetObjLength called with shared object error
# http://www.mail-archive.com/pld-devel-en@lists.pld-linux.org/msg05239.html
sed -i -e '/set auto_index(history)/s,^,#&,' $RPM_BUILD_ROOT%{_ulibdir}/tcl%{major}/tclIndex

install -d $RPM_BUILD_ROOT%{_includedir}/%{name}-private/{generic,unix}
find generic unix -name '*.h' -exec cp -p '{}' $RPM_BUILD_ROOT%{_includedir}/%{name}-private/'{}' ';'
for h in $RPM_BUILD_ROOT%{_includedir}/*.h; do
	rh=$(basename "$h")
	if [ -f "$RPM_BUILD_ROOT%{_includedir}/%{name}-private/generic/$rh" ]; then
		ln -sf "../../$rh" $RPM_BUILD_ROOT%{_includedir}/%{name}-private/generic
	fi
done

ln -sf libtcl%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtcl.so
ln -sf libtcl%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtcl%{major}.so
ln -sf libtcl%{major}.so.0.0 $RPM_BUILD_ROOT%{_libdir}/libtcl%{major}.so.0
mv -f $RPM_BUILD_ROOT%{_bindir}/tclsh%{major} $RPM_BUILD_ROOT%{_bindir}/tclsh

%{?have_ulibdir:mv $RPM_BUILD_ROOT%{_libdir}/tclConfig.sh $RPM_BUILD_ROOT%{_ulibdir}/tclConfig.sh}
%{?have_ulibdir:mv $RPM_BUILD_ROOT%{_libdir}/tclooConfig.sh $RPM_BUILD_ROOT%{_ulibdir}/tclooConfig.sh}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

install -d $RPM_BUILD_ROOT%{_libdir}/tcl%{major}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libtcl%{major}.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libtcl%{major}.so.0
%{?have_ulibdir:%dir %{_libdir}/tcl%{major}}
%dir %{_datadir}/tcl%{major}
%{_ulibdir}/tcl[0-9]
%dir %{_ulibdir}/tcl%{major}
%{_ulibdir}/tcl%{major}/*.tcl
%{_ulibdir}/tcl%{major}/encoding
%{_ulibdir}/tcl%{major}/http1.0
%{_ulibdir}/tcl%{major}/opt0.4
%{_ulibdir}/tcl%{major}/tclIndex

%dir %{_ulibdir}/tcl%{major}/msgs
%lang(af) %{_ulibdir}/tcl%{major}/msgs/af.msg
%lang(af_ZA) %{_ulibdir}/tcl%{major}/msgs/af_za.msg
%lang(ar) %{_ulibdir}/tcl%{major}/msgs/ar.msg
%lang(ar_IN) %{_ulibdir}/tcl%{major}/msgs/ar_in.msg
%lang(ar_JO) %{_ulibdir}/tcl%{major}/msgs/ar_jo.msg
%lang(ar_LB) %{_ulibdir}/tcl%{major}/msgs/ar_lb.msg
%lang(ar_SY) %{_ulibdir}/tcl%{major}/msgs/ar_sy.msg
%lang(be) %{_ulibdir}/tcl%{major}/msgs/be.msg
%lang(bg) %{_ulibdir}/tcl%{major}/msgs/bg.msg
%lang(bn) %{_ulibdir}/tcl%{major}/msgs/bn.msg
%lang(bn_IN) %{_ulibdir}/tcl%{major}/msgs/bn_in.msg
%lang(ca) %{_ulibdir}/tcl%{major}/msgs/ca.msg
%lang(cs) %{_ulibdir}/tcl%{major}/msgs/cs.msg
%lang(da) %{_ulibdir}/tcl%{major}/msgs/da.msg
%lang(de) %{_ulibdir}/tcl%{major}/msgs/de.msg
%lang(de_AT) %{_ulibdir}/tcl%{major}/msgs/de_at.msg
%lang(de_BE) %{_ulibdir}/tcl%{major}/msgs/de_be.msg
%lang(el) %{_ulibdir}/tcl%{major}/msgs/el.msg
%lang(en_AU) %{_ulibdir}/tcl%{major}/msgs/en_au.msg
%lang(en_BE) %{_ulibdir}/tcl%{major}/msgs/en_be.msg
%lang(en_BW) %{_ulibdir}/tcl%{major}/msgs/en_bw.msg
%lang(en_CA) %{_ulibdir}/tcl%{major}/msgs/en_ca.msg
%lang(en_GB) %{_ulibdir}/tcl%{major}/msgs/en_gb.msg
%lang(en_HK) %{_ulibdir}/tcl%{major}/msgs/en_hk.msg
%lang(en_IE) %{_ulibdir}/tcl%{major}/msgs/en_ie.msg
%lang(en_IN) %{_ulibdir}/tcl%{major}/msgs/en_in.msg
%lang(en_NZ) %{_ulibdir}/tcl%{major}/msgs/en_nz.msg
%lang(en_PH) %{_ulibdir}/tcl%{major}/msgs/en_ph.msg
%lang(en_SG) %{_ulibdir}/tcl%{major}/msgs/en_sg.msg
%lang(en_ZA) %{_ulibdir}/tcl%{major}/msgs/en_za.msg
%lang(en_ZW) %{_ulibdir}/tcl%{major}/msgs/en_zw.msg
%lang(eo) %{_ulibdir}/tcl%{major}/msgs/eo.msg
%lang(es) %{_ulibdir}/tcl%{major}/msgs/es.msg
%lang(es_AR) %{_ulibdir}/tcl%{major}/msgs/es_ar.msg
%lang(es_BO) %{_ulibdir}/tcl%{major}/msgs/es_bo.msg
%lang(es_CL) %{_ulibdir}/tcl%{major}/msgs/es_cl.msg
%lang(es_CO) %{_ulibdir}/tcl%{major}/msgs/es_co.msg
%lang(es_CR) %{_ulibdir}/tcl%{major}/msgs/es_cr.msg
%lang(es_DO) %{_ulibdir}/tcl%{major}/msgs/es_do.msg
%lang(es_EC) %{_ulibdir}/tcl%{major}/msgs/es_ec.msg
%lang(es_GT) %{_ulibdir}/tcl%{major}/msgs/es_gt.msg
%lang(es_HN) %{_ulibdir}/tcl%{major}/msgs/es_hn.msg
%lang(es_MX) %{_ulibdir}/tcl%{major}/msgs/es_mx.msg
%lang(es_NI) %{_ulibdir}/tcl%{major}/msgs/es_ni.msg
%lang(es_PA) %{_ulibdir}/tcl%{major}/msgs/es_pa.msg
%lang(es_PE) %{_ulibdir}/tcl%{major}/msgs/es_pe.msg
%lang(es_PR) %{_ulibdir}/tcl%{major}/msgs/es_pr.msg
%lang(es_PY) %{_ulibdir}/tcl%{major}/msgs/es_py.msg
%lang(es_SV) %{_ulibdir}/tcl%{major}/msgs/es_sv.msg
%lang(es_UY) %{_ulibdir}/tcl%{major}/msgs/es_uy.msg
%lang(es_VE) %{_ulibdir}/tcl%{major}/msgs/es_ve.msg
%lang(et) %{_ulibdir}/tcl%{major}/msgs/et.msg
%lang(eu) %{_ulibdir}/tcl%{major}/msgs/eu.msg
%lang(eu_ES) %{_ulibdir}/tcl%{major}/msgs/eu_es.msg
%lang(fa) %{_ulibdir}/tcl%{major}/msgs/fa.msg
%lang(fa_IN) %{_ulibdir}/tcl%{major}/msgs/fa_in.msg
%lang(fa_IR) %{_ulibdir}/tcl%{major}/msgs/fa_ir.msg
%lang(fi) %{_ulibdir}/tcl%{major}/msgs/fi.msg
%lang(fo) %{_ulibdir}/tcl%{major}/msgs/fo.msg
%lang(fo_FO) %{_ulibdir}/tcl%{major}/msgs/fo_fo.msg
%lang(fr) %{_ulibdir}/tcl%{major}/msgs/fr.msg
%lang(fr_BE) %{_ulibdir}/tcl%{major}/msgs/fr_be.msg
%lang(fr_CA) %{_ulibdir}/tcl%{major}/msgs/fr_ca.msg
%lang(fr_CH) %{_ulibdir}/tcl%{major}/msgs/fr_ch.msg
%lang(ga) %{_ulibdir}/tcl%{major}/msgs/ga.msg
%lang(ga_IE) %{_ulibdir}/tcl%{major}/msgs/ga_ie.msg
%lang(gl) %{_ulibdir}/tcl%{major}/msgs/gl.msg
%lang(gl_ES) %{_ulibdir}/tcl%{major}/msgs/gl_es.msg
%lang(gv) %{_ulibdir}/tcl%{major}/msgs/gv.msg
%lang(gv_GB) %{_ulibdir}/tcl%{major}/msgs/gv_gb.msg
%lang(he) %{_ulibdir}/tcl%{major}/msgs/he.msg
%lang(hi) %{_ulibdir}/tcl%{major}/msgs/hi.msg
%lang(hi_IN) %{_ulibdir}/tcl%{major}/msgs/hi_in.msg
%lang(hr) %{_ulibdir}/tcl%{major}/msgs/hr.msg
%lang(hu) %{_ulibdir}/tcl%{major}/msgs/hu.msg
%lang(id) %{_ulibdir}/tcl%{major}/msgs/id.msg
%lang(id_ID) %{_ulibdir}/tcl%{major}/msgs/id_id.msg
%lang(is) %{_ulibdir}/tcl%{major}/msgs/is.msg
%lang(it) %{_ulibdir}/tcl%{major}/msgs/it.msg
%lang(it_CH) %{_ulibdir}/tcl%{major}/msgs/it_ch.msg
%lang(ja) %{_ulibdir}/tcl%{major}/msgs/ja.msg
%lang(kl) %{_ulibdir}/tcl%{major}/msgs/kl.msg
%lang(kl_GL) %{_ulibdir}/tcl%{major}/msgs/kl_gl.msg
%lang(ko) %{_ulibdir}/tcl%{major}/msgs/ko.msg
%lang(ko) %{_ulibdir}/tcl%{major}/msgs/ko_kr.msg
%lang(kok) %{_ulibdir}/tcl%{major}/msgs/kok.msg
%lang(kok_IN) %{_ulibdir}/tcl%{major}/msgs/kok_in.msg
%lang(kw) %{_ulibdir}/tcl%{major}/msgs/kw.msg
%lang(kw_GB) %{_ulibdir}/tcl%{major}/msgs/kw_gb.msg
%lang(lt) %{_ulibdir}/tcl%{major}/msgs/lt.msg
%lang(lv) %{_ulibdir}/tcl%{major}/msgs/lv.msg
%lang(mk) %{_ulibdir}/tcl%{major}/msgs/mk.msg
%lang(mr) %{_ulibdir}/tcl%{major}/msgs/mr.msg
%lang(mr_IN) %{_ulibdir}/tcl%{major}/msgs/mr_in.msg
%lang(ms) %{_ulibdir}/tcl%{major}/msgs/ms.msg
%lang(ms_MY) %{_ulibdir}/tcl%{major}/msgs/ms_my.msg
%lang(mt) %{_ulibdir}/tcl%{major}/msgs/mt.msg
%lang(nb) %{_ulibdir}/tcl%{major}/msgs/nb.msg
%lang(nl) %{_ulibdir}/tcl%{major}/msgs/nl.msg
%lang(nl_BE) %{_ulibdir}/tcl%{major}/msgs/nl_be.msg
%lang(nn) %{_ulibdir}/tcl%{major}/msgs/nn.msg
%lang(pl) %{_ulibdir}/tcl%{major}/msgs/pl.msg
%lang(pt) %{_ulibdir}/tcl%{major}/msgs/pt.msg
%lang(pt_BR) %{_ulibdir}/tcl%{major}/msgs/pt_br.msg
%lang(ro) %{_ulibdir}/tcl%{major}/msgs/ro.msg
%lang(ru) %{_ulibdir}/tcl%{major}/msgs/ru.msg
%lang(ru_UA) %{_ulibdir}/tcl%{major}/msgs/ru_ua.msg
%lang(sh) %{_ulibdir}/tcl%{major}/msgs/sh.msg
%lang(sk) %{_ulibdir}/tcl%{major}/msgs/sk.msg
%lang(sl) %{_ulibdir}/tcl%{major}/msgs/sl.msg
%lang(sq) %{_ulibdir}/tcl%{major}/msgs/sq.msg
%lang(sr) %{_ulibdir}/tcl%{major}/msgs/sr.msg
%lang(sv) %{_ulibdir}/tcl%{major}/msgs/sv.msg
%lang(sw) %{_ulibdir}/tcl%{major}/msgs/sw.msg
%lang(ta) %{_ulibdir}/tcl%{major}/msgs/ta.msg
%lang(ta_IN) %{_ulibdir}/tcl%{major}/msgs/ta_in.msg
%lang(te) %{_ulibdir}/tcl%{major}/msgs/te.msg
%lang(te_IN) %{_ulibdir}/tcl%{major}/msgs/te_in.msg
%lang(th) %{_ulibdir}/tcl%{major}/msgs/th.msg
%lang(tr) %{_ulibdir}/tcl%{major}/msgs/tr.msg
%lang(uk) %{_ulibdir}/tcl%{major}/msgs/uk.msg
%lang(vi) %{_ulibdir}/tcl%{major}/msgs/vi.msg
%lang(zh) %{_ulibdir}/tcl%{major}/msgs/zh.msg
%lang(zh_CN) %{_ulibdir}/tcl%{major}/msgs/zh_cn.msg
%lang(zh_HK) %{_ulibdir}/tcl%{major}/msgs/zh_hk.msg
%lang(zh_SG) %{_ulibdir}/tcl%{major}/msgs/zh_sg.msg
%lang(zh_TW) %{_ulibdir}/tcl%{major}/msgs/zh_tw.msg

%{_mandir}/man1/tclsh.1*
%lang(pl) %{_mandir}/pl/man1/tclsh.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_ulibdir}/tclConfig.sh
%attr(755,root,root) %{_ulibdir}/tclooConfig.sh
%{_ulibdir}/tcl%{major}/tclAppInit.c
%attr(755,root,root) %{_libdir}/libtcl%{major}.so
%attr(755,root,root) %{_libdir}/libtcl.so
%{_libdir}/libtclstub%{major}.a
%{_includedir}/tcl*.h
%{_includedir}/tcl-private
%{_pkgconfigdir}/tcl.pc
%{_mandir}/man3/TCL_*.3*
%{_mandir}/man3/Tcl_*.3*
%{_mandir}/man3/attemptck*alloc.3*
%{_mandir}/man3/ck*.3*
%{_mandir}/mann/*.n*
%lang(pl) %{_mandir}/pl/mann/*.n*
