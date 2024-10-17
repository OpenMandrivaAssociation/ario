%define __noautoprov 'devel\\(.*|libaudioscrobbler\\.so\\.0.*|libfilesystem\\.so\\.0.*|libinformation\\.so\\.0.*|liblibnotify\\.so\\.0.*|libmmkeys\\.so\\.0.*|libradios\\.so\\.0.*|libwikipedia\\.so\\.0.*'
%define __noautoreq 'libaudioscrobbler\\.so\\.0.*|libfilesystem\\.so\\.0.*|libinformation\\.so\\.0.*|liblibnotify\\.so\\.0.*|libmmkeys\\.so\\.0.*|libradios\\.so\\.0.*|libwikipedia\\.so\\.0.*'

Summary:	Ario is a GTK2 client for MPD
Name:		ario
Version:	1.5.1
Release:	4
Group:		Sound
License:	GPLv2+
Url:		https://ario-player.sourceforge.net/
Source0:	%{name}-%{version}.tar
Source10:	%{name}.rpmlintrc
Patch1:		ario-1.5.1-glib.patch
BuildRequires:	intltool
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libmpdclient)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(unique-1.0)
Requires:	mpd

%description
Ario is a GTK2 client for MPD (Music player daemon). The interface used to
browse the library is inspired by Rhythmbox but Ario aims to be much lighter
and faster.

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_libdir}/%{name}
%{_bindir}/%{name}
%{_iconsdir}/*/*/apps/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch1 -p1

%build
./configure \
	--libdir=%{_libdir} \
	--datadir=%{_datadir} \
	--disable-static
%make

%install
%makeinstall

%find_lang %{name}

rm -f %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache

