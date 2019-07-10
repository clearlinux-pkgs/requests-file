#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x6BA525CF7F55FA2E (dshea@redhat.com)
#
Name     : requests-file
Version  : 1.4.3
Release  : 1
URL      : https://files.pythonhosted.org/packages/a0/f9/8c1712aea1b70c6a77db322bb18610a078ba8f44876e95289137953db30d/requests-file-1.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/a0/f9/8c1712aea1b70c6a77db322bb18610a078ba8f44876e95289137953db30d/requests-file-1.4.3.tar.gz
Source99 : https://files.pythonhosted.org/packages/a0/f9/8c1712aea1b70c6a77db322bb18610a078ba8f44876e95289137953db30d/requests-file-1.4.3.tar.gz.asc
Summary  : File transport adapter for Requests
Group    : Development/Tools
License  : Apache-2.0
Requires: requests-file-python = %{version}-%{release}
Requires: requests-file-python3 = %{version}-%{release}
Requires: requests
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : requests
BuildRequires : six

%description
Requests-File
=============
Requests-File is a transport adapter for use with the `Requests`_ Python
library to allow local filesystem access via file:\/\/ URLs.

%package python
Summary: python components for the requests-file package.
Group: Default
Requires: requests-file-python3 = %{version}-%{release}

%description python
python components for the requests-file package.


%package python3
Summary: python3 components for the requests-file package.
Group: Default
Requires: python3-core

%description python3
python3 components for the requests-file package.


%prep
%setup -q -n requests-file-1.4.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1562795818
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
