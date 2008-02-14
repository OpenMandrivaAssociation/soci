%define build_mysql		1
%define build_sqlite3		1
%define build_postgresql	1
%define build_firebird		1

%{?_with_mysql: %{expand: %%global build_mysql 1}}
%{?_without_mysql: %{expand: %%global build_mysql 0}}

%{?_with_sqlite3: %{expand: %%global build_sqlite3 1}}
%{?_without_sqlite3: %{expand: %%global build_sqlite3 0}}

%{?_with_postgresql: %{expand: %%global build_postgresql 1}}
%{?_without_postgresql: %{expand: %%global build_postgresql 0}}

%{?_with_firebird: %{expand: %%global build_firebird 1}}
%{?_without_firebird: %{expand: %%global build_firebird 0}}

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
%if %{build_sqlite3}
BuildRequires:	libsqlite3-devel
Requires:	%{libname}-sqlite3
%endif
%if %{build_postgresql}
BuildRequires:	postgresql-devel
Requires:	%{libname}-postgresql
%endif
%if %{build_firebird}
BuildRequires:	firebird-devel
Requires:	%{libname}-firebird
%endif
%if %{build_mysql}
BuildRequires:	libmysql-devel
Requires:	%{libname}-mysql
%endif
Source:		%{name}-%{version}.tar.bz2
Patch0:		soci-2.2.0_sqlite_fix.patch

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

%if %{build_sqlite3}
%package -n %{libname}-sqlite3
Summary:	Soci sqlite3 backend
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
Group:		Development/Databases

%package -n %{libname}-sqlite3-devel
Summary:	Soci sqlite3 backend development files
Requires:	%{libname}-sqlite3, %{libname}-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-sqlite3-devel = %{version}-%{release}
Group:		Development/Databases
%endif

%if %{build_postgresql}
%package -n %{libname}-postgresql
Summary:	Soci postgresql backend
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
Group:		Development/Databases

%package -n %{libname}-postgresql-devel
Summary:	Soci postgresql backend development files
Requires:	%{libname}-postgresql, %{libname}-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-postgresql-devel = %{version}-%{release}
Group:		Development/Databases
%endif

%if %{build_firebird}
%package -n %{libname}-firebird
Summary:	Soci firebird backend
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
Group:		Development/Databases

%package -n %{libname}-firebird-devel
Summary:	Soci firebird backend development files
Requires:	%{libname}-firebird, %{libname}-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-firebird-devel = %{version}-%{release}
Group:		Development/Databases
%endif

%if %{build_mysql}
%package -n %{libname}-mysql
Summary:	Soci mysql backend
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name} = %{version}-%{release}
Group:		Development/Databases

%package -n %{libname}-mysql-devel
Summary:	Soci mysql backend development files
Requires:	%{libname}-mysql, %{libname}-devel
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-mysql-devel = %{version}-%{release}
Group:		Development/Databases
%endif

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

%if %{build_sqlite3}
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

%endif
%if %{build_postgresql}
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

%endif
%if %{build_firebird}
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

%endif
%if %{build_mysql}
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

%endif
%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%configure \
%if %{build_firebird}
	--enable-backend-firebird=yes \
%endif
%if %{build_mysql}
	--enable-backend-mysql=yes \
%endif
%if %{build_postgresql}
	--enable-backend-postgresql=yes \
%endif
%if %{build_sqlite3}
	--enable-backend-sqlite3=yes
%endif
%make


%install
%makeinstall

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%if %{build_sqlite3}
%post -n %{libname}-sqlite3 -p /sbin/ldconfig
%postun -n %{libname}-sqlite3 -p /sbin/ldconfig
%endif
%if %{build_postgresql}
%post -n %{libname}-postgresql -p /sbin/ldconfig
%postun -n %{libname}-postgresql -p /sbin/ldconfig
%endif
%if %{build_firebird}
%post -n %{libname}-firebird -p /sbin/ldconfig
%postun -n %{libname}-firebird -p /sbin/ldconfig
%endif
%if %{build_mysql}
%post -n %{libname}-mysql -p /sbin/ldconfig
%postun -n %{libname}-mysql -p /sbin/ldconfig
%endif

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

%if %{build_sqlite3}
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
%endif

%if %{build_postgresql}
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
%endif

%if %{build_firebird}
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
%endif

%if %{build_mysql}
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
%endif

