%bcond_without mysql
%bcond_without sqlite3
%bcond_without postgresql
%bcond_without odbc

%define major 3
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	C++ Database Access Library
Name:		soci
Version:	3.2.3
Release:	1
License:	MIT
Group:		Development/Databases
URL:		http://soci.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	boost-devel
%if %{with_sqlite3}
BuildRequires:	sqlite3-devel
%endif
%if %{with_postgresql}
BuildRequires:	postgresql-devel
%endif
%if %{with_mysql}
BuildRequires:	mysql-devel
%endif
%if %{with_odbc}
BuildRequires:	unixODBC-devel
%endif
Source0:	http://downloads.sourceforge.net/project/soci/%{name}/%{name}-%{version}/%{name}-%{version}.zip
Patch0:		%{name}-3.2.3-fix-type.patch

%description
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

PostgreSQL, Firebird, MySQL, SQLite are supported databases.

%files
%doc README.md AUTHORS CHANGES LICENSE_1_0.txt

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
%doc doc/

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
%{_libdir}/libsoci_*.so
%{_libdir}/libsoci_*.a
%{_includedir}/soci

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
%cmake \
	-DSOCI_EMPTY:BOOL=OFF \
%if %{with_mysql}
	-DSOCI_MYSQL:BOOL=ON \
%else
	-DSOCI_MYSQL:BOOL=OFF \
%endif
%if %{with_odbc}
	-DSOCI_ODBC:BOOL=ON \
%else
	-DSOCI_ODBC:BOOL=OFF \
%endif
%if %{with_postgresql}
	-DSOCI_POSTGRESQL:BOOL=ON \
%else
	-DSOCI_POSTGRESQL:BOOL=OFF \
%endif
%if %{with_sqlite3}
	-DSOCI_SQLITE3:BOOL=ON
%else
	-DSOCI_SQLITE3:BOOL=OFF
%endif

%make

%install
%makeinstall_std -C build

