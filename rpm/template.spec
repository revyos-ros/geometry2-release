%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/iron/.*$
%global __requires_exclude_from ^/opt/ros/iron/.*$

Name:           ros-iron-tf2
Version:        0.31.5
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS tf2 package

License:        BSD
URL:            http://www.ros.org/wiki/tf2
Source0:        %{name}-%{version}.tar.gz

Requires:       console-bridge-devel
Requires:       ros-iron-builtin-interfaces
Requires:       ros-iron-console-bridge-vendor
Requires:       ros-iron-geometry-msgs
Requires:       ros-iron-rcutils
Requires:       ros-iron-rosidl-runtime-cpp
Requires:       ros-iron-ros-workspace
BuildRequires:  console-bridge-devel
BuildRequires:  ros-iron-ament-cmake
BuildRequires:  ros-iron-ament-cmake-ros
BuildRequires:  ros-iron-builtin-interfaces
BuildRequires:  ros-iron-console-bridge-vendor
BuildRequires:  ros-iron-geometry-msgs
BuildRequires:  ros-iron-rcutils
BuildRequires:  ros-iron-rosidl-runtime-cpp
BuildRequires:  ros-iron-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-iron-ament-cmake-copyright
BuildRequires:  ros-iron-ament-cmake-cppcheck
BuildRequires:  ros-iron-ament-cmake-cpplint
BuildRequires:  ros-iron-ament-cmake-gtest
BuildRequires:  ros-iron-ament-cmake-lint-cmake
BuildRequires:  ros-iron-ament-cmake-uncrustify
BuildRequires:  ros-iron-ament-cmake-xmllint
%endif

%description
tf2 is the second generation of the transform library, which lets the user keep
track of multiple coordinate frames over time. tf2 maintains the relationship
between coordinate frames in a tree structure buffered in time, and lets the
user transform points, vectors, etc between any two coordinate frames at any
desired point in time.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/iron" \
    -DAMENT_PREFIX_PATH="/opt/ros/iron" \
    -DCMAKE_PREFIX_PATH="/opt/ros/iron" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/iron/setup.sh" ]; then . "/opt/ros/iron/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/iron

%changelog
* Fri Sep 08 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.31.5-1
- Autogenerated by Bloom

* Fri Jul 14 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.31.4-1
- Autogenerated by Bloom

* Thu May 11 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.31.3-1
- Autogenerated by Bloom

* Thu Apr 20 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.31.2-2
- Autogenerated by Bloom

* Thu Apr 13 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.31.2-1
- Autogenerated by Bloom

* Wed Apr 12 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.31.1-1
- Autogenerated by Bloom

* Tue Apr 11 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.31.0-1
- Autogenerated by Bloom

* Tue Mar 21 2023 Alejandro Hernandez Cordero <alejandro@openrobotics.org> - 0.30.0-3
- Autogenerated by Bloom

