%global service searchlight
%global release_name liberty
Name:           openstack-%{service}
Version:        0.1.0
Release:        1%{?dist}
Summary:        OpenStack Indexing and Search

License:        ASL 2.0
URL:            https://launchpad.net/searchlight
Source0:        https://launchpad.net/%{service}/%release_name}/%{version}/+download/searchlight-%{version}.tar.gz

BuildRequires:  python-setuptools
BuildRequires:  python2-devel
Requires:       python-elasticsearch
Requires:       python-pbr
Requires:       python-eventlet
Requires:       python-paste-deploy
Requires:       python-webob
Requires:       python-routes
Requires:       pycryptopp
Requires:       python-oslo-config
Requires:       python-oslo-concurrency
Requires:       python-oslo-context
Requires:       python-oslo-middleware
Requires:       python-oslo-service
Requires:       python-oslo-utils
Requires:       python-stevedore
Requires:       python-keystonemiddleware
Requires:       python-wsme
Requires:       python-paste
Requires:       python-keystoneclient
Requires:       pyOpenSSL
Requires:       python-six
Requires:       python-oslo-i18n
Requires:       python-oslo-log
Requires:       python-oslo-messaging
Requires:       python-oslo-policy
Requires:       python-oslo-serializaion
Requires:       python-osprofiler
Requires:       python-designateclient
Requires:       python-glanceclient
Requires:       python-novaclient
BuildArch:      noarch

%description
Mission: To provide advanced and scalable search across multi-tenant cloud
resources.

This is intended to improve performance of OpenStack API services while
dramatically improving search capabilities. It will improve performance by
offloading user search queries from existing API servers and utilizing
technologies designed for large scale searching. The desired user experience
is greatly dependent upon a rich, dynamic, near real time faceted and
aggregated search capability with a strong query language.

%prep
%setup -q -n %{service}-%{version}

rm -rf {test-,}requirements.txt


%build
export OSLO_PACKAGE_VERSION=%{version}
%{__python2} setup.py build

sphinx-build -b html doc/source html


%install
python setup.py install --skip-build --root %{buildroot}


%files
%doc html
%doc README.rst
%license LICENSE
%{python_sitelib}/%{service}
%{python_sitelib}/%{service}-%{version}-py%{python2_version}.egg-info
%{_bindir}/searchlight-api
%{_bindir}/searchlight-control
%{_bindir}/searchlight-listener
%{_bindir}/searchlight-manage


%changelog
* Fri Oct 30 2015 Matthias Runge <mrunge@redhat.com>
- initial package
