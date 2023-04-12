%define url_ver	%(echo %{version}|cut -d. -f1,2)

%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Name:		gnome-taquin
Version:	3.38.1
Release:	6
Summary:	GNOME Taquin game
License:	GPLv2+ and CC-BY-SA
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Apps/Taquin
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:   https://gitlab.gnome.org/GNOME/gnome-taquin/-/commit/99dea5e7863e112f33f16e59898c56a4f1a547b3.patch
BuildRequires:	pkgconfig(pygobject-3.0) >= 2.28.3
BuildRequires:	gettext
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	meson
BuildRequires:	python
BuildRequires:	vala
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:	pkgconfig(gio-2.0) >= 2.40.0
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(gsound)
BuildRequires:	pkgconfig(libcanberra-gtk3)
BuildRequires:  librsvg-vala-devel
# For help
Requires:	yelp

%description
Test your logic skills in this number grid puzzle.

%prep
%setup -q
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Taquin.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Taquin.gschema.xml
%{_datadir}/%{name}/
%{_iconsdir}/*/*/apps/org.gnome.Taquin*
%{_datadir}/metainfo/org.gnome.Taquin.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Taquin.service
%{_mandir}/man6/%{name}.6*
