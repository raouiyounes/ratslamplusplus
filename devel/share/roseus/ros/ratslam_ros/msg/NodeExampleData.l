;; Auto-generated. Do not edit!


(when (boundp 'ratslam_ros::NodeExampleData)
  (if (not (find-package "RATSLAM_ROS"))
    (make-package "RATSLAM_ROS"))
  (shadow 'NodeExampleData (find-package "RATSLAM_ROS")))
(unless (find-package "RATSLAM_ROS::NODEEXAMPLEDATA")
  (make-package "RATSLAM_ROS::NODEEXAMPLEDATA"))

(in-package "ROS")
;;//! \htmlinclude NodeExampleData.msg.html


(defclass ratslam_ros::NodeExampleData
  :super ros::object
  :slots (_message _a _b ))

(defmethod ratslam_ros::NodeExampleData
  (:init
   (&key
    ((:message __message) "")
    ((:a __a) 0)
    ((:b __b) 0)
    )
   (send-super :init)
   (setq _message (string __message))
   (setq _a (round __a))
   (setq _b (round __b))
   self)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:b
   (&optional __b)
   (if __b (setq _b __b)) _b)
  (:serialization-length
   ()
   (+
    ;; string _message
    4 (length _message)
    ;; int32 _a
    4
    ;; int32 _b
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;; int32 _a
       (write-long _a s)
     ;; int32 _b
       (write-long _b s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32 _a
     (setq _a (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _b
     (setq _b (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get ratslam_ros::NodeExampleData :md5sum-) "3192b76bfe6df73dcca63fc0aa4efaf9")
(setf (get ratslam_ros::NodeExampleData :datatype-) "ratslam_ros/NodeExampleData")
(setf (get ratslam_ros::NodeExampleData :definition-)
      "string message
int32 a
int32 b

")



(provide :ratslam_ros/NodeExampleData "3192b76bfe6df73dcca63fc0aa4efaf9")


