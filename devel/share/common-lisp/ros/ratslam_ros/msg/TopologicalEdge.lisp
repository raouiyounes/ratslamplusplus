; Auto-generated. Do not edit!


(cl:in-package ratslam_ros-msg)


;//! \htmlinclude TopologicalEdge.msg.html

(cl:defclass <TopologicalEdge> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0)
   (source_id
    :reader source_id
    :initarg :source_id
    :type cl:integer
    :initform 0)
   (destination_id
    :reader destination_id
    :initarg :destination_id
    :type cl:integer
    :initform 0)
   (duration
    :reader duration
    :initarg :duration
    :type cl:real
    :initform 0)
   (transform
    :reader transform
    :initarg :transform
    :type geometry_msgs-msg:Transform
    :initform (cl:make-instance 'geometry_msgs-msg:Transform)))
)

(cl:defclass TopologicalEdge (<TopologicalEdge>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TopologicalEdge>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TopologicalEdge)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ratslam_ros-msg:<TopologicalEdge> is deprecated: use ratslam_ros-msg:TopologicalEdge instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <TopologicalEdge>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:id-val is deprecated.  Use ratslam_ros-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'source_id-val :lambda-list '(m))
(cl:defmethod source_id-val ((m <TopologicalEdge>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:source_id-val is deprecated.  Use ratslam_ros-msg:source_id instead.")
  (source_id m))

(cl:ensure-generic-function 'destination_id-val :lambda-list '(m))
(cl:defmethod destination_id-val ((m <TopologicalEdge>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:destination_id-val is deprecated.  Use ratslam_ros-msg:destination_id instead.")
  (destination_id m))

(cl:ensure-generic-function 'duration-val :lambda-list '(m))
(cl:defmethod duration-val ((m <TopologicalEdge>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:duration-val is deprecated.  Use ratslam_ros-msg:duration instead.")
  (duration m))

(cl:ensure-generic-function 'transform-val :lambda-list '(m))
(cl:defmethod transform-val ((m <TopologicalEdge>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:transform-val is deprecated.  Use ratslam_ros-msg:transform instead.")
  (transform m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TopologicalEdge>) ostream)
  "Serializes a message object of type '<TopologicalEdge>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'source_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'source_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'source_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'source_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'destination_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'destination_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'destination_id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'destination_id)) ostream)
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'duration)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'duration) (cl:floor (cl:slot-value msg 'duration)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'transform) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TopologicalEdge>) istream)
  "Deserializes a message object of type '<TopologicalEdge>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'source_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'source_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'source_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'source_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'destination_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'destination_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'destination_id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'destination_id)) (cl:read-byte istream))
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'duration) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'transform) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TopologicalEdge>)))
  "Returns string type for a message object of type '<TopologicalEdge>"
  "ratslam_ros/TopologicalEdge")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TopologicalEdge)))
  "Returns string type for a message object of type 'TopologicalEdge"
  "ratslam_ros/TopologicalEdge")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TopologicalEdge>)))
  "Returns md5sum for a message object of type '<TopologicalEdge>"
  "c5998f5af8b3f0379746951076b5511a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TopologicalEdge)))
  "Returns md5sum for a message object of type 'TopologicalEdge"
  "c5998f5af8b3f0379746951076b5511a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TopologicalEdge>)))
  "Returns full string definition for message of type '<TopologicalEdge>"
  (cl:format cl:nil "uint32 id~%uint32 source_id~%uint32 destination_id~%duration duration~%geometry_msgs/Transform transform~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TopologicalEdge)))
  "Returns full string definition for message of type 'TopologicalEdge"
  (cl:format cl:nil "uint32 id~%uint32 source_id~%uint32 destination_id~%duration duration~%geometry_msgs/Transform transform~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TopologicalEdge>))
  (cl:+ 0
     4
     4
     4
     8
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'transform))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TopologicalEdge>))
  "Converts a ROS message object to a list"
  (cl:list 'TopologicalEdge
    (cl:cons ':id (id msg))
    (cl:cons ':source_id (source_id msg))
    (cl:cons ':destination_id (destination_id msg))
    (cl:cons ':duration (duration msg))
    (cl:cons ':transform (transform msg))
))
