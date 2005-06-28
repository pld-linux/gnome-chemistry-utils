#
# Conditional build:
%bcond_with gtkglarea	# use gtkglarea instead of gtkglext
#
Summary:	Backend for GNOME chemistry apps
Summary(pl):	Backend dla aplikacji chemicznych GNOME
Name:		gnome-chemistry-utils
Version:	0.2.5
Release:	2
License:	LGPL
Group:		X11/Applications/Science
Source0:	http://savannah.nongnu.org/download/gchemutils/%{name}-%{version}.tar.bz2
# Source0-md5:	40aab80476187645e05dabf1ffb3caad
Patch0:		%{name}-DESTDIR.patch
URL:		http://www.nongnu.org/gchemutils/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
%{?with_gtkglarea:BuildRequires:	gtkglarea-devel >= 1.99.0}
%{?with_gtkglarea:BuildConflicts:	gtkglext-devel >= 0.6.0}
%{!?with_gtkglarea:BuildRequires:	gtkglext-devel >= 0.6.0}
BuildRequires:	intltool
BuildRequires:	libbonoboui-devel >= 2.8.1-2
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeprint-devel >= 2.10.0
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openbabel-devel >= 1.100.2
BuildRequires:	pkgconfig
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
Obsoletes:	gcu-lib-devel

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
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTMLDIR=%{_gtkdocdir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gchemutils
%{_datadir}/mime-info/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gcu
%{_libdir}/pkgconfig/*.pc
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
