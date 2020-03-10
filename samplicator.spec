Name:		samplicator
Version:	1.3.8
Release:	1
Summary:	Send copies of (UDP) datagrams to multiple receivers, with optional sampling and spoofing
Group:		Applications/Internet
License:	GPLv2+
URL:		https://github.com/chipitsine/samplicator
Source0:	https://github.com/chipitsine/samplicator/archive/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	make

%description
Send copies of (UDP) datagrams to multiple receivers, with optional sampling and spoofing

%prep
%setup -q -n %{name}-%{version}

%build
cd %{_builddir}/%{name}-%{version}
autoreconf -iv

%configure 
make 

%install

make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/samplicate

%changelog
* Tue Mar 03 2020 Ilya Shipitcin <chipitsine@gmail.com> - 1.3.8
- initial rpm
