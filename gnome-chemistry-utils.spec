Summary:	Backend for GNOME chemistry apps
Summary(pl):	Backend dla aplikacji chemicznych GNOME
Name:		gnome-chemistry-utils
Version:	0.6.0
Release:	1
License:	LGPL
Group:		X11/Applications/Science
Source0:	http://savannah.nongnu.org/download/gchemutils/%{name}-%{version}.tar.bz2
# Source0-md5:	46eb14c0f61386f75bd27063b4e905dd
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

%description -l pl
GNOME Chemistry Utils to zestaw klas C++ i widgetów GTK2 zwi±zanych z
chemi±. Obecnie u¿ywany jest w programach GNOME Crystal (gcrystal) i
GNOME Chemistry Paint (gchempaint).

%package devel
Summary:	Header files for gnome-chemistry-utils library
Summary(pl):	Pliki nag³ówkowe gnome-chemistry-utils
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

%description devel -l pl
Pakiet gnome-chemistry-utils-devel zawiera pliki nag³ówkowe niezbêdne
do budowania programów u¿ywaj±cych bibliotek gnome-chemistry-utils.

%package static
Summary:	Static gnome-chemistry-utils libraries
Summary(pl):	Statyczne biblioteki gnome-chemistry-utils
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gnome-chemistry-utils libraries.

%description static -l pl
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
update-mime-database %{_datadir}/mime >/dev/null 2>&1 ||:
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
/sbin/ldconfig
if [ "$1" = "0" ]; then
	umask 022
	update-mime-database %{_datadir}/mime >/dev/null 2>&1
	[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/gchemutils
%{_datadir}/mime/packages/gchemutils.xml
%{_desktopdir}/*.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gchemutils
%{_pkgconfigdir}/*.pc
%{_docdir}/gchemutils

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
