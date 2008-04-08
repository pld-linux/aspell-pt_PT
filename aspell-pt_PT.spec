Summary:	Portuguese dictionaries for aspell
Summary(pl.UTF-8):	Portugalskie słowniki dla aspella
Name:		aspell-pt_PT
Version:	20070510
%define	subv	0
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/pt_PT/aspell6-pt_PT-%{version}-%{subv}.tar.bz2
# Source0-md5:	a54267ce8f91de6e6a1baf1e8048cba0
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60.0
Requires:	aspell >= 3:0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Portuguese dictionaries (i.e. word lists) for aspell.

%description -l pl.UTF-8
Portugalskie słowniki (listy słów) dla aspella.

%prep
%setup -q -n aspell6-pt_PT-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
