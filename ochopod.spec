%define name           ochopod
%define version        1.0.0
%define release        1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Container boot application
License:        GPLv3
URL:            https://github.com/autodesk-cloud/ochopod
Source0:        ochopod-v%{version}.tar.gz

Requires:       python-flask
Requires:       python-requests
Requires:       python-kazoo
Requires:       python-pykka
Requires:       python-jinja2
Requires:       curl

BuildRequires:  python-setuptools
BuildRequires:  python-sphinx

BuildArch:      noarch

%description
Ochopod
This project is a small Python package you can use to boot your Docker containers. It is configured to interface with Kubernetes or various Apache Mesos frameworks and coordinates how a given family of containers should cluster together at run-time. It transparently manages dependencies and port remapping as well. In short you effectively apply an overlay to your provisioning stack that enables you to do more !
Ochopod internally relies on Apache Zookeeper for synchronization and metadata storage.

%prep
%setup -q


%build
cd sdk
%{__python} setup.py build

%install
# Install command
cd sdk
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Install documentation
cd ../docs
%{__install} -d -m 755 %{buildroot}/%{_docdir}/ochopod/
sphinx-build -b html -d . . %{buildroot}/%{_docdir}/ochopod/
# no man page for now
#%{__install} -d -m 755 %{buildroot}/%{_mandir}/man7/
#sphinx-build -b man -d . . %{buildroot}/%{_mandir}/man7/
cd ..
%{__cp} -r docs/ %{buildroot}/%{_docdir}/ochopod

# Delete useless files
rm -f %{buildroot}/usr/bin/ocho
rmdir %{buildroot}/usr/bin
find %{buildroot} -name "*.pyc" -delete
find %{buildroot} -name "*.pyo" -delete

%files
%defattr(-,root,root,-)

%dir %{python_sitelib}/ochopod
%{python_sitelib}/ochopod
%{python_sitelib}/ochopod-*.egg-info/

%docdir
%{_docdir}/ochopod
# no man page for now
#%{_mandir}/man7/ochopod.1.gz

%changelog
* Wed Sep 2 2015 Thibault Cohen <thibault.cohen@nuance.com> - 1.0.0-1
- Initial package
