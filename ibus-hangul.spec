%define	version 1.3.1
%define	release %mkrel 2

Name:      ibus-hangul
Summary:   ibus - Korean Hangul engine
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPLv2+
URL:       http://code.google.com/p/ibus/
Source0:   http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libhangul-devel >= 0.0.10
BuildRequires: ibus-devel >= 1.3.9-5
BuildRequires: intltool >= 0.35.0
Requires:	ibus >= 1.3.0
Requires(post,preun): GConf2

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

%post
%post_ibus_register_engine hangul ko

%preun
%preun_ibus_unregister_engine hangul

%files -f %name.lang
%defattr(-,root,root)
%{_libexecdir}/ibus-*
%{_datadir}/%{name}
%{_datadir}/ibus/component/*.xml
