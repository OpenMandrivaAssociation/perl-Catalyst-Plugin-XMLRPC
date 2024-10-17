%define upstream_name	 Catalyst-Plugin-XMLRPC
%define upstream_version 2.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Dispatch XMLRPC methods with Catalyst
License:	Artistic/GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(RPC::XML)

BuildArch:	noarch

%description
This plugin allows your controller class to dispatch XMLRPC methods
from its own class.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Catalyst


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.10.0-2mdv2011.0
+ Revision: 680767
- mass rebuild

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2.10.0-1mdv2011.0
+ Revision: 461035
- adding missing buildrequires:
- update buildrequires:
- update to 2.01

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2009.0
+ Revision: 241162
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-2mdv2008.0
+ Revision: 86061
- rebuild


* Tue Apr 18 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdk
- contributed by Scott Karns <scott@karnstech.com>

