# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "ratslam_ros: 8 messages, 0 services")

set(MSG_I_FLAGS "-Iratslam_ros:/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(ratslam_ros_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/VisualObjet.msg" NAME_WE)
add_custom_target(_ratslam_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ratslam_ros" "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/VisualObjet.msg" ""
)

get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/signalFromCNN.msg" NAME_WE)
add_custom_target(_ratslam_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ratslam_ros" "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/signalFromCNN.msg" ""
)

get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg" NAME_WE)
add_custom_target(_ratslam_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ratslam_ros" "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg" "geometry_msgs/Quaternion:geometry_msgs/Transform:geometry_msgs/Vector3"
)

get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalAction.msg" NAME_WE)
add_custom_target(_ratslam_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ratslam_ros" "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalAction.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/NodeExampleData.msg" NAME_WE)
add_custom_target(_ratslam_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ratslam_ros" "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/NodeExampleData.msg" ""
)

get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg" NAME_WE)
add_custom_target(_ratslam_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ratslam_ros" "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg" "geometry_msgs/Quaternion:geometry_msgs/Pose:geometry_msgs/Point"
)

get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/ViewTemplate.msg" NAME_WE)
add_custom_target(_ratslam_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ratslam_ros" "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/ViewTemplate.msg" "std_msgs/Header"
)

get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalMap.msg" NAME_WE)
add_custom_target(_ratslam_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "ratslam_ros" "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalMap.msg" "std_msgs/Header:geometry_msgs/Quaternion:ratslam_ros/TopologicalNode:geometry_msgs/Vector3:geometry_msgs/Point:geometry_msgs/Transform:ratslam_ros/TopologicalEdge:geometry_msgs/Pose"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/VisualObjet.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_cpp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/signalFromCNN.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_cpp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_cpp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_cpp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/NodeExampleData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_cpp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_cpp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/ViewTemplate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_cpp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalMap.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ratslam_ros
)

### Generating Services

### Generating Module File
_generate_module_cpp(ratslam_ros
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ratslam_ros
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(ratslam_ros_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(ratslam_ros_generate_messages ratslam_ros_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/VisualObjet.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_cpp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/signalFromCNN.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_cpp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_cpp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalAction.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_cpp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/NodeExampleData.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_cpp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_cpp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/ViewTemplate.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_cpp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalMap.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_cpp _ratslam_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ratslam_ros_gencpp)
add_dependencies(ratslam_ros_gencpp ratslam_ros_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ratslam_ros_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/VisualObjet.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ratslam_ros
)
_generate_msg_eus(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/signalFromCNN.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ratslam_ros
)
_generate_msg_eus(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ratslam_ros
)
_generate_msg_eus(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ratslam_ros
)
_generate_msg_eus(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/NodeExampleData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ratslam_ros
)
_generate_msg_eus(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ratslam_ros
)
_generate_msg_eus(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/ViewTemplate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ratslam_ros
)
_generate_msg_eus(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalMap.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ratslam_ros
)

### Generating Services

### Generating Module File
_generate_module_eus(ratslam_ros
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ratslam_ros
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(ratslam_ros_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(ratslam_ros_generate_messages ratslam_ros_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/VisualObjet.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_eus _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/signalFromCNN.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_eus _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_eus _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalAction.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_eus _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/NodeExampleData.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_eus _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_eus _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/ViewTemplate.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_eus _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalMap.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_eus _ratslam_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ratslam_ros_geneus)
add_dependencies(ratslam_ros_geneus ratslam_ros_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ratslam_ros_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/VisualObjet.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_lisp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/signalFromCNN.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_lisp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_lisp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_lisp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/NodeExampleData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_lisp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_lisp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/ViewTemplate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ratslam_ros
)
_generate_msg_lisp(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalMap.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ratslam_ros
)

### Generating Services

### Generating Module File
_generate_module_lisp(ratslam_ros
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ratslam_ros
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(ratslam_ros_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(ratslam_ros_generate_messages ratslam_ros_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/VisualObjet.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_lisp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/signalFromCNN.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_lisp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_lisp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalAction.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_lisp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/NodeExampleData.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_lisp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_lisp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/ViewTemplate.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_lisp _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalMap.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_lisp _ratslam_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ratslam_ros_genlisp)
add_dependencies(ratslam_ros_genlisp ratslam_ros_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ratslam_ros_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/VisualObjet.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ratslam_ros
)
_generate_msg_nodejs(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/signalFromCNN.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ratslam_ros
)
_generate_msg_nodejs(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ratslam_ros
)
_generate_msg_nodejs(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ratslam_ros
)
_generate_msg_nodejs(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/NodeExampleData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ratslam_ros
)
_generate_msg_nodejs(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ratslam_ros
)
_generate_msg_nodejs(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/ViewTemplate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ratslam_ros
)
_generate_msg_nodejs(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalMap.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ratslam_ros
)

### Generating Services

### Generating Module File
_generate_module_nodejs(ratslam_ros
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ratslam_ros
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(ratslam_ros_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(ratslam_ros_generate_messages ratslam_ros_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/VisualObjet.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_nodejs _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/signalFromCNN.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_nodejs _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_nodejs _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalAction.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_nodejs _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/NodeExampleData.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_nodejs _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_nodejs _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/ViewTemplate.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_nodejs _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalMap.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_nodejs _ratslam_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ratslam_ros_gennodejs)
add_dependencies(ratslam_ros_gennodejs ratslam_ros_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ratslam_ros_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/VisualObjet.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ratslam_ros
)
_generate_msg_py(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/signalFromCNN.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ratslam_ros
)
_generate_msg_py(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ratslam_ros
)
_generate_msg_py(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalAction.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ratslam_ros
)
_generate_msg_py(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/NodeExampleData.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ratslam_ros
)
_generate_msg_py(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ratslam_ros
)
_generate_msg_py(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/ViewTemplate.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ratslam_ros
)
_generate_msg_py(ratslam_ros
  "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalMap.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Transform.msg;/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ratslam_ros
)

### Generating Services

### Generating Module File
_generate_module_py(ratslam_ros
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ratslam_ros
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(ratslam_ros_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(ratslam_ros_generate_messages ratslam_ros_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/VisualObjet.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_py _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/signalFromCNN.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_py _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalEdge.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_py _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalAction.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_py _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/NodeExampleData.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_py _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalNode.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_py _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/ViewTemplate.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_py _ratslam_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/younes/eclipse-workspace/Hamburg_Lim/src/ratslam_python/msg/TopologicalMap.msg" NAME_WE)
add_dependencies(ratslam_ros_generate_messages_py _ratslam_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(ratslam_ros_genpy)
add_dependencies(ratslam_ros_genpy ratslam_ros_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS ratslam_ros_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ratslam_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/ratslam_ros
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(ratslam_ros_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(ratslam_ros_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ratslam_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/ratslam_ros
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(ratslam_ros_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(ratslam_ros_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ratslam_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/ratslam_ros
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(ratslam_ros_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(ratslam_ros_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ratslam_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/ratslam_ros
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(ratslam_ros_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(ratslam_ros_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ratslam_ros)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ratslam_ros\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/ratslam_ros
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(ratslam_ros_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(ratslam_ros_generate_messages_py std_msgs_generate_messages_py)
endif()
