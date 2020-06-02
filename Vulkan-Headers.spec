#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Vulkan-Headers
Version  : 1.2.142
Release  : 44
URL      : https://github.com/KhronosGroup/Vulkan-Headers/archive/v1.2.142/Vulkan-Headers-1.2.142.tar.gz
Source0  : https://github.com/KhronosGroup/Vulkan-Headers/archive/v1.2.142/Vulkan-Headers-1.2.142.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: Vulkan-Headers-data = %{version}-%{release}
Requires: Vulkan-Headers-license = %{version}-%{release}
BuildRequires : buildreq-cmake

%description
# Vulkan-Headers
Vulkan header files and API registry
## Repository Content
The contents of this repository are largely obtained from other repositories and are
collected, coordinated, and curated here.

%package data
Summary: data components for the Vulkan-Headers package.
Group: Data

%description data
data components for the Vulkan-Headers package.


%package dev
Summary: dev components for the Vulkan-Headers package.
Group: Development
Requires: Vulkan-Headers-data = %{version}-%{release}
Provides: Vulkan-Headers-devel = %{version}-%{release}
Requires: Vulkan-Headers = %{version}-%{release}

%description dev
dev components for the Vulkan-Headers package.


%package license
Summary: license components for the Vulkan-Headers package.
Group: Default

%description license
license components for the Vulkan-Headers package.


%prep
%setup -q -n Vulkan-Headers-1.2.142
cd %{_builddir}/Vulkan-Headers-1.2.142

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591116555
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1591116555
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Vulkan-Headers
cp %{_builddir}/Vulkan-Headers-1.2.142/LICENSE.txt %{buildroot}/usr/share/package-licenses/Vulkan-Headers/2b8b815229aa8a61e483fb4ba0588b8b6c491890
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/vulkan/registry/cgenerator.py
/usr/share/vulkan/registry/conventions.py
/usr/share/vulkan/registry/generator.py
/usr/share/vulkan/registry/genvk.py
/usr/share/vulkan/registry/reg.py
/usr/share/vulkan/registry/spec_tools/util.py
/usr/share/vulkan/registry/validusage.json
/usr/share/vulkan/registry/vk.xml
/usr/share/vulkan/registry/vkconventions.py

%files dev
%defattr(-,root,root,-)
/usr/include/vulkan/vk_icd.h
/usr/include/vulkan/vk_layer.h
/usr/include/vulkan/vk_platform.h
/usr/include/vulkan/vk_sdk_platform.h
/usr/include/vulkan/vulkan.h
/usr/include/vulkan/vulkan.hpp
/usr/include/vulkan/vulkan_android.h
/usr/include/vulkan/vulkan_beta.h
/usr/include/vulkan/vulkan_core.h
/usr/include/vulkan/vulkan_fuchsia.h
/usr/include/vulkan/vulkan_ggp.h
/usr/include/vulkan/vulkan_ios.h
/usr/include/vulkan/vulkan_macos.h
/usr/include/vulkan/vulkan_metal.h
/usr/include/vulkan/vulkan_vi.h
/usr/include/vulkan/vulkan_wayland.h
/usr/include/vulkan/vulkan_win32.h
/usr/include/vulkan/vulkan_xcb.h
/usr/include/vulkan/vulkan_xlib.h
/usr/include/vulkan/vulkan_xlib_xrandr.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Vulkan-Headers/2b8b815229aa8a61e483fb4ba0588b8b6c491890
