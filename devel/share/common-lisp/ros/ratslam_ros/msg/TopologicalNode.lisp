; Auto-generated. Do not edit!


(cl:in-package ratslam_ros-msg)


;//! \htmlinclude TopologicalNode.msg.html

(cl:defclass <TopologicalNode> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:integer
    :initform 0)
   (pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose)))
)

(cl:defclass TopologicalNode (<TopologicalNode>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <TopologicalNode>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'TopologicalNode)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ratslam_ros-msg:<TopologicalNode> is deprecated: use ratslam_ros-msg:TopologicalNode instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <TopologicalNode>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:id-val is deprecated.  Use ratslam_ros-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <TopologicalNode>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:pose-val is deprecated.  Use ratslam_ros-msg:pose instead.")
  (pose m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <TopologicalNode>) ostream)
  "Serializes a message object of type '<TopologicalNode>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'id)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'id)) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <TopologicalNode>) istream)
  "Deserializes a message object of type '<TopologicalNode>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) (cl:slot-value msg 'id)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) (cl:slot-value msg 'id)) (cl:read-byte istream))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<TopologicalNode>)))
  "Returns string type for a message object of type '<TopologicalNode>"
  "ratslam_ros/TopologicalNode")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'TopologicalNode)))
  "Returns string type for a message object of type 'TopologicalNode"
  "ratslam_ros/TopologicalNode")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<TopologicalNode>)))
  "Returns md5sum for a message object of type '<TopologicalNode>"
  "9ad7ea65113411e05ab5cf09fc962a2d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'TopologicalNode)))
  "Returns md5sum for a message object of type 'TopologicalNode"
  "9ad7ea65113411e05ab5cf09fc962a2d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<TopologicalNode>)))
  "Returns full string definition for message of type '<TopologicalNode>"
  (cl:format cl:nil "uint32 id~%geometry_msgs/Pose pose~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'TopologicalNode)))
  "Returns full string definition for message of type 'TopologicalNode"
  (cl:format cl:nil "uint32 id~%geometry_msgs/Pose pose~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <TopologicalNode>))
  (cl:+ 0
     4
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <TopologicalNode>))
  "Converts a ROS message object to a list"
  (cl:list 'TopologicalNode
    (cl:cons ':id (id msg))
    (cl:cons ':pose (pose msg))
))
