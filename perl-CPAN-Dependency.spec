%define upstream_name    CPAN-Dependency
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Analyzes CPAN modules and generates their dependency tree
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/CPAN/CPAN-Dependency-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(CPANPLUS)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBI)
BuildRequires:	perl(File::Slurp)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Module::CoreList)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(YAML)
BuildArch:	noarch

%description
This module can process a set of distributions, up to the whole CPAN, and
extract the dependency relations between these distributions.
Alternatively, it can load the prerequisites information from a CPANTS
database. 

It also calculates a score for each distribution based on the number of
times it appears in the prerequisites of other distributions. The algorithm
is described in more details in the "SCORE CALCULATION" manpage. 

'CPAN::Dependency' stores the data in an internal structure which can be
saved and loaded using 'save_deps_tree()' and 'load_deps_tree()'. The
structure looks like this: 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.150.0-2mdv2011.0
+ Revision: 654879
- rebuild for updated spec-helper

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 401699
- rebuild using %%perl_convert_version
- fixed license field

* Mon Dec 08 2008 Jérôme Quelin <jquelin@mandriva.org> 0.15-1mdv2009.1
+ Revision: 311882
- import perl-CPAN-Dependency


* Mon Dec 08 2008 cpan2dist 0.15-1mdv
- initial mdv release, generated with cpan2dist


