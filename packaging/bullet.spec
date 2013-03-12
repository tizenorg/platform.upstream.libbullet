#sbs-git:slp/unmodified/libbullet bullet 2.77 ef5f1217bdb947807e117963430e967f0360817a
Name: libbullet
Version: 2.80
Release: 3
Summary: Bullet Continuous Collision Detection and Physics Library
License: Zlib
Group: System/Libraries
Source: %{name}-%{version}.tar.gz 
BuildRequires: cmake 
#BuildRequires: pkgconfig(opengl-es-11)
#BuildRequires: pkgconfig(opengl-es-20)

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
  
cmake . -G "Unix Makefiles" -DBUILD_SHARED_LIBS=ON -DBUILD_EXTRAS=OFF -DBUILD_DEMOS=OFF -DBUILD_CPU_DEMOS=OFF -DUSE_GRAPHICAL_BENCHMARK=OFF -DCMAKE_INSTALL_PREFIX=/usr -DUSE_GLUT=OFF

make %{?jobs:-j%jobs}  
  
%install  
rm -rf %{buildroot}  
%make_install
mkdir -p %{buildroot}/%{_datadir}/license
cp -rf %{_builddir}/%{name}-%{version}/packaging/bullet %{buildroot}/%{_datadir}/license

  
%post -p /sbin/ldconfig  
%postun -p /sbin/ldconfig  
  
  
%files  
%manifest bullet.manifest
%defattr(-,root,root,-)  
%{_libdir}/*.so.%{version}
%{_datadir}/license/bullet
  
%files devel  
%defattr(-,root,root,-)  
%{_includedir}/bullet/*.h
%{_includedir}/bullet/*/*/*/*.h
%{_includedir}/bullet/*/*/*.h
%{_includedir}/bullet/*/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
