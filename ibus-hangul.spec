Summary:	ibus - Korean Hangul engine
Name:		ibus-hangul
Version:	1.5.3
Release:	1
Group:		System/Internationalization
License:	GPLv2+
URL:           https://github.com/choehwanjin/ibus-hangul
Source0:       https://github.com/choehwanjin/ibus-hangul/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	intltool
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(libhangul) >= 0.1.0
Requires:	ibus

%description
ibus - Korean Hangul engine.

%files -f %{name}.lang
%{_bindir}/*
#{_libdir}/%{name}
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
%configure
%make_build

%install
%make_install

%find_lang %{name}

