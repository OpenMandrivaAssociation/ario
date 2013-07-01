Name:		ario
Version:	1.5.1
Release:	2
Summary:	GTK2 client for MPD
Group:		Sound
License:	GPLv2
Url:		http://ario-player.sourceforge.net/
Source:		%{name}-%{version}.tar
Patch1:		ario-1.5.1-glib.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libmpdclient)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(avahi-client)
Requires:	mpd

%description
Ario is a GTK2 client for MPD (Music player daemon).
The interface used to browse the library is inspired
by Rhythmbox but Ario aims to be much lighter and faster.

%prep
%setup -q
%patch1 -p1

%build
./configure --libdir=%{_libdir} --datadir=%{_datadir}
%make

%install
%makeinstall

%find_lang %{name}

rm -f %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_iconsdir}/*/*/apps/*

%changelog
* Thu Sep 01 2011 Andrey Bondrov <abondrov@mandriva.org> 1.5.1-1mdv2011.0
+ Revision: 697714
- imported package ario


* Thu Sep 01 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 1.5.1-1mdv2010.2
- New version 1.5.1

* Sun Jan 03 2010 Andrey Bondrov <bondrov@math.dvgu.ru> 1.4.2-69.1mib2009.1
- First build for MIB users
- Mandriva Italia Backports