%global __provides_exclude devel\\(.*|libaudioscrobbler\\.so\\.0.*|libfilesystem\\.so\\.0.*|libinformation\\.so\\.0.*|liblibnotify\\.so\\.0.*|libmmkeys\\.so\\.0.*|libradios\\.so\\.0.*|libwikipedia\\.so\\.0.*
%global __requires_exclude libaudioscrobbler\\.so\\.0.*|libfilesystem\\.so\\.0.*|libinformation\\.so\\.0.*|liblibnotify\\.so\\.0.*|libmmkeys\\.so\\.0.*|libradios\\.so\\.0.*|libwikipedia\\.so\\.0.*

Summary:	A GTK+ client for MPD
Name:	ario
Version:	1.6
Release:	1
Group:	Sound
License:	GPLv2+
Url:		https://ario-player.sourceforge.net/
# Use a devel snapshot to pick up support for gtk+3
#Source0:	https://sourceforge.net/projects/ario-player/files/ario-player/%%{version}/%%{name}-%%{version}.tar.gz
Source0: ario-1.6-r822.tar.xz
Source100:	%{name}.rpmlintrc
BuildRequires:	intltool
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libmpdclient)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(unique-1.0)
Requires:	mpd

%description
A GTK+ client for MPD (Music player daemon). The interface used to browse the
library is inspired by Rhythmbox but Ario aims to be much lighter and faster.

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_iconsdir}/*/*/apps/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}-r822


%build
./autogen.sh

# Configure force prefix == /usl/local and then does not propagate the changes
# the the makefile for lang
sed -i 's|ac_default_prefix=/usr/local|ac_default_prefix=/usr|g' configure

# Using our configure macros makes the build
# fail with boatloads of linking errors
./configure \
	--libdir="%{_libdir}" \
	--bindir="%{_bindir}" \
	--datadir="%{_datadir}" \
	--disable-static

%make_build


%install
%make_install

rm -f %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache

%find_lang %{name}
