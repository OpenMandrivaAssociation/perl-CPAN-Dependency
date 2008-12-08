
%define realname   CPAN-Dependency
%define version    0.15
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Analyzes CPAN modules and generates their dependency tree
Source:     http://www.cpan.org/modules/by-module/CPAN/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
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
%setup -q -n %{realname}-%{version} 

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


