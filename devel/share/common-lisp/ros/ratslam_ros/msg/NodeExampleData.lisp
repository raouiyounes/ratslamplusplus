; Auto-generated. Do not edit!


(cl:in-package ratslam_ros-msg)


;//! \htmlinclude NodeExampleData.msg.html

(cl:defclass <NodeExampleData> (roslisp-msg-protocol:ros-message)
  ((message
    :reader message
    :initarg :message
    :type cl:string
    :initform "")
   (a
    :reader a
    :initarg :a
    :type cl:integer
    :initform 0)
   (b
    :reader b
    :initarg :b
    :type cl:integer
    :initform 0))
)

(cl:defclass NodeExampleData (<NodeExampleData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <NodeExampleData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'NodeExampleData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ratslam_ros-msg:<NodeExampleData> is deprecated: use ratslam_ros-msg:NodeExampleData instead.")))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <NodeExampleData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:message-val is deprecated.  Use ratslam_ros-msg:message instead.")
  (message m))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <NodeExampleData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:a-val is deprecated.  Use ratslam_ros-msg:a instead.")
  (a m))

(cl:ensure-generic-function 'b-val :lambda-list '(m))
(cl:defmethod b-val ((m <NodeExampleData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:b-val is deprecated.  Use ratslam_ros-msg:b instead.")
  (b m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <NodeExampleData>) ostream)
  "Serializes a message object of type '<NodeExampleData>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
  (cl:let* ((signed (cl:slot-value msg 'a)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'b)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <NodeExampleData>) istream)
  "Deserializes a message object of type '<NodeExampleData>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'a) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'b) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<NodeExampleData>)))
  "Returns string type for a message object of type '<NodeExampleData>"
  "ratslam_ros/NodeExampleData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'NodeExampleData)))
  "Returns string type for a message object of type 'NodeExampleData"
  "ratslam_ros/NodeExampleData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<NodeExampleData>)))
  "Returns md5sum for a message object of type '<NodeExampleData>"
  "3192b76bfe6df73dcca63fc0aa4efaf9")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'NodeExampleData)))
  "Returns md5sum for a message object of type 'NodeExampleData"
  "3192b76bfe6df73dcca63fc0aa4efaf9")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<NodeExampleData>)))
  "Returns full string definition for message of type '<NodeExampleData>"
  (cl:format cl:nil "string message~%int32 a~%int32 b~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'NodeExampleData)))
  "Returns full string definition for message of type 'NodeExampleData"
  (cl:format cl:nil "string message~%int32 a~%int32 b~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <NodeExampleData>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'message))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <NodeExampleData>))
  "Converts a ROS message object to a list"
  (cl:list 'NodeExampleData
    (cl:cons ':message (message msg))
    (cl:cons ':a (a msg))
    (cl:cons ':b (b msg))
))
