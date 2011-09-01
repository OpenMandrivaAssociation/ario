Name: ario
Version: 1.5.1
Release: %mkrel 1
Summary: Ario is a GTK2 client for MPD
Group: Sound
License: GPLv2
Url: http://ario-player.sourceforge.net/
Source: %{name}-%{version}.tar
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: intltool
BuildRequires: unique-devel
BuildRequires: gnutls-devel
BuildRequires: curl-devel
BuildRequires: libxml2-devel
BuildRequires: glib2-devel
BuildRequires: libmpdclient-devel
BuildRequires: libnotify-devel
BuildRequires: taglib-devel
BuildRequires: libsoup-devel
BuildRequires: avahi-glib-devel
BuildRequires: avahi-client-devel
Requires: mpd

%description
Ario is a GTK2 client for MPD (Music player daemon).
The interface used to browse the library is inspired
by Rhythmbox but Ario aims to be much lighter and faster.

%prep
%setup -q

%build
./configure --libdir=%{_libdir} --datadir=%{_datadir}
%make

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

%__rm -f %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_iconsdir}/*/*/apps/*

