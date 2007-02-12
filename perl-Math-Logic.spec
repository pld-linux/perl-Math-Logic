#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Logic
Summary:	Math::Logic - pure 2, 3 or multi-value logic
Summary(pl.UTF-8):   Math::Logic - logika czysto 2-, 3- lub wielowartościowa
Name:		perl-Math-Logic
Version:	1.19
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	01352cf5bf8f4be78779ac57c033b7b5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl's built-in logical operators, "and", "or", "xor" and "not"
support 2-value logic. This means that they always produce a result
which is either true or false. In fact Perl sometimes returns 0 and
sometimes returns undef for false depending on the operator and the
order of the arguments. For "true" Perl generally returns the first
value that evaluated to true which turns out to be extremely useful in
practice. Given the choice Perl's built-in logical operators are to be
preferred - but when you really want pure 2-degree logic or 3-degree
logic or multi-degree logic they are available through this module.

%description -l pl.UTF-8
Wbudowane w Perla operatory logiczne: "and", "or", "xor" i "not"
obsługują logikę 2-wartościową. Oznacza to, że zawsze zwracają wynik,
który jest prawdą lub fałszem. W rzeczywistości Perl czasami zwraca 0,
a czasami undef jako fałsz, w zależności od operatora i kolejności
argumentów. Jako "prawdę" Perl zwykle zwraca pierwszą wartość, z
której wyliczona została prawda, co okazuje się być bardzo przydatne w
praktyce. Ten moduł udostępnia logikę czysto 2-wartościową,
3-wartościową lub wielowartościową.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Math/Logic.pm
%{_mandir}/man3/*
