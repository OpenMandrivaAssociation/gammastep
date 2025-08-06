Name:		gammastep
Version:	2.0.11
Release:	1
Source0:	https://gitlab.com/chinstrap/gammastep/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Summary:	Adjust the color temperature of your screen according to your surroundings
URL:		https://gitlab.com/chinstrap/gammastep
License:	GPLv3
Group:		Window Manager/Utility

BuildRequires: %{mklibname gettext -d}
BuildRequires: intltool


%description
%summary

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
./bootstrap
%configure
%make_build

%install
%make_install

%post
%systemd_user_post %{name}.service
%systemd_user_post %{name}-indicator.service
%preun
%systemd_user_preun %{name}.service
%systemd_user_preun %{name}-indicator.service

%files
%license README.md
%{_bindir}/%{name}*
%{_prefix}/lib/python3.11/site-packages/*
%{_userunitdir}/gammastep-indicator.service
%{_userunitdir}/gammastep.service
%{_datadir}//applications/*
%{_iconsdir}/hicolor/scalable/apps/*
%{_datadir}//locale/ar/LC_MESSAGES/gammastep.mo
%{_datadir}//locale/be/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/bg/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/ca/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/cs/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/da/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/de/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/el/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/es/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/et/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/eu/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/fi/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/fr/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/gl/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/he/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/hi/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/hr/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/hu/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/it/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/ja/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/ka/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/lt/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/nb/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/nl/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/pl/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/pt/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/ro/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/ru/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/sr/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/sv/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/tr/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/uk/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/gammastep.mo
%{_datadir}/locale/zh_TW/LC_MESSAGES/gammastep.mo
%{_mandir}/man1/%{name}*
%{_datadir}//metainfo/%{name}*
