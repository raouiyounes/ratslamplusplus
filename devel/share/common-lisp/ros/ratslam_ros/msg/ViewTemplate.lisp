; Auto-generated. Do not edit!


(cl:in-package ratslam_ros-msg)


;//! \htmlinclude ViewTemplate.msg.html

(cl:defclass <ViewTemplate> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (current_id
    :reader current_id
    :initarg :current_id
    :type cl:integer
    :initform 0)
   (relative_rad
    :reader relative_rad
    :initarg :relative_rad
    :type cl:float
    :initform 0.0))
)

(cl:defclass ViewTemplate (<ViewTemplate>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ViewTemplate>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ViewTemplate)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ratslam_ros-msg:<ViewTemplate> is deprecated: use ratslam_ros-msg:ViewTemplate instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ViewTemplate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:header-val is deprecated.  Use ratslam_ros-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'current_id-val :lambda-list '(m))
(cl:defmethod current_id-val ((m <ViewTemplate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:current_id-val is deprecated.  Use ratslam_ros-msg:current_id instead.")
  (current_id m))

(cl:ensure-generic-function 'relative_rad-val :lambda-list '(m))
(cl:defmethod relative_rad-val ((m <ViewTemplate>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:relative_rad-val is deprecated.  Use ratslam_ros-msg:relative_rad instead.")
  (relative_rad m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ViewTemplate>) ostream)
  "Serializes a message object of type '<ViewTemplate>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'current_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'current_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'current_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'current_id)) ostream)
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ViewTemplate>) istream)
  "Deserializes a message object of type '<ViewTemplate>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'current_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'current_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'current_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'current_id)) (cl:read-byte istream))
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ViewTemplate>)))
  "Returns string type for a message object of type '<ViewTemplate>"
  "ratslam_ros/ViewTemplate")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ViewTemplate)))
  "Returns string type for a message object of type 'ViewTemplate"
  "ratslam_ros/ViewTemplate")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ViewTemplate>)))
  "Returns md5sum for a message object of type '<ViewTemplate>"
  "a3978e682f73dc18ef3727352b92d92e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ViewTemplate)))
  "Returns md5sum for a message object of type 'ViewTemplate"
  "a3978e682f73dc18ef3727352b92d92e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ViewTemplate>)))
  "Returns full string definition for message of type '<ViewTemplate>"
  (cl:format cl:nil "Header header~%~%uint32 current_id~%float64 relative_rad~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ViewTemplate)))
  "Returns full string definition for message of type 'ViewTemplate"
  (cl:format cl:nil "Header header~%~%uint32 current_id~%float64 relative_rad~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ViewTemplate>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ViewTemplate>))
  "Converts a ROS message object to a list"
  (cl:list 'ViewTemplate
    (cl:cons ':header (header msg))
    (cl:cons ':current_id (current_id msg))
    (cl:cons ':relative_rad (relative_rad msg))
))
