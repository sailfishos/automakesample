Name:       automakesample

Summary:    Sample Automake-based library
Version:    0.1
Release:    1
Group:      Development/Libraries
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
Sample Automake-based library

%package devel
Summary:    Header files and libraries for sample Automake-based library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The automakesample-devel package contains the header files and libraries needed
to use the sample Automake-based library.

%prep
%setup -q -n %{name}-%{version}

%build
if ! test -f Makefile; then
    %reconfigure
fi
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
%{_libdir}/libautomakesample.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libautomakesample.so
%{_libdir}/pkgconfig/automakesample.pc
%{_includedir}/automakesample.h
