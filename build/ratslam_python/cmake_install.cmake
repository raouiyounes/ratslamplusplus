# Install script for directory: /home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/younes/eclipse-workspace/Hamburg_Lim/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ratslam_ros/msg" TYPE FILE FILES
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/NodeExampleData.msg"
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalAction.msg"
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg"
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalMap.msg"
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg"
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/ViewTemplate.msg"
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/VisualObjet.msg"
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/signalFromCNN.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ratslam_ros/cmake" TYPE FILE FILES "/home/younes/eclipse-workspace/Hamburg_Lim/build/ratslam_python/catkin_generated/installspace/ratslam_ros-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/younes/eclipse-workspace/Hamburg_Lim/devel/include/ratslam_ros")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/younes/eclipse-workspace/Hamburg_Lim/devel/share/roseus/ros/ratslam_ros")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/younes/eclipse-workspace/Hamburg_Lim/devel/share/common-lisp/ros/ratslam_ros")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/younes/eclipse-workspace/Hamburg_Lim/devel/share/gennodejs/ros/ratslam_ros")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/younes/eclipse-workspace/Hamburg_Lim/devel/lib/python2.7/dist-packages/ratslam_ros")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/younes/eclipse-workspace/Hamburg_Lim/devel/lib/python2.7/dist-packages/ratslam_ros")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/ratslam_ros" TYPE FILE FILES "/home/younes/eclipse-workspace/Hamburg_Lim/devel/include/ratslam_ros/ratslam_rosConfig.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/ratslam_ros" TYPE FILE FILES "/home/younes/eclipse-workspace/Hamburg_Lim/devel/lib/python2.7/dist-packages/ratslam_ros/__init__.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/younes/eclipse-workspace/Hamburg_Lim/devel/lib/python2.7/dist-packages/ratslam_ros/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/ratslam_ros" TYPE DIRECTORY FILES "/home/younes/eclipse-workspace/Hamburg_Lim/devel/lib/python2.7/dist-packages/ratslam_ros/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/younes/eclipse-workspace/Hamburg_Lim/build/ratslam_python/catkin_generated/installspace/ratslam_ros.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ratslam_ros/cmake" TYPE FILE FILES "/home/younes/eclipse-workspace/Hamburg_Lim/build/ratslam_python/catkin_generated/installspace/ratslam_ros-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ratslam_ros/cmake" TYPE FILE FILES
    "/home/younes/eclipse-workspace/Hamburg_Lim/build/ratslam_python/catkin_generated/installspace/ratslam_rosConfig.cmake"
    "/home/younes/eclipse-workspace/Hamburg_Lim/build/ratslam_python/catkin_generated/installspace/ratslam_rosConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ratslam_ros" TYPE FILE FILES "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libratslam.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libratslam.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libratslam.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE SHARED_LIBRARY FILES "/home/younes/eclipse-workspace/Hamburg_Lim/devel/lib/libratslam.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libratslam.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libratslam.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/libratslam.so")
    endif()
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ratslam_ros/ratslam_pc" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ratslam_ros/ratslam_pc")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ratslam_ros/ratslam_pc"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ratslam_ros" TYPE EXECUTABLE FILES "/home/younes/eclipse-workspace/Hamburg_Lim/devel/lib/ratslam_ros/ratslam_pc")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ratslam_ros/ratslam_pc" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ratslam_ros/ratslam_pc")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ratslam_ros/ratslam_pc"
         OLD_RPATH "/opt/ros/kinetic/lib:/home/younes/eclipse-workspace/Hamburg_Lim/devel/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/ratslam_ros/ratslam_pc")
    endif()
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/ratslam_ros" TYPE PROGRAM FILES
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/src/main_lv.py"
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/src/main_pc.py"
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/src/ratslam/posecell_networkv_pointer.py"
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/src/main_em.py"
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/src/ratslam/posecell_networkv.py"
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/src/ratslam/experience_map_younes.py"
    "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/src/ratslam/EM_Objects.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ratslam_ros" TYPE DIRECTORY FILES "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/launch")
endif()

