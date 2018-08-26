; Auto-generated. Do not edit!


(cl:in-package ratslam_ros-msg)


;//! \htmlinclude signalFromCNN.msg.html

(cl:defclass <signalFromCNN> (roslisp-msg-protocol:ros-message)
  ((signalCNN
    :reader signalCNN
    :initarg :signalCNN
    :type cl:float
    :initform 0.0))
)

(cl:defclass signalFromCNN (<signalFromCNN>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <signalFromCNN>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'signalFromCNN)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ratslam_ros-msg:<signalFromCNN> is deprecated: use ratslam_ros-msg:signalFromCNN instead.")))

(cl:ensure-generic-function 'signalCNN-val :lambda-list '(m))
(cl:defmethod signalCNN-val ((m <signalFromCNN>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:signalCNN-val is deprecated.  Use ratslam_ros-msg:signalCNN instead.")
  (signalCNN m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <signalFromCNN>) ostream)
  "Serializes a message object of type '<signalFromCNN>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'signalCNN))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <signalFromCNN>) istream)
  "Deserializes a message object of type '<signalFromCNN>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'signalCNN) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<signalFromCNN>)))
  "Returns string type for a message object of type '<signalFromCNN>"
  "ratslam_ros/signalFromCNN")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'signalFromCNN)))
  "Returns string type for a message object of type 'signalFromCNN"
  "ratslam_ros/signalFromCNN")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<signalFromCNN>)))
  "Returns md5sum for a message object of type '<signalFromCNN>"
  "6affad96707d21429a6e875cadc1f691")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'signalFromCNN)))
  "Returns md5sum for a message object of type 'signalFromCNN"
  "6affad96707d21429a6e875cadc1f691")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<signalFromCNN>)))
  "Returns full string definition for message of type '<signalFromCNN>"
  (cl:format cl:nil "float32 signalCNN~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'signalFromCNN)))
  "Returns full string definition for message of type 'signalFromCNN"
  (cl:format cl:nil "float32 signalCNN~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <signalFromCNN>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <signalFromCNN>))
  "Converts a ROS message object to a list"
  (cl:list 'signalFromCNN
    (cl:cons ':signalCNN (signalCNN msg))
))
