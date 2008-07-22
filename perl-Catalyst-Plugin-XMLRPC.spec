%define module	Catalyst-Plugin-XMLRPC
%define name	perl-%{module}
%define version	1.0
%define release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Summary:	Dispatch XMLRPC methods with Catalyst
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl(Catalyst) >= 5.64
BuildRequires:	perl(RPC::XML)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows your controller class to dispatch XMLRPC methods
from its own class.


%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Catalyst

