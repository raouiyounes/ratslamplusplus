;; Auto-generated. Do not edit!


(when (boundp 'ratslam_ros::signalFromCNN)
  (if (not (find-package "RATSLAM_ROS"))
    (make-package "RATSLAM_ROS"))
  (shadow 'signalFromCNN (find-package "RATSLAM_ROS")))
(unless (find-package "RATSLAM_ROS::SIGNALFROMCNN")
  (make-package "RATSLAM_ROS::SIGNALFROMCNN"))

(in-package "ROS")
;;//! \htmlinclude signalFromCNN.msg.html


(defclass ratslam_ros::signalFromCNN
  :super ros::object
  :slots (_signalCNN ))

(defmethod ratslam_ros::signalFromCNN
  (:init
   (&key
    ((:signalCNN __signalCNN) 0.0)
    )
   (send-super :init)
   (setq _signalCNN (float __signalCNN))
   self)
  (:signalCNN
   (&optional __signalCNN)
   (if __signalCNN (setq _signalCNN __signalCNN)) _signalCNN)
  (:serialization-length
   ()
   (+
    ;; float32 _signalCNN
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _signalCNN
       (sys::poke _signalCNN (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _signalCNN
     (setq _signalCNN (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get ratslam_ros::signalFromCNN :md5sum-) "6affad96707d21429a6e875cadc1f691")
(setf (get ratslam_ros::signalFromCNN :datatype-) "ratslam_ros/signalFromCNN")
(setf (get ratslam_ros::signalFromCNN :definition-)
      "float32 signalCNN
")



(provide :ratslam_ros/signalFromCNN "6affad96707d21429a6e875cadc1f691")


