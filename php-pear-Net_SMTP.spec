%include	/usr/lib/rpm/macros.php
%define         _class          Net
%define         _subclass       SMTP
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - implementation of the SMTP protocol
Summary(pl):	%{_pearname} - implementacja protoko³u SMTP
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an implementation of the SMTP protocol using PEAR's
Net_Socket:: class.

%description -l pl
Dostarcza implementacjê protoko³u SMTP przy u¿yciu PEAR-owej klasy
Net_Socket:: .

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
