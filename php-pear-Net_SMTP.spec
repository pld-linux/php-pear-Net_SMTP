%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       SMTP
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - implementation of the SMTP protocol
Summary(pl):	%{_pearname} - implementacja protoko³u SMTP
Name:		php-pear-%{_pearname}
Version:	1.1.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	af7f864596ed36cc17023991aeb96c69
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an implementation of the SMTP protocol using PEAR's
Net_Socket:: class.

This class has in PEAR status: %{_status}.

%description -l pl
Dostarcza implementacjê protoko³u SMTP przy u¿yciu PEAR-owej klasy
Net_Socket:: .

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
