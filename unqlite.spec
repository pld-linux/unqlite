Summary:	An Embeddable NoSQL Database Engine
Name:		unqlite
Version:	1.1.6
Release:	1
License:	BSD
Group:		Libraries
# Source0Download: http://unqlite.org/downloads.html
Source0:	http://unqlite.org/db/%{name}-db-20130825-116.zip
# Source0-md5:	a48b7409414cc4a9ff8f7ccce81f40c5
URL:		http://unqlite.org/
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		soname libunqlite.so.0

%description
UnQLite is a in-process software library which implements a
self-contained, serverless, zero-configuration, transactional NoSQL
database engine. UnQLite is a document store database similar to
MongoDB, Redis, CouchDB etc. as well a standard Key/Value store
similar to BerkeleyDB, LevelDB, etc.

%package devel
Summary:	Header file for UnQLite development
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for UnQLite development.

%prep
%setup -qc

%build
%{__cc} %{rpmcppflags} %{rpmcflags} -c unqlite.c -fPIC
%{__cc} %{rpmldflags} -Wl,-soname,%{soname} -shared *.o -o %{soname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}
cp -p unqlite.h $RPM_BUILD_ROOT%{_includedir}
install -p %{soname} $RPM_BUILD_ROOT%{_libdir}
ln -s %{soname} $RPM_BUILD_ROOT%{_libdir}/libunqlite.so

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc license.txt
%attr(755,root,root) %{_libdir}/libunqlite.so.0

%files devel
%defattr(644,root,root,755)
%{_includedir}/unqlite.h
%{_libdir}/libunqlite.so
