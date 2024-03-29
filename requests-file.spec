#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : requests-file
Version  : 1.5.1
Release  : 20
URL      : https://files.pythonhosted.org/packages/50/5c/d32aeed5c91e7970ee6ab8316c08d911c1d6044929408f6bbbcc763f8019/requests-file-1.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/50/5c/d32aeed5c91e7970ee6ab8316c08d911c1d6044929408f6bbbcc763f8019/requests-file-1.5.1.tar.gz
Summary  : File transport adapter for Requests
Group    : Development/Tools
License  : Apache-2.0
Requires: requests-file-license = %{version}-%{release}
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

%package license
Summary: license components for the requests-file package.
Group: Default

%description license
license components for the requests-file package.


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
Provides: pypi(requests_file)
Requires: pypi(requests)
Requires: pypi(six)

%description python3
python3 components for the requests-file package.


%prep
%setup -q -n requests-file-1.5.1
cd %{_builddir}/requests-file-1.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588007940
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/requests-file
cp %{_builddir}/requests-file-1.5.1/LICENSE %{buildroot}/usr/share/package-licenses/requests-file/6ece8941471a5843511a796d798cbb6ac05be6f7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/requests-file/6ece8941471a5843511a796d798cbb6ac05be6f7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
