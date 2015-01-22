Name:		shinken-mod-booster-nrpe
Version:	1.4.1
Release:	2kaji0.2
Summary:	Shinken Module Booster NRPE for Poller

Group:		Network
License:	AGPLv3+
URL:		https://github.com/kaji-project/shinken-mod-booster-nrpe
Source0:	%{name}_%{version}.orig.tar.gz

BuildArch:  noarch

Requires:	shinken-common >= 2.0
Requires:   pyOpenSSL

%description
Shinken NRPE module for Poller

%prep
%setup -q


%build


%install
rm -rf %{buildroot}/*

install -d %{buildroot}/usr/share/pyshared/shinken/modules/booster-nrpe
install -pm07555 module/* %{buildroot}/usr/share/pyshared/shinken/modules/booster-nrpe 

install -d %{buildroot}/usr/share/doc/%{name}
install -pm0755 doc/* %{buildroot}/%{_docdir}/%{name}

install -d %{buildroot}/etc/shinken/modules
install -pm0755 etc/modules/* %{buildroot}/etc/shinken/modules


%files
/usr/share/pyshared/shinken/modules/booster-nrpe
%config(noreplace) %{_sysconfdir}/shinken/modules/

%docdir
%{_docdir}/%{name}


%changelog
* Wed Jan 21 2015 Sébastien Coavoux <sebastien.coavoux@savoirfairelinux.com> 1.4.1-2kaji0.2
- Initial Package
