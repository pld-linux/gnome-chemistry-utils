Summary:	Backend for GNOME chemistry apps
Summary(pl.UTF-8):	Backend dla aplikacji chemicznych GNOME
Name:		gnome-chemistry-utils
Version:	0.6.5
Release:	1
License:	LGPL
Group:		X11/Applications/Science
Source0:	http://savannah.nongnu.org/download/gchemutils/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	493dbb6aea0d3664e7b203337fafe056
URL:		http://www.nongnu.org/gchemutils/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
#BuildRequires:	chemical-mime-data >= 0.1.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	gtkglext-devel >= 1.0.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeprint-devel >= 2.10.0
BuildRequires:	libgoffice-devel >= 0.1.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
#BuildRequires:	mozilla-devel
BuildRequires:	openbabel-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	shared-mime-info >= 0.12
Obsoletes:	gcu
Obsoletes:	gcu-lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The GNOME Chemistry Utils provide C++ classes and GTK2 widgets related
to chemistry. They are currently used in GNOME Crystal (gcrystal) and
GNOME Chemistry Paint (gchempaint).

%description -l pl.UTF-8
GNOME Chemistry Utils to zestaw klas C++ i widgetów GTK2 związanych z
chemią. Obecnie używany jest w programach GNOME Crystal (gcrystal) i
GNOME Chemistry Paint (gchempaint).

%package devel
Summary:	Header files for gnome-chemistry-utils library
Summary(pl.UTF-8):	Pliki nagłówkowe gnome-chemistry-utils
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-vfs2-devel >= 2.10.0-2
Requires:	gtk+2-devel >= 2:2.6.0
Requires:	gtkglext-devel >= 1.0.0
Requires:	libglade2-devel >= 1:2.5.1
Requires:	libgnomeprint-devel >= 2.10.0
Requires:	libgoffice-devel >= 0.1.0
Requires:	openbabel-devel >= 2.0.0
Obsoletes:	gcu-lib-devel
Conflicts:	pkgconfig < 1:0.20

%description devel
The gnome-chemistry-utils-devel package includes the header files
necessary for developing programs using the gnome-chemistry-utils
libraries.

%description devel -l pl.UTF-8
Pakiet gnome-chemistry-utils-devel zawiera pliki nagłówkowe niezbędne
do budowania programów używających bibliotek gnome-chemistry-utils.

%package static
Summary:	Static gnome-chemistry-utils libraries
Summary(pl.UTF-8):	Statyczne biblioteki gnome-chemistry-utils
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gnome-chemistry-utils libraries.

%description static -l pl.UTF-8
Statyczne biblioteki gnome-chemistry-utils.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static \
	--disable-update-databases
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
/sbin/ldconfig
if [ "$1" = "0" ]; then
	umask 022
	[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %{_libdir}/chem-viewer
%{_datadir}/gchemutils
%{_desktopdir}/*.desktop
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gchemutils
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/libgcu.3*
%{_docdir}/gchemutils

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

# -n browser-plugin-*
# /usr/lib64/mozilla-firefox/plugins/libmozgcu.so
