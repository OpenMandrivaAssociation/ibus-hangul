Summary:	ibus - Korean Hangul engine
Name:		ibus-hangul
Version:	1.4.2
Release:	2
Group:		System/Internationalization
License:	GPLv2+
Url:		http://code.google.com/p/ibus/
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	intltool
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(libhangul) >= 0.1.0
Requires:	ibus

%description
ibus - Korean Hangul engine.

%files -f %{name}.lang
%{_bindir}/*
%{_libdir}/%{name}
%{_libexecdir}/ibus-engine-hangul
%{_libexecdir}/ibus-setup-hangul
%{_datadir}/%{name}
%{_iconsdir}/*/*/*
%{_datadir}/ibus/component/*.xml
%{_datadir}/applications/*.desktop

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

