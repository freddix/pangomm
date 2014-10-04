%include	/usr/lib/rpm/macros.perl

Summary:	A C++ interface for pango library
Name:		pangomm
Version:	2.34.0
Release:	2
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/pangomm/2.34/%{name}-%{version}.tar.xz
# Source0-md5:	2c702caede167323c9ed9eed2b933098
URL:		http://gtkmm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cairomm-devel
BuildRequires:	glibmm-devel
BuildRequires:	libsigc++-devel
BuildRequires:	libtool
BuildRequires:	mm-common
BuildRequires:	pango-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver	1.4

%description
A C++ interface for pango library.

%package devel
Summary:	Header files for glibmm library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	gtkmm-pango-devel

%description devel
Header files for pangomm library.

%package apidocs
Summary:	Reference documentation and examples for pangomm
Group:		Documentation

%description apidocs
Reference documentation and examples for pangomm.

%prep
%setup -q

%build
mm-common-prepare
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install	\
	DESTDIR=$RPM_BUILD_ROOT	\
	libdocdir=%{_gtkdocdir}/pangomm-%{apiver}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libpangomm*.so.?
%attr(755,root,root) %{_libdir}/libpangomm*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpangomm*.so
%{_libdir}/pangomm-%{apiver}
%{_pkgconfigdir}/pangomm*.pc
%{_includedir}/pangomm-%{apiver}

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}-%{apiver}

