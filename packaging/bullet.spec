#sbs-git:slp/unmodified/libbullet bullet 2.77 ef5f1217bdb947807e117963430e967f0360817a
Name: libbullet
Version: 2.80
Release: 1
Summary: Bullet Continuous Collision Detection and Physics Library
License: Zlib
Group: TO_BE/FILLED_IN
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
  
  
%post -p /sbin/ldconfig  
%postun -p /sbin/ldconfig  
  
  
%files  
%defattr(-,root,root,-)  
/usr/lib/libBulletCollision.so.2.80
/usr/lib/libBulletDynamics.so.2.80
/usr/lib/libBulletMultiThreaded.so.2.80
/usr/lib/libBulletSoftBody.so.2.80
/usr/lib/libBulletSoftBodySolvers_OpenCL_Mini.so.2.80
/usr/lib/libLinearMath.so.2.80
/usr/lib/libMiniCL.so.2.80
 
  
%files devel  
%defattr(-,root,root,-)  
/usr/include/bullet/*.h
/usr/include/bullet/*/*/*/*.h
/usr/include/bullet/*/*/*.h
/usr/include/bullet/*/*.h
/usr/lib/libBulletCollision.so
/usr/lib/libBulletDynamics.so
/usr/lib/libBulletMultiThreaded.so
/usr/lib/libBulletSoftBody.so
/usr/lib/libBulletSoftBodySolvers_OpenCL_Mini.so
/usr/lib/libLinearMath.so
/usr/lib/libMiniCL.so
/usr/lib/pkgconfig/bullet.pc
