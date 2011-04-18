%define upstream_name    CPAN-Dependency
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Analyzes CPAN modules and generates their dependency tree
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(CPANPLUS)
BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBI)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Module::CoreList)
BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warn)
BuildRequires: perl(YAML)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*

