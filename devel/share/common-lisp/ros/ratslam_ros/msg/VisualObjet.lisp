; Auto-generated. Do not edit!


(cl:in-package ratslam_ros-msg)


;//! \htmlinclude VisualObjet.msg.html

(cl:defclass <VisualObjet> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (label
    :reader label
    :initarg :label
    :type cl:fixnum
    :initform 0))
)

(cl:defclass VisualObjet (<VisualObjet>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <VisualObjet>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'VisualObjet)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name ratslam_ros-msg:<VisualObjet> is deprecated: use ratslam_ros-msg:VisualObjet instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <VisualObjet>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:x-val is deprecated.  Use ratslam_ros-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <VisualObjet>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:y-val is deprecated.  Use ratslam_ros-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'label-val :lambda-list '(m))
(cl:defmethod label-val ((m <VisualObjet>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader ratslam_ros-msg:label-val is deprecated.  Use ratslam_ros-msg:label instead.")
  (label m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <VisualObjet>) ostream)
  "Serializes a message object of type '<VisualObjet>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'label)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <VisualObjet>) istream)
  "Deserializes a message object of type '<VisualObjet>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'label)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<VisualObjet>)))
  "Returns string type for a message object of type '<VisualObjet>"
  "ratslam_ros/VisualObjet")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'VisualObjet)))
  "Returns string type for a message object of type 'VisualObjet"
  "ratslam_ros/VisualObjet")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<VisualObjet>)))
  "Returns md5sum for a message object of type '<VisualObjet>"
  "817923b48e2ccfeef3b9d7bf797a5e39")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'VisualObjet)))
  "Returns md5sum for a message object of type 'VisualObjet"
  "817923b48e2ccfeef3b9d7bf797a5e39")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<VisualObjet>)))
  "Returns full string definition for message of type '<VisualObjet>"
  (cl:format cl:nil "float64 x~%float64 y~%uint8 label~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'VisualObjet)))
  "Returns full string definition for message of type 'VisualObjet"
  (cl:format cl:nil "float64 x~%float64 y~%uint8 label~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <VisualObjet>))
  (cl:+ 0
     8
     8
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <VisualObjet>))
  "Converts a ROS message object to a list"
  (cl:list 'VisualObjet
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':label (label msg))
))
