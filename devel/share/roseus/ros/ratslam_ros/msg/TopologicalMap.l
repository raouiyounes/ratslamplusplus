;; Auto-generated. Do not edit!


(when (boundp 'ratslam_ros::TopologicalMap)
  (if (not (find-package "RATSLAM_ROS"))
    (make-package "RATSLAM_ROS"))
  (shadow 'TopologicalMap (find-package "RATSLAM_ROS")))
(unless (find-package "RATSLAM_ROS::TOPOLOGICALMAP")
  (make-package "RATSLAM_ROS::TOPOLOGICALMAP"))

(in-package "ROS")
;;//! \htmlinclude TopologicalMap.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass ratslam_ros::TopologicalMap
  :super ros::object
  :slots (_header _node_count _node _edge_count _edge ))

(defmethod ratslam_ros::TopologicalMap
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:node_count __node_count) 0)
    ((:node __node) (let (r) (dotimes (i 0) (push (instance ratslam_ros::TopologicalNode :init) r)) r))
    ((:edge_count __edge_count) 0)
    ((:edge __edge) (let (r) (dotimes (i 0) (push (instance ratslam_ros::TopologicalEdge :init) r)) r))
    )
   (send-super :init)
   (setq _header __header)
   (setq _node_count (round __node_count))
   (setq _node __node)
   (setq _edge_count (round __edge_count))
   (setq _edge __edge)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:node_count
   (&optional __node_count)
   (if __node_count (setq _node_count __node_count)) _node_count)
  (:node
   (&rest __node)
   (if (keywordp (car __node))
       (send* _node __node)
     (progn
       (if __node (setq _node (car __node)))
       _node)))
  (:edge_count
   (&optional __edge_count)
   (if __edge_count (setq _edge_count __edge_count)) _edge_count)
  (:edge
   (&rest __edge)
   (if (keywordp (car __edge))
       (send* _edge __edge)
     (progn
       (if __edge (setq _edge (car __edge)))
       _edge)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint32 _node_count
    4
    ;; ratslam_ros/TopologicalNode[] _node
    (apply #'+ (send-all _node :serialization-length)) 4
    ;; uint32 _edge_count
    4
    ;; ratslam_ros/TopologicalEdge[] _edge
    (apply #'+ (send-all _edge :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint32 _node_count
       (write-long _node_count s)
     ;; ratslam_ros/TopologicalNode[] _node
     (write-long (length _node) s)
     (dolist (elem _node)
       (send elem :serialize s)
       )
     ;; uint32 _edge_count
       (write-long _edge_count s)
     ;; ratslam_ros/TopologicalEdge[] _edge
     (write-long (length _edge) s)
     (dolist (elem _edge)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint32 _node_count
     (setq _node_count (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; ratslam_ros/TopologicalNode[] _node
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _node (let (r) (dotimes (i n) (push (instance ratslam_ros::TopologicalNode :init) r)) r))
     (dolist (elem- _node)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; uint32 _edge_count
     (setq _edge_count (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; ratslam_ros/TopologicalEdge[] _edge
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _edge (let (r) (dotimes (i n) (push (instance ratslam_ros::TopologicalEdge :init) r)) r))
     (dolist (elem- _edge)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get ratslam_ros::TopologicalMap :md5sum-) "deefb2c5a22caaa16af4e1b64a821bdc")
(setf (get ratslam_ros::TopologicalMap :datatype-) "ratslam_ros/TopologicalMap")
(setf (get ratslam_ros::TopologicalMap :definition-)
      "Header header
uint32 node_count
TopologicalNode[] node
uint32 edge_count
TopologicalEdge[] edge

	

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: ratslam_ros/TopologicalNode
uint32 id
geometry_msgs/Pose pose
================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: ratslam_ros/TopologicalEdge
uint32 id
uint32 source_id
uint32 destination_id
duration duration
geometry_msgs/Transform transform
================================================================================
MSG: geometry_msgs/Transform
# This represents the transform between two coordinate frames in free space.

Vector3 translation
Quaternion rotation

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
")



(provide :ratslam_ros/TopologicalMap "deefb2c5a22caaa16af4e1b64a821bdc")


