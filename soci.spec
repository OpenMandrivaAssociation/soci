%bcond_without empty
%bcond_without odbc
%bcond_without postgresql
%bcond_without mysql
%bcond_without sqlite3

%define major 4
%define minor 0
%define patch 2
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:		C++ Database Access Library
Name:			soci
Version:		%{major}.%{minor}.%{patch}
Release:		1
License:		MIT
Group:			Development/Databases
URL:			http://soci.sourceforge.net/
Source0:		http://downloads.sourceforge.net/project/soci/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel
%if %{with_sqlite3}
BuildRequires:	pkgconfig(sqlite3)
%endif
%if %{with_postgresql}
BuildRequires:	pkgconfig(libpgtypes)
%endif
%if %{with_mysql}
BuildRequires:	pkgconfig(mariadb)
%endif
%if %{with_odbc}
BuildRequires:	pkgconfig(odbc)
%endif

%description
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

PostgreSQL, Firebird, MySQL, SQLite are supported databases.

%files
%doc README.md AUTHORS
%license LICENSE_1_0.txt

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for SOCI
Group:		Development/Databases

%description doc
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

This package is the documentation.

%files doc
%doc docs/

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	C++ Database Access Libraries
Group:		Development/Databases

%description -n %{libname}
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

PostgreSQL, MySQL, SQLite are supported databases.

%files -n %{libname}
%{_libdir}/libsoci_*.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	C++ Database Access Library development files
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}
Group:		Development/Databases

%description -n %{devname}
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

This package contains development files.

%files -n %{devname}
%{_libdir}/lib%{name}_*.so
%{_includedir}/%{name}
%{_libdir}/cmake/SOCI

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%cmake \
	-DSOCI_STATIC:BOOL=OFF \
	-DSOCI_EMPTY:BOOL==%{?with_empty:ON}%{?without_empty:OFF} \
	-DSOCI_MYSQL:BOOL=%{?with_mysql:ON}%{?without_mysql:OFF} \
	-DSOCI_ODBC:BOOL=%{?with_odbc:ON}%{?without_odbc:OFF} \
	-DSOCI_POSTGRESQL:BOOL==%{?with_postgresql:ON}%{?without_postgresql:OFF} \
	-DSOCI_SQLITE3:BOOL=%{?with_sqlite3:ON}%{?without_sqlite3:OFF} \
	-G Ninja
%ninja_build

%install
%ninja_install -C build

# fix cmake path
install -dm 0755 %{buildroot}%{_datadir}/cmake/%{name}
mv -f %{buildroot}%{_prefix}/cmake %{buildroot}%{_datadir}/cmake/%{name}

