#
# Conditional build:
# _with_gtkglarea	- use gtkglarea instead of gtkglext
#
Summary:	Backend for Gnome chemistry apps
Summary(pl):	Backend dla aplikacji chemicznych Gnome
Name:		gnome-chemistry-utils
Version:	0.1.3
Release:	1
License:	LGPL
Group:		X11/Applications/Science
Source0:	http://savannah.nongnu.org/download/gchemutils/unstable.pkg/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	0be12cb53fad3ccbb70aaa600da34cf7
URL:		http://www.nongnu.org/gchemutils/
%{?_with_gtkglarea:BuildRequires:	gtkglarea-devel >= 1.99.0}
%{?_with_gtkglarea:BuildConflicts:	gtkglext-devel >= 0.6.0}
%{!?_with_gtkglarea:BuildRequires:	gtkglext-devel >= 0.6.0}
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeprint-devel >= 2.0.0
Obsoletes:	gcu
Obsoletes:	gcu-lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
The Gnome Chemistry Utils provide C++ classes and GTK2 widgets related
to chemistry. They are currently used in Gnome Crystal (gcrystal) and
Gnome Chemistry Paint (gchempaint).

%description -l pl
Gnome Chemistry Utils to zestaw klas C++ i widgetów GTK2 zwi±zanych z
chemi±. Obecnie u¿ywany jest w programach Gnome Crystal (gcrystal) i
Gnome Chemistry Paint (gchempaint).

%package devel
Summary:	Header files for %{name} library
Summary(pl):	Pliki nag³ówkowe %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	gcu-lib-devel

%description devel
The gnome-chemistry-utils-devel package includes the header files
necessary for developing programs using the gnome-chemistry-utils
libraries.

%description devel -l pl
Pakiet gnome-chemistry-utils-devel zawiera pliki nag³ówkowe niezbêdne
do budowania programów u¿ywaj±cych bibliotek gnome-chemistry-utils.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/gchemutils
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/gcu
%{_libdir}/pkgconfig/*.pc
