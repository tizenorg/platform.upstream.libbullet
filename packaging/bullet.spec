Name: bullet
Version: 2.81
Release: 0
Summary: Bullet Continuous Collision Detection and Physics Library
License: Zlib
Group: System/Libraries
Source: %{name}-%{version}.tar.gz 
BuildRequires: cmake 

%description
Bullet Continuous Collision Detection and Physics Library

%package -n libbullet
Summary: Bullet Continuous Collision Detection and Physics Library
Group: System/Libraries

%description
Bullet Continuous Collision Detection and Physics Library
  
%package devel  
Summary:    Development components for the bullet
Group:      Development/Libraries  
Requires:   %{name} = %{version}-%{release}  
  
%description devel  
Bullet Continuous Collision Detection and Physics Library (devel) 
  
%prep  
%setup -q
  
%build  
  
%cmake . -G "Unix Makefiles" -DBUILD_SHARED_LIBS=ON -DBUILD_EXTRAS=OFF -DBUILD_DEMOS=OFF -DBUILD_CPU_DEMOS=OFF -DUSE_GRAPHICAL_BENCHMARK=OFF -DCMAKE_INSTALL_PREFIX=/usr -DUSE_GLUT=OFF

make %{?jobs:-j%jobs}  
  
%install  
%make_install
  
%post -p /sbin/ldconfig  

%postun -p /sbin/ldconfig  
  
  
%files -n libbullet  
%manifest bullet.manifest
%license COPYING
%defattr(-,root,root,-)  
%{_libdir}/*.so.%{version}
  
%files devel  
%defattr(-,root,root,-)  
%{_includedir}/bullet/*.h
%{_includedir}/bullet/*/*/*/*.h
%{_includedir}/bullet/*/*/*.h
%{_includedir}/bullet/*/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
