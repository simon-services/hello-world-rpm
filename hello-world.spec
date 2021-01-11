Name: hello-world-rpm
Version: 0.0
Release: 1
Summary: "hello world obs testing project"
License: BSD
URL: https://github.com/simon-services/hello-world-rpm.git
Source0: %{name}-%{version}.tar.gz
BuildArch: x86_64
Requires: supervisor

%description
hello world obs testing project

%prep
%setup
%build

%install
%files
