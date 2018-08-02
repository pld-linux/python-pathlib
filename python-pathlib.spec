#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module [module included in Python 3.4+]

Summary:	Object-oriented filesystem paths
Summary(pl.UTF-8):	Zorientowane obiektowo ścieżki w systemie plików
Name:		python-pathlib
Version:	1.0.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pathlib/
Source0:	https://files.pythonhosted.org/packages/source/p/pathlib/pathlib-%{version}.tar.gz
# Source0-md5:	5099ed48be9b1ee29b31c82819240537
URL:		https://pathlib.readthedocs.org/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
%if "%{py_ver}" < "2.7"
BuildRequires:	python-unittest2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pathlib offers a set of classes to handle filesystem paths.

%description -l pl.UTF-8
pathlib oferuje zbiór klas do obsługi ścieżek w systemie plików.

%package -n python3-pathlib
Summary:	Object-oriented filesystem paths
Summary(pl.UTF-8):	Zorientowane obiektowo ścieżki w systemie plików
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-pathlib
pathlib offers a set of classes to handle filesystem paths.

%description -n python3-pathlib -l pl.UTF-8
pathlib oferuje zbiór klas do obsługi ścieżek w systemie plików.

%package apidocs
Summary:	API documentation for Python %{module} module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona %{module}
Group:		Documentation

%description apidocs
API documentation for Python %{module} module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona %{module}.

%prep
%setup -q -n pathlib-%{version}

%build
%if %{with python2}
%py_build

%{__python} test_pathlib.py
%endif

%if %{with python3}
%py3_build

%{__python3} test_pathlib.py
%endif

%if %{with doc}
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt
%{py_sitescriptdir}/pathlib.py[co]
%{py_sitescriptdir}/pathlib-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pathlib
%defattr(644,root,root,755)
%doc LICENSE.txt README.txt
%{py3_sitescriptdir}/pathlib.py
%{py3_sitescriptdir}/__pycache__/pathlib.cpython-*.py[co]
%{py3_sitescriptdir}/pathlib-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_images,_static,*.html,*.js}
%endif
