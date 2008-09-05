%define	version 0.1.1.20080901
%define	release %mkrel 1

Name:      ibus-hangul
Summary:   ibus - Korean Hangul engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libhangul-devel
BuildRequires: python-devel
BuildRequires: swig
Requires:	ibus

%description
ibus - Korean Hangul engine.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%{name}
%{python_sitearch}/*
%{_datadir}/ibus/engine/*.engine
