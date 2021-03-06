#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Crypt
%define		pnam	Rot13
Summary:	Crypt::Rot13 Perl module - a rotational deviator
Summary(pl.UTF-8):	Moduł Perla Crypt::Rot13 - obrotowy dewiator
Name:		perl-Crypt-Rot13
Version:	0.6
Release:	2
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/AYRNIEU/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0898cc852619875a743678083152155a
URL:		http://search.cpan.org/dist/Crypt-Rot13/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rot13 provides an object into which arrays may be placed, and then
returned to you in altered - specifically: rotated - form. Valid
rot13() arguments are 0-26, though 0 and 26 do not alter the array.

%description -l pl.UTF-8
Rot13 udostępnia obiekt, w którym można umieszczać tablice, które
następnie są zwracane w zmodyfikowanej, a konkretnie "obróconej"
formie. Prawidłowy argument dla rot13() to liczba z przedziału 0-26,
ale 0 i 26 nie zmieniają zawartości tablicy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/Rot13.pm
%{_mandir}/man3/*
