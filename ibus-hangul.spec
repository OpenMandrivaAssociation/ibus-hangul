%define	version 1.3.1
%define	release %mkrel 4

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


%changelog
* Fri May 06 2011 Funda Wang <fwang@mandriva.org> 1.3.1-3mdv2011.0
+ Revision: 669828
- rebuild

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 1.3.1-2
+ Revision: 659303
- rebuild for new ibus

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 1.3.1-1
+ Revision: 640312
- new version 1.3.1

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.0.20100329-2mdv2011.0
+ Revision: 611122
- rebuild

* Mon Apr 26 2010 Funda Wang <fwang@mandriva.org> 1.3.0.20100329-1mdv2010.1
+ Revision: 538845
- new version 1.3.0.20100329

* Sun Jan 03 2010 Funda Wang <fwang@mandriva.org> 1.2.0.20100102-1mdv2010.1
+ Revision: 485770
- BR intltool
- new version 1.2.0.20100102

* Fri Nov 06 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20091031-1mdv2010.1
+ Revision: 460646
- bump BR
- New version  1.2.0.20091031

* Mon Aug 03 2009 Funda Wang <fwang@mandriva.org> 1.2.0.20090617-1mdv2010.0
+ Revision: 408395
- new version 1.2.0

* Fri May 01 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090328-2mdv2010.0
+ Revision: 369491
- New version 1.1.0.20090328

* Fri Feb 13 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090211-2mdv2009.1
+ Revision: 340004
- New version 1.1.0.20090211

* Sat Feb 07 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090205-2mdv2009.1
+ Revision: 338336
- fix file list

* Thu Feb 05 2009 Funda Wang <fwang@mandriva.org> 1.1.0.20090205-1mdv2009.1
+ Revision: 337934
- swig is of no use here
- no more python dep
- New version 1.1.0.20090205

* Thu Dec 25 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20081023-2mdv2009.1
+ Revision: 318671
- rebuild for new python

* Thu Oct 23 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20081023-1mdv2009.1
+ Revision: 296678
- New version 0.1.1.20081023

* Fri Sep 05 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20080901-1mdv2009.0
+ Revision: 281258
- new version

* Mon Aug 25 2008 Funda Wang <fwang@mandriva.org> 0.1.1.20080823-1mdv2009.0
+ Revision: 275852
- import ibus-hangul


