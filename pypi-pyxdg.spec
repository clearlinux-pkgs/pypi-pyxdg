#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyxdg
Version  : 0.28
Release  : 43
URL      : https://files.pythonhosted.org/packages/b0/25/7998cd2dec731acbd438fbf91bc619603fc5188de0a9a17699a781840452/pyxdg-0.28.tar.gz
Source0  : https://files.pythonhosted.org/packages/b0/25/7998cd2dec731acbd438fbf91bc619603fc5188de0a9a17699a781840452/pyxdg-0.28.tar.gz
Summary  : PyXDG contains implementations of freedesktop.org standards in python.
Group    : Development/Tools
License  : LGPL-2.0
Requires: pypi-pyxdg-license = %{version}-%{release}
Requires: pypi-pyxdg-python = %{version}-%{release}
Requires: pypi-pyxdg-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
The XDG Package contains:
- Implementation of the XDG-Base-Directory Standard
http://standards.freedesktop.org/basedir-spec/

%package license
Summary: license components for the pypi-pyxdg package.
Group: Default

%description license
license components for the pypi-pyxdg package.


%package python
Summary: python components for the pypi-pyxdg package.
Group: Default
Requires: pypi-pyxdg-python3 = %{version}-%{release}

%description python
python components for the pypi-pyxdg package.


%package python3
Summary: python3 components for the pypi-pyxdg package.
Group: Default
Requires: python3-core
Provides: pypi(pyxdg)

%description python3
python3 components for the pypi-pyxdg package.


%prep
%setup -q -n pyxdg-0.28
cd %{_builddir}/pyxdg-0.28
pushd ..
cp -a pyxdg-0.28 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656403435
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyxdg
cp %{_builddir}/pyxdg-0.28/COPYING %{buildroot}/usr/share/package-licenses/pypi-pyxdg/44f7289042b71631acac29b2f143330d2da2479e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyxdg/44f7289042b71631acac29b2f143330d2da2479e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
