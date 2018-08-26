;; Auto-generated. Do not edit!


(when (boundp 'ratslam_ros::TopologicalAction)
  (if (not (find-package "RATSLAM_ROS"))
    (make-package "RATSLAM_ROS"))
  (shadow 'TopologicalAction (find-package "RATSLAM_ROS")))
(unless (find-package "RATSLAM_ROS::TOPOLOGICALACTION")
  (make-package "RATSLAM_ROS::TOPOLOGICALACTION"))

(in-package "ROS")
;;//! \htmlinclude TopologicalAction.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(intern "*CREATE_NODE*" (find-package "RATSLAM_ROS::TOPOLOGICALACTION"))
(shadow '*CREATE_NODE* (find-package "RATSLAM_ROS::TOPOLOGICALACTION"))
(defconstant ratslam_ros::TopologicalAction::*CREATE_NODE* 1)
(intern "*CREATE_EDGE*" (find-package "RATSLAM_ROS::TOPOLOGICALACTION"))
(shadow '*CREATE_EDGE* (find-package "RATSLAM_ROS::TOPOLOGICALACTION"))
(defconstant ratslam_ros::TopologicalAction::*CREATE_EDGE* 2)
(intern "*SET_NODE*" (find-package "RATSLAM_ROS::TOPOLOGICALACTION"))
(shadow '*SET_NODE* (find-package "RATSLAM_ROS::TOPOLOGICALACTION"))
(defconstant ratslam_ros::TopologicalAction::*SET_NODE* 3)
(defclass ratslam_ros::TopologicalAction
  :super ros::object
  :slots (_header _action _src_id _dest_id _relative_rad ))

(defmethod ratslam_ros::TopologicalAction
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:action __action) 0)
    ((:src_id __src_id) 0)
    ((:dest_id __dest_id) 0)
    ((:relative_rad __relative_rad) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _action (round __action))
   (setq _src_id (round __src_id))
   (setq _dest_id (round __dest_id))
   (setq _relative_rad (float __relative_rad))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:action
   (&optional __action)
   (if __action (setq _action __action)) _action)
  (:src_id
   (&optional __src_id)
   (if __src_id (setq _src_id __src_id)) _src_id)
  (:dest_id
   (&optional __dest_id)
   (if __dest_id (setq _dest_id __dest_id)) _dest_id)
  (:relative_rad
   (&optional __relative_rad)
   (if __relative_rad (setq _relative_rad __relative_rad)) _relative_rad)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint32 _action
    4
    ;; uint32 _src_id
    4
    ;; uint32 _dest_id
    4
    ;; float64 _relative_rad
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint32 _action
       (write-long _action s)
     ;; uint32 _src_id
       (write-long _src_id s)
     ;; uint32 _dest_id
       (write-long _dest_id s)
     ;; float64 _relative_rad
       (sys::poke _relative_rad (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint32 _action
     (setq _action (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _src_id
     (setq _src_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _dest_id
     (setq _dest_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _relative_rad
     (setq _relative_rad (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get ratslam_ros::TopologicalAction :md5sum-) "365d6e23e0fb90a477e21472cd2edf80")
(setf (get ratslam_ros::TopologicalAction :datatype-) "ratslam_ros/TopologicalAction")
(setf (get ratslam_ros::TopologicalAction :definition-)
      "# actions
uint32 CREATE_NODE=1
uint32 CREATE_EDGE=2
uint32 SET_NODE=3

Header header

uint32 action

uint32 src_id
uint32 dest_id

float64 relative_rad


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

")



(provide :ratslam_ros/TopologicalAction "365d6e23e0fb90a477e21472cd2edf80")


