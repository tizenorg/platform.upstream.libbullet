Name: bullet
Version: 2.81
Release: 0
Summary: Bullet Continuous Collision Detection and Physics Library
License: Zlib
Group: System/Libraries
Source: %{name}-%{version}.tar.gz 
BuildRequires: cmake 
Source1001:     bullet.manifest

%description
Bullet Continuous Collision Detection and Physics Library

%package -n libbullet
Summary: Bullet Continuous Collision Detection and Physics Library
Group: System/Libraries

%description -n libbullet
Bullet Continuous Collision Detection and Physics Library
  
%package devel  
Summary:    Development components for the bullet
Group:      Development/Libraries  
Requires:   libbullet = %{version}-%{release}  
  
%description devel  
Bullet Continuous Collision Detection and Physics Library (devel) 
  
%prep  
%setup -q
cp %{SOURCE1001} .
  
%build  
  
%cmake . -G "Unix Makefiles" -DBUILD_SHARED_LIBS=ON -DBUILD_EXTRAS=OFF -DBUILD_DEMOS=OFF -DBUILD_CPU_DEMOS=OFF -DUSE_GRAPHICAL_BENCHMARK=OFF -DCMAKE_INSTALL_PREFIX=/usr -DUSE_GLUT=OFF

make %{?jobs:-j%jobs}  
  
%install  
%make_install
  
%post -p /sbin/ldconfig   -n libbullet

%postun -p /sbin/ldconfig  -n libbullet
  
%files -n libbullet  
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root,-)  
%{_libdir}/*.so.%{version}
  
%files devel  
%manifest %{name}.manifest
%defattr(-,root,root,-)  
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
