; Auto-generated. Do not edit!


(cl:in-package ratslam_ros-msg)


;//! \htmlinclude TopologicalAction.msg.html

(cl:defclass <TopologicalAction> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (action
    :reader action
    :initarg :action
    :type cl:integer
    :initform 0)
   (src_id
    :reader src_id
    :initarg :src_id
    :type cl:integer
    :initform 0)
   (dest_id
    :reader dest_id
    :initarg :dest_id
    :type cl:integer
    :initform 0)
   (relative_rad
    :reader relative_rad
    :initarg :relative_rad
    :type cl:float
    :initform 0.0))
)

(cl:defclass TopologicalAction (<TopologicalAction>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TopologicalAction>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TopologicalAction)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ratslam_ros-msg:<TopologicalAction> is deprecated: use ratslam_ros-msg:TopologicalAction instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <TopologicalAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:header-val is deprecated.  Use ratslam_ros-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'action-val :lambda-list '(m))
(cl:defmethod action-val ((m <TopologicalAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:action-val is deprecated.  Use ratslam_ros-msg:action instead.")
  (action m))

(cl:ensure-generic-function 'src_id-val :lambda-list '(m))
(cl:defmethod src_id-val ((m <TopologicalAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:src_id-val is deprecated.  Use ratslam_ros-msg:src_id instead.")
  (src_id m))

(cl:ensure-generic-function 'dest_id-val :lambda-list '(m))
(cl:defmethod dest_id-val ((m <TopologicalAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:dest_id-val is deprecated.  Use ratslam_ros-msg:dest_id instead.")
  (dest_id m))

(cl:ensure-generic-function 'relative_rad-val :lambda-list '(m))
(cl:defmethod relative_rad-val ((m <TopologicalAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:relative_rad-val is deprecated.  Use ratslam_ros-msg:relative_rad instead.")
  (relative_rad m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<TopologicalAction>)))
    "Constants for message type '<TopologicalAction>"
  '((:CREATE_NODE . 1)
    (:CREATE_EDGE . 2)
    (:SET_NODE . 3))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'TopologicalAction)))
    "Constants for message type 'TopologicalAction"
  '((:CREATE_NODE . 1)
    (:CREATE_EDGE . 2)
    (:SET_NODE . 3))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TopologicalAction>) ostream)
  "Serializes a message object of type '<TopologicalAction>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'action)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'action)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'action)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'action)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'src_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'src_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'src_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'src_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dest_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'dest_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'dest_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'dest_id)) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'relative_rad))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TopologicalAction>) istream)
  "Deserializes a message object of type '<TopologicalAction>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'action)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'action)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'action)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'action)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'src_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'src_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'src_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'src_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'dest_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'dest_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'dest_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'dest_id)) (cl:read-byte istream))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'relative_rad) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TopologicalAction>)))
  "Returns string type for a message object of type '<TopologicalAction>"
  "ratslam_ros/TopologicalAction")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TopologicalAction)))
  "Returns string type for a message object of type 'TopologicalAction"
  "ratslam_ros/TopologicalAction")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TopologicalAction>)))
  "Returns md5sum for a message object of type '<TopologicalAction>"
  "365d6e23e0fb90a477e21472cd2edf80")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TopologicalAction)))
  "Returns md5sum for a message object of type 'TopologicalAction"
  "365d6e23e0fb90a477e21472cd2edf80")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TopologicalAction>)))
  "Returns full string definition for message of type '<TopologicalAction>"
  (cl:format cl:nil "# actions~%uint32 CREATE_NODE=1~%uint32 CREATE_EDGE=2~%uint32 SET_NODE=3~%~%Header header~%~%uint32 action~%~%uint32 src_id~%uint32 dest_id~%~%float64 relative_rad~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TopologicalAction)))
  "Returns full string definition for message of type 'TopologicalAction"
  (cl:format cl:nil "# actions~%uint32 CREATE_NODE=1~%uint32 CREATE_EDGE=2~%uint32 SET_NODE=3~%~%Header header~%~%uint32 action~%~%uint32 src_id~%uint32 dest_id~%~%float64 relative_rad~%~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TopologicalAction>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
     4
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TopologicalAction>))
  "Converts a ROS message object to a list"
  (cl:list 'TopologicalAction
    (cl:cons ':header (header msg))
    (cl:cons ':action (action msg))
    (cl:cons ':src_id (src_id msg))
    (cl:cons ':dest_id (dest_id msg))
    (cl:cons ':relative_rad (relative_rad msg))
))
