Name:		gammastep
Summary:	Adjust the color temperature of your screen according to your surroundings
Version:	2.0.11
Release:	3
License:	GPL-3.0-or-later
Group:		Window Manager/Utility
URL:		https://gitlab.com/chinstrap/gammastep
Source0:	https://gitlab.com/chinstrap/gammastep/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	appstream-util
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gobject-introspection
BuildRequires:	hicolor-icon-theme
BuildRequires:	intltool
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-scanner)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-randr)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	systemd-rpm-macros
Requires:	hicolor-icon-theme

%description
Adjust the color temperature of your screen according to
your surroundings.

This may help your eyes hurt less if you are
working in front of the screen at night.

Run gammastep -h for help on command line options.
A graphical indicator is provided, gammastep-indicator.

%package indicator
Summary:	GTK indicator applet for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	python%{pyver}dist(pygobject)
Requires:	python%{pyver}dist(pyxdg)
Requires:	typelib(AppIndicator3)

%description	indicator
This package provides a status icon for %{name} that allows the user
to control color temperature.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
./bootstrap
%configure \
    --with-systemduserunitdir=%{_userunitdir}
%make_build

%install
%make_install
# fix python interpreter
sed -i 's|/env python3|/python3|' %{buildroot}%{_bindir}/%{name}-indicator
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%post
%systemd_user_post %{name}.service

%post indicator
%systemd_user_post %{name}-indicator.service

%preun
%systemd_user_preun %{name}.service

%preun indicator
%systemd_user_preun %{name}-indicator.service

%files -f %{name}.lang
%doc README.md README-colorramp %{name}.conf.sample
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1.*
%{_userunitdir}/%{name}.service

%files indicator
%{_bindir}/%{name}-indicator
%{_datadir}/applications/%{name}-indicator.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}-status-*.svg
%{_datadir}/metainfo/%{name}-indicator.appdata.xml
%{_userunitdir}/%{name}-indicator.service
%{python_sitelib}/%{name}_indicator
