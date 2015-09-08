
Name:       python-setuptools
Summary:    Easily build and distribute Python packages
Version:    0.6c11
Release:    2
Group:      Applications/System
License:    Python or ZPLv2.0
BuildArch:  noarch
URL:        http://pypi.python.org/pypi/setuptools
Source0:    http://pypi.python.org/packages/source/s/setuptools/setuptools-%{version}.tar.gz
Source1:    psfl.txt
Source2:    zpl.txt
BuildRequires:  python-devel

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

This package contains the runtime components of setuptools, necessary to
execute the software that requires pkg_resources.py.



%package devel
Summary:    Download, install, upgrade, and uninstall Python packages
Group:      Development/Languages
Requires:   %{name} = %{version}-%{release}
Requires:   python-devel

%description devel
setuptools is a collection of enhancements to the Python distutils that allow
you to more easily build and distribute Python packages, especially ones that
have dependencies on other packages.

This package contains the components necessary to build and install software
requiring setuptools.



%prep
%setup -q -n setuptools-%{version}

%build
find -name '*.txt' | xargs chmod -x
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'



CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
%install
rm -rf %{buildroot}
# Please write install script under ">> install post"


%{__python} setup.py install -O1 --skip-build \
    --root $RPM_BUILD_ROOT \
    --single-version-externally-managed \
    --prefix %{_prefix}

rm -rf $RPM_BUILD_ROOT%{python_sitelib}/setuptools/tests

install -p -m 0644 %{SOURCE1} %{SOURCE2} .
find $RPM_BUILD_ROOT%{python_sitelib} -name '*.exe' | xargs rm -f
chmod +x $RPM_BUILD_ROOT%{python_sitelib}/setuptools/command/easy_install.py


%clean
rm -rf %{buildroot}







%files
%defattr(-,root,root,-)
%doc pkg_resources.txt psfl.txt setuptools.txt zpl.txt
%{python_sitelib}/*
%exclude %{python_sitelib}/easy_install*


%files devel
%defattr(-,root,root,-)
%doc EasyInstall.txt README.txt api_tests.txt psfl.txt zpl.txt
%{python_sitelib}/easy_install*
%{_bindir}/*

