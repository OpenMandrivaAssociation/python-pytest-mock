# Created by pyp2rpm-3.3.5
%global pypi_name pytest-mock
%bcond_with bootstrap

Name:           python-%{pypi_name}
Version:        3.6.1
Release:        1
Summary:        Thin-wrapper around the mock package for easier use with pytest
Group:          Development/Python
License:        MIT
URL:            https://github.com/pytest-dev/pytest-mock/
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pre-commit)
BuildRequires:  python3dist(pytest) >= 5
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
%if %{with bootstrap}
BuildRequires:  python3dist(tox)
%endif

%description
 pytest-mock This plugin provides a mocker fixture which is a thin-wrapper
around the patching API provided by the mock package < code-block:: python
import os class UnixFS: @staticmethod def rm(filename): os.remove(filename) def
test_unix_fs(mocker): mocker.patch('os.remove') UnixFS.rm('file')
os.remove.assert_called_once_with('file') Besides undoing the mocking
automatically after the end of...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_mock
%{python3_sitelib}/pytest_mock-%{version}-py%{python3_version}.egg-info

