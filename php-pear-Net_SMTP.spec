%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	Net_SMTP
Summary:	%{_pearname} - implementation of the SMTP protocol
Summary(pl.UTF-8):	%{_pearname} - implementacja protokołu SMTP
Name:		php-pear-%{_pearname}
Version:	1.5.0
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c194d913de360aeebea85385affd3706
URL:		http://pear.php.net/package/Net_SMTP/
BuildRequires:	php-pear-PEAR >= 1:1.4.3
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Net_Socket >= 1.0.7
Suggests:	php-pear-Auth_SASL
Obsoletes:	php-pear-Net_SMTP-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Auth/SASL.*)

%description
Provides an implementation of the SMTP protocol using PEAR's
Net_Socket:: class.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Dostarcza implementację protokołu SMTP przy użyciu PEAR-owej klasy
Net_Socket:: .

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/*.php
