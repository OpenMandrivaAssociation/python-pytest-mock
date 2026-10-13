%global pypi_name pytest-mock
%bcond_with bootstrap

Name:           python-%{pypi_name}
Version:        3.16.0
Release:        1
Summary:        Thin-wrapper around the mock package for easier use with pytest
Group:          Development/Python
License:        MIT
URL:            https://github.com/pytest-dev/pytest-mock/
# Also https://pypi.org/project/pytest-mock/
Source0:        https://files.pythonhosted.org/packages/source/p/pytest_mock/pytest_mock-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:	python
BuildRequires:  python%{pyver}dist(pytest) >= 5
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(tomli)
%if %{with bootstrap}
BuildRequires:  python%{pyver}dist(tox)
%endif

%build -p
# The sdist is not a git checkout.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%description
 pytest-mock This plugin provides a mocker fixture which is a thin-wrapper
around the patching API provided by the mock package < code-block:: python
import os class UnixFS: @staticmethod def rm(filename): os.remove(filename) def
test_unix_fs(mocker): mocker.patch('os.remove') UnixFS.rm('file')
os.remove.assert_called_once_with('file') Besides undoing the mocking
automatically after the end of...

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python_sitelib}/pytest_mock
%{python_sitelib}/pytest_mock-%{version}.dist-info
