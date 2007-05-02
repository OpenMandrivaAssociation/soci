%define name soci
%define libname %{mklibname %name}
%define version 2.2.0
%define release %mkrel 1

Summary:	C++ Database Access Library
Name:		%name
Version:	%version
Release:	%release
BuildRoot:	%{_tmppath}/%{name}-root
License:	BSD Style
Group:		Development/Databases
URL:		http://soci.sourceforge.net/
BuildRequires:	libsqlite3-devel, postgresql-devel, firebird-devel, libmysql-devel
Requires:	%{libname}-sqlite3, %{libname}-postgresql, %{libname}-mysql, %{libname}-firebird
Source:		%{name}-%{version}.tar.bz2

%description
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

PostgreSQL, Firebird, MySQL, SQLite are supported databases.

%package doc
Summary:	Documentation for SOCI
Group:		Development/Databases

%package -n %{libname}
Summary:	C++ Database Access Library
Group:		Development/Databases

%package -n %{libname}-devel
Summary:	C++ Database Access Library development files
Requires:	%{libname}
Group:		Development/Databases

%package -n %{libname}-sqlite3
Summary:	soci sqlite3 backend
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
Group:		Development/Databases

%package -n %{libname}-sqlite3-devel
Summary:	soci sqlite3 backend development files
Requires:	%{libname}-sqlite3, %{libname}-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-sqlite3-devel = %{version}-%{release}
Group:		Development/Databases

%package -n %{libname}-postgresql
Summary:	soci postgresql backend
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
Group:		Development/Databases

%package -n %{libname}-postgresql-devel
Summary:	soci postgresql backend development files
Requires:	%{libname}-postgresql, %{libname}-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-postgresql-devel = %{version}-%{release}
Group:		Development/Databases

%package -n %{libname}-firebird
Summary:	soci firebird backend
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
Group:		Development/Databases

%package -n %{libname}-firebird-devel
Summary:	soci firebird backend development files
Requires:	%{libname}-firebird, %{libname}-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-firebird-devel = %{version}-%{release}
Group:		Development/Databases

%package -n %{libname}-mysql
Summary:	soci mysql backend
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
Group:		Development/Databases

%package -n %{libname}-mysql-devel
Summary:	soci mysql backend development files
Requires:	%{libname}-mysql, %{libname}-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-mysql-devel = %{version}-%{release}
Group:		Development/Databases

%description doc
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

This package is the documentation.

%description -n %{libname}
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

PostgreSQL, Firebird, MySQL, SQLite are supported databases.

%description -n %{libname}-devel
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

This package contains development files.

%description -n %{libname}-sqlite3
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

This package is for the SQLite3 backend.

%description -n %{libname}-sqlite3-devel
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

This package is for the SQLite3 backend development files.

%description -n %{libname}-postgresql
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

This package is for the PostgreSQL backend.

%description -n %{libname}-postgresql-devel
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

This package is for the PostgreSQL backend development files.

%description -n %{libname}-firebird
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

This package is for the firebird backend.

%description -n %{libname}-firebird-devel
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

This package is for the firebird backend development files.

%description -n %{libname}-mysql
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

This package is for the MySQL backend.

%description -n %{libname}-mysql-devel
SOCI is a database access library for C++ that makes the illusion of
embedding SQL queries in the regular C++ code, staying entirely within
the Standard C++.

This package is for the MySQL backend development files.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --enable-backend-firebird=yes --enable-backend-mysql=yes --enable-backend-postgresql=yes --enable-backend-sqlite3=yes

%install
%makeinstall

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%post -n %{libname}-sqlite3 -p /sbin/ldconfig
%postun -n %{libname}-sqlite3 -p /sbin/ldconfig
%post -n %{libname}-postgresql -p /sbin/ldconfig
%postun -n %{libname}-postgresql -p /sbin/ldconfig
%post -n %{libname}-firebird -p /sbin/ldconfig
%postun -n %{libname}-firebird -p /sbin/ldconfig
%post -n %{libname}-mysql -p /sbin/ldconfig
%postun -n %{libname}-mysql -p /sbin/ldconfig

%clean
%{__rm} -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc README CHANGES LICENSE_1_0.txt

%files doc
%defattr(-,root,root)
%doc doc/

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libsoci_core-gcc-2_2-%{version}.so

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/libsoci_core-gcc-2_2.a
%{_libdir}/libsoci_core-gcc-2_2.la
%{_libdir}/libsoci_core-gcc-2_2.so
%{_includedir}/soci/empty/soci-empty.h
%{_includedir}/soci/soci-backend.h
%{_includedir}/soci/soci-config.h
%{_includedir}/soci/soci-platform.h
%{_includedir}/soci/soci.h

%files -n %{libname}-sqlite3
%defattr(-,root,root)
%{_libdir}/libsoci_sqlite3-gcc-2_2-%{version}.so

%files -n %{libname}-sqlite3-devel
%defattr(-,root,root)
%{_libdir}/libsoci_sqlite3-gcc-2_2.a
%{_libdir}/libsoci_sqlite3-gcc-2_2.la
%{_libdir}/libsoci_sqlite3-gcc-2_2.so
%{_includedir}/soci/sqlite3/common.h
%{_includedir}/soci/sqlite3/soci-sqlite3.h

%files -n %{libname}-postgresql
%defattr(-,root,root)
%{_libdir}/libsoci_postgresql-gcc-2_2-%{version}.so

%files -n %{libname}-postgresql-devel
%defattr(-,root,root)
%{_libdir}/libsoci_postgresql-gcc-2_2.a
%{_libdir}/libsoci_postgresql-gcc-2_2.la
%{_libdir}/libsoci_postgresql-gcc-2_2.so
%{_includedir}/soci/postgresql/common.h
%{_includedir}/soci/postgresql/soci-postgresql.h

%files -n %{libname}-firebird
%defattr(-,root,root)
%{_libdir}/libsoci_firebird-gcc-2_2-%{version}.so

%files -n %{libname}-firebird-devel
%defattr(-,root,root)
%{_libdir}/libsoci_firebird-gcc-2_2.a
%{_libdir}/libsoci_firebird-gcc-2_2.la
%{_libdir}/libsoci_firebird-gcc-2_2.so
%{_includedir}/soci/firebird/common.h
%{_includedir}/soci/firebird/error.h
%{_includedir}/soci/firebird/soci-firebird.h

%files -n %{libname}-mysql
%defattr(-,root,root)
%{_libdir}/libsoci_mysql-gcc-2_2-%{version}.so

%files -n %{libname}-mysql-devel
%defattr(-,root,root)
%{_libdir}/libsoci_mysql-gcc-2_2.a
%{_libdir}/libsoci_mysql-gcc-2_2.la
%{_libdir}/libsoci_mysql-gcc-2_2.so
%{_includedir}/soci/mysql/common.h
%{_includedir}/soci/mysql/soci-mysql.h

