%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	Rot13
Summary:	Crypt::Rot13 Perl module - a rotational deviator
Summary(pl):	Modu³ Perla Crypt::Rot13 - obrotowy dewiator
Name:		perl-Crypt-Rot13
Version:	0.04
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rot13 provides an object into which arrays may be placed, and then
returned to you in altered - specifically: rotated - form. Valid
rot13() arguments are 0-26, though 0 and 26 do not alter the array.

%description -l pl
Rot13 udostêpnia obiekt, w którym mo¿na umieszczaæ tablice, które
nastêpnie s± zwracane w zmodyfikowanej, a konkretnie "obróconej"
formie. Prawid³owy argument dla rot13() to liczba z przedzia³u 0-26,
ale 0 i 26 nie zmieniaj± zawarto¶ci tablicy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{__make} test

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
