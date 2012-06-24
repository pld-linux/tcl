'\"
'\" Copyright (c) 1993 The Regents of the University of California.
'\" Copyright (c) 1994-1996 Sun Microsystems, Inc.
'\"
'\" See the file "license.terms" for information on usage and redistribution
'\" of this file, and for a DISCLAIMER OF ALL WARRANTIES.
'\" 
'\" RCS: @(#) $Id$
'\" 
'\" The definitions below are for supplemental macros used in Tcl/Tk
'\" manual entries.
'\"
'\" .AP type name in/out ?indent?
'\"	Start paragraph describing an argument to a library procedure.
'\"	type is type of argument (int, etc.), in/out is either "in", "out",
'\"	or "in/out" to describe whether procedure reads or modifies arg,
'\"	and indent is equivalent to second arg of .IP (shouldn't ever be
'\"	needed;  use .AS below instead)
'\"
'\" .AS ?type? ?name?
'\"	Give maximum sizes of arguments for setting tab stops.  Type and
'\"	name are examples of largest possible arguments that will be passed
'\"	to .AP later.  If args are omitted, default tab stops are used.
'\"
'\" .BS
'\"	Start box enclosure.  From here until next .BE, everything will be
'\"	enclosed in one large box.
'\"
'\" .BE
'\"	End of box enclosure.
'\"
'\" .CS
'\"	Begin code excerpt.
'\"
'\" .CE
'\"	End code excerpt.
'\"
'\" .VS ?version? ?br?
'\"	Begin vertical sidebar, for use in marking newly-changed parts
'\"	of man pages.  The first argument is ignored and used for recording
'\"	the version when the .VS was added, so that the sidebars can be
'\"	found and removed when they reach a certain age.  If another argument
'\"	is present, then a line break is forced before starting the sidebar.
'\"
'\" .VE
'\"	End of vertical sidebar.
'\"
'\" .DS
'\"	Begin an indented unfilled display.
'\"
'\" .DE
'\"	End of indented unfilled display.
'\"
'\" .SO
'\"	Start of list of standard options for a Tk widget.  The
'\"	options follow on successive lines, in four columns separated
'\"	by tabs.
'\"
'\" .SE
'\"	End of list of standard options for a Tk widget.
'\"
'\" .OP cmdName dbName dbClass
'\"	Start of description of a specific option.  cmdName gives the
'\"	option's name as specified in the class command, dbName gives
'\"	the option's name in the option database, and dbClass gives
'\"	the option's class in the option database.
'\"
'\" .UL arg1 arg2
'\"	Print arg1 underlined, then print arg2 normally.
'\"
'\" RCS: @(#) $Id$
'\"
'\"	# Set up traps and other miscellaneous stuff for Tcl/Tk man pages.
.if t .wh -1.3i ^B
.nr ^l \n(.l
.ad b
'\"	# Start an argument description
.de AP
.ie !"\\$4"" .TP \\$4
.el \{\
.   ie !"\\$2"" .TP \\n()Cu
.   el          .TP 15
.\}
.ie !"\\$3"" \{\
.ta \\n()Au \\n()Bu
\&\\$1	\\fI\\$2\\fP	(\\$3)
.\".b
.\}
.el \{\
.br
.ie !"\\$2"" \{\
\&\\$1	\\fI\\$2\\fP
.\}
.el \{\
\&\\fI\\$1\\fP
.\}
.\}
..
'\"	# define tabbing values for .AP
.de AS
.nr )A 10n
.if !"\\$1"" .nr )A \\w'\\$1'u+3n
.nr )B \\n()Au+15n
.\"
.if !"\\$2"" .nr )B \\w'\\$2'u+\\n()Au+3n
.nr )C \\n()Bu+\\w'(in/out)'u+2n
..
.AS Tcl_Interp Tcl_CreateInterp in/out
'\"	# BS - start boxed text
'\"	# ^y = starting y location
'\"	# ^b = 1
.de BS
.br
.mk ^y
.nr ^b 1u
.if n .nf
.if n .ti 0
.if n \l'\\n(.lu\(ul'
.if n .fi
..
'\"	# BE - end boxed text (draw box now)
.de BE
.nf
.ti 0
.mk ^t
.ie n \l'\\n(^lu\(ul'
.el \{\
.\"	Draw four-sided box normally, but don't draw top of
.\"	box if the box started on an earlier page.
.ie !\\n(^b-1 \{\
\h'-1.5n'\L'|\\n(^yu-1v'\l'\\n(^lu+3n\(ul'\L'\\n(^tu+1v-\\n(^yu'\l'|0u-1.5n\(ul'
.\}
.el \}\
\h'-1.5n'\L'|\\n(^yu-1v'\h'\\n(^lu+3n'\L'\\n(^tu+1v-\\n(^yu'\l'|0u-1.5n\(ul'
.\}
.\}
.fi
.br
.nr ^b 0
..
'\"	# VS - start vertical sidebar
'\"	# ^Y = starting y location
'\"	# ^v = 1 (for troff;  for nroff this doesn't matter)
.de VS
.if !"\\$2"" .br
.mk ^Y
.ie n 'mc \s12\(br\s0
.el .nr ^v 1u
..
'\"	# VE - end of vertical sidebar
.de VE
.ie n 'mc
.el \{\
.ev 2
.nf
.ti 0
.mk ^t
\h'|\\n(^lu+3n'\L'|\\n(^Yu-1v\(bv'\v'\\n(^tu+1v-\\n(^Yu'\h'-|\\n(^lu+3n'
.sp -1
.fi
.ev
.\}
.nr ^v 0
..
'\"	# Special macro to handle page bottom:  finish off current
'\"	# box/sidebar if in box/sidebar mode, then invoked standard
'\"	# page bottom macro.
.de ^B
.ev 2
'ti 0
'nf
.mk ^t
.if \\n(^b \{\
.\"	Draw three-sided box if this is the box's first page,
.\"	draw two sides but no top otherwise.
.ie !\\n(^b-1 \h'-1.5n'\L'|\\n(^yu-1v'\l'\\n(^lu+3n\(ul'\L'\\n(^tu+1v-\\n(^yu'\h'|0u'\c
.el \h'-1.5n'\L'|\\n(^yu-1v'\h'\\n(^lu+3n'\L'\\n(^tu+1v-\\n(^yu'\h'|0u'\c
.\}
.if \\n(^v \{\
.nr ^x \\n(^tu+1v-\\n(^Yu
\kx\h'-\\nxu'\h'|\\n(^lu+3n'\ky\L'-\\n(^xu'\v'\\n(^xu'\h'|0u'\c
.\}
.bp
'fi
.ev
.if \\n(^b \{\
.mk ^y
.nr ^b 2
.\}
.if \\n(^v \{\
.mk ^Y
.\}
..
'\"	# DS - begin display
.de DS
.RS
.nf
.sp
..
'\"	# DE - end display
.de DE
.fi
.RE
.sp
..
'\"	# SO - start of list of standard options
.de SO
.SH "STANDARD OPTIONS"
.LP
.nf
.ta 4c 8c 12c
.ft B
..
'\"	# SE - end of list of standard options
.de SE
.fi
.ft R
.LP
See the \\fBoptions\\fR manual entry for details on the standard options.
..
'\"	# OP - start of full description for a single option
.de OP
.LP
.nf
.ta 4c
Command-Line Name:	\\fB\\$1\\fR
Database Name:	\\fB\\$2\\fR
Database Class:	\\fB\\$3\\fR
.fi
.IP
..
'\"	# CS - begin code excerpt
.de CS
.RS
.nf
.ta .25i .5i .75i 1i
..
'\"	# CE - end code excerpt
.de CE
.fi
.RE
..
.de UL
\\$1\l'|0\(ul'\\$2
..
.TH tclsh 1 "" Tcl "Aplikacje Tcl"
.BS
'\" Note:  do not modify the .SH NAME line immediately below!
.SH NAZWA
tclsh \- Prosta pow�oka zawieraj�ca interpreter Tcl
.SH SK�ADNIA
\fBtclsh\fR ?\fInazwapliku param param ...\fR?
.BE

.SH OPIS
.PP
\fBTclsh\fR jest pow�okopodobn� aplikacj�, kt�ra odczytuje i
interpretuje polecenia Tcl ze standardowego wej�cia lub pliku.
Je�li zostanie uruchomiona bez parametr�w dzia�a w 
trybie interaktywnym czytaj�c polecenia Tcl ze standardowego 
wej�cia i wy�wietla rezultaty i komunikaty o 
b��dach na standardowym wyj�ciu. Swoje dzia�anie ko�czy w momencie
podania komendy \fBexit\fR lub je�li standardowe wej�cie 
dotrze do ko�ca pliku. Je�li w katalogu domowym u�ytkownika istnieje
plik \fB.tclshrc\fR, \fBtclsh\fR zinterpretuje ten plik jako skrypt 
Tcl tu� przed odczytaniem pierwszego polecenia ze standardowego wej�cia.

.SH "PLIKI SKRYPT�W"
.PP
Je�li \fBtclsh\fR jest wywo�any z parametrami, wtedy pierwszy parametr jest 
nazw� pliku skryptu, a reszta parametr�w jest dost�pna w skrypcie jako zmienne
(patrz ni�ej).
Zamiast czyta� polecenia ze standardowego wej�cia \fBtclsh\fR b�dzie odczytywa�
polecenia Tcl z pliku o podanej nazwie. \fBTclsh\fR zako�czy dzia�anie kiedy
dotrze do ko�ca pliku.
W tym przypadku nie nast�puje automatyczne przetwarzanie \fB.tclshrc\fR, ale w razie 
potrzeby plik skryptu mo�e zawsze z niego \fBkorzysta�\fR.

.PP
Je�li utworzysz plik ze skryptem Tcl, kt�rego pierwsza linia zawiera� b�dzie
.CS
\fB#!/usr/local/bin/tclsh\fR
.CE
i je�li nadasz mu prawa do wykonywania, mo�esz wtedy uruchomi� plik skryptu 
bezpo�rednio z pow�oki.
Zak�adamy, �e \fBtclsh\fR zosta� zainstalowany domy�lnie w /usr/local/bin. Je�li
zosta� zainstalowany w innym miejscu, b�dziesz musia� zmodyfikowa� 
powy�sz� lini�, tak aby by�a zgodna z twoj� instalacj�.
Wiele system�w UNIX nie pozwala aby linia zaczynaj�ca si� od \fB#!\fR mia�a
d�ugo�� wi�ksz� ni� 30 znak�w, wi�c upewnij si� czy plik wykonywalny
\fBtclsh\fR mo�e by� dost�pny przy u�yciu kr�tkiej nazwy pliku.
.PP
Lepszym sposobem mo�e by� rozpoczynanie plik�w ze skryptami 
tymi trzema liniami:
.CS
\fB#!/bin/sh
# nast�pna linia uruchamia tclsh \e
exec tclsh "$0" "$@"\fR
.CE
Spos�b ten mo�na uzna� za lepszy od poprzedniego z trzech powod�w.
Po pierwsze, po�o�enie binari�w \fBtclsh\fR nie musi by� �ci�le 
okre�lone w skrypcie: mog� by� one umieszczone gdziekolwiek w �cie�ce 
szukania twojej pow�oki (PATH). Po drugie, dzi�ki temu mo�na obej�� 
30-znakowe ograniczenie nazwy pliku z poprzedniego przypadku.
Po trzecie, ten spos�b zadzia�a nawet wtedy, kiedy \fBtclsh\fR sam jest 
skryptem pow�oki (tak dzieje si� w niekt�rych systemach, �eby obs�u�y�
wiele architektur lub system�w operacyjnych: \fBtclsh\fR wybiera jeden z
kilku binari�w do uruchomienia). Te trzy linie sprawiaj�, �e zar�wno 
\fBsh\fR jak i \fBtclsh\fR wykonuj� skrypt, ale \fBexec\fR jest wykonywany
jedynie przez \fBsh\fR.
Pow�oka \fBsh\fR przetwarza skrypt jako pierwsza, traktuje drug� lini� jako komentarz
i wykonuje lini� trzeci�.
Polecenie \fBexec\fR sprawia, �e pow�oka \fBsh\fR zaprzestaje dalszego 
przetwarzania i zamiast tego uruchamia \fBtclsh\fR, kt�ry przetworzy 
ca�y skrypt jeszcze raz.
W momencie uruchomienia, \fBtclsh\fR traktuje trzy pierwsze linie 
jako komentarz, poniewa� na ko�cu drugiej linii jest backslash, kt�ry powoduje,
�e trzecia linia jest traktowana jako cz�� komentarza z linii drugiej.

.SH "ZMIENNE"
.PP
\fBTclsh\fR posiada nast�puj�ce zmienne:
.TP 15
\fBargc\fR
Zawiera liczb� parametr�w \fIparam\fR (0 je�li brak) z wy��czeniem
nazwy pliku skryptu.
.TP 15
\fBargv\fR
Zawiera list� Tcl, kt�rej elementami s� parametry \fIparam\fR lub 
jest pusta je�li nie ma parametr�w \fIparam\fR.
.TP 15
\fBargv0\fR
Zawiera \fInazw�pliku\fR je�li by�a podana. 
W innym przypadku zawiera nazw� pliku, z kt�rego uruchomiono \fBtclsh\fR.
.TP 15
\fBtcl_interactive\fR
Zawiera warto�� 1 je�li \fBtclsh\fR by� uruchomiony w trybie interaktywnym
(nie podano \fInazwypliku\fR i wej�cie standardowe jest urz�dzeniem terminalowym),
w innym przypadku zawiera 0.

.SH ZNAKI ZACH�TY
.PP
Kiedy \fBtclsh\fR jest uruchomiony w trybie interaktywnym, normalnie, po 
ka�dym poleceniu wy�wietla znak zach�ty ``\fB% \fR''. Mo�na jednak zmieni�
znak zach�ty poprzez ustawienie zmiennych 
\fBtcl_prompt1\fR i \fBtcl_prompt2\fR.  Je�eli zmienna
\fBtcl_prompt1\fR jest ustawiona, musi ona zawiera� skrypt Tcl 
wy�wietlaj�cy znak zach�ty. Zamiast wy�wietlania znaku zach�ty 
\fBtclsh\fR wykona skrypt zawarty w zmiennej \fBtcl_prompt1\fR.
Zmienna \fBtcl_prompt2\fR jest u�ywana je�eli bie��ce polecenie nie
jest sko�czone, a jego wpisywanie zosta�o przeniesione do nowej linii. 
W przypadku, gdy \fBtcl_prompt2\fR nie jest ustawione nie jest wy�wietlany 
znak zach�ty dla niedoko�czonych polece�.

.SH S�OWA KLUCZOWE
parametr, interpreter, znak zach�ty, plik skryptu, pow�oka
