Summary:	Command line tools to deal with linear-timecode (LTC)
Summary(pl.UTF-8):	Narzędzia linii poleceń do obsługi liniowego kodu czasowego (LTC)
Name:		ltc-tools
Version:	0.7.0
Release:	1
License:	GPL v2+
Group:		Applications/Sound
#Source0Download: https://github.com/x42/ltc-tools/releases
Source0:	https://github.com/x42/ltc-tools/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	65711807269b97b87547b66898680680
URL:		https://github.com/x42/ltc-tools
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libltc-devel >= 1.1.0
BuildRequires:	libsndfile-devel
BuildRequires:	pkgconfig
Requires:	libltc >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Command line tools to deal with linear-timecode (LTC).

%description -l pl.UTF-8
Narzędzia linii poleceń do obsługi liniowego kodu czasowego (LTC).

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/jltc2mtc
%attr(755,root,root) %{_bindir}/jltcdump
%attr(755,root,root) %{_bindir}/jltcgen
%attr(755,root,root) %{_bindir}/jltcntp
%attr(755,root,root) %{_bindir}/jltctrigger
%attr(755,root,root) %{_bindir}/ltcdump
%attr(755,root,root) %{_bindir}/ltcgen
%{_mandir}/man1/jltc2mtc.1*
%{_mandir}/man1/jltcdump.1*
%{_mandir}/man1/jltcgen.1*
%{_mandir}/man1/jltcntp.1*
%{_mandir}/man1/jltctrigger.1*
%{_mandir}/man1/ltcdump.1*
%{_mandir}/man1/ltcgen.1*
