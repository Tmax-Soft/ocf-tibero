%define debug_package %{nil}

Name:		ocf-tibero		
Version:	%{version}
Release:	%{release}
Summary:	Resource script for Tibero database

Group:		System Environment/Base
License:	GPLv2
URL:		https://github.com/ivoronin/ocf-tibero
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	redhat-rpm-config
Requires:	resource-agents

%description
Manages Tibero database as an OCF resource in an High Availability setup.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
install -m 0755 -D tibero %{buildroot}/usr/lib/ocf/resource.d/heartbeat/tibero

%clean
rm -rf %{buildroot}

%files
%attr(0755,root,root) /usr/lib/ocf/resource.d/heartbeat/tibero
%doc

%changelog
