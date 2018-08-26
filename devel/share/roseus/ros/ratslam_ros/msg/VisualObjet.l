;; Auto-generated. Do not edit!


(when (boundp 'ratslam_ros::VisualObjet)
  (if (not (find-package "RATSLAM_ROS"))
    (make-package "RATSLAM_ROS"))
  (shadow 'VisualObjet (find-package "RATSLAM_ROS")))
(unless (find-package "RATSLAM_ROS::VISUALOBJET")
  (make-package "RATSLAM_ROS::VISUALOBJET"))

(in-package "ROS")
;;//! \htmlinclude VisualObjet.msg.html


(defclass ratslam_ros::VisualObjet
  :super ros::object
  :slots (_x _y _label ))

(defmethod ratslam_ros::VisualObjet
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:label __label) 0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _label (round __label))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:label
   (&optional __label)
   (if __label (setq _label __label)) _label)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; uint8 _label
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; uint8 _label
       (write-byte _label s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; uint8 _label
     (setq _label (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get ratslam_ros::VisualObjet :md5sum-) "817923b48e2ccfeef3b9d7bf797a5e39")
(setf (get ratslam_ros::VisualObjet :datatype-) "ratslam_ros/VisualObjet")
(setf (get ratslam_ros::VisualObjet :definition-)
      "float64 x
float64 y
uint8 label

")



(provide :ratslam_ros/VisualObjet "817923b48e2ccfeef3b9d7bf797a5e39")


