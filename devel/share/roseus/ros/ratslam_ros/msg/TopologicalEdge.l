;; Auto-generated. Do not edit!


(when (boundp 'ratslam_ros::TopologicalEdge)
  (if (not (find-package "RATSLAM_ROS"))
    (make-package "RATSLAM_ROS"))
  (shadow 'TopologicalEdge (find-package "RATSLAM_ROS")))
(unless (find-package "RATSLAM_ROS::TOPOLOGICALEDGE")
  (make-package "RATSLAM_ROS::TOPOLOGICALEDGE"))

(in-package "ROS")
;;//! \htmlinclude TopologicalEdge.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass ratslam_ros::TopologicalEdge
  :super ros::object
  :slots (_id _source_id _destination_id _duration _transform ))

(defmethod ratslam_ros::TopologicalEdge
  (:init
   (&key
    ((:id __id) 0)
    ((:source_id __source_id) 0)
    ((:destination_id __destination_id) 0)
    ((:duration __duration) (instance ros::time :init))
    ((:transform __transform) (instance geometry_msgs::Transform :init))
    )
   (send-super :init)
   (setq _id (round __id))
   (setq _source_id (round __source_id))
   (setq _destination_id (round __destination_id))
   (setq _duration __duration)
   (setq _transform __transform)
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:source_id
   (&optional __source_id)
   (if __source_id (setq _source_id __source_id)) _source_id)
  (:destination_id
   (&optional __destination_id)
   (if __destination_id (setq _destination_id __destination_id)) _destination_id)
  (:duration
   (&optional __duration)
   (if __duration (setq _duration __duration)) _duration)
  (:transform
   (&rest __transform)
   (if (keywordp (car __transform))
       (send* _transform __transform)
     (progn
       (if __transform (setq _transform (car __transform)))
       _transform)))
  (:serialization-length
   ()
   (+
    ;; uint32 _id
    4
    ;; uint32 _source_id
    4
    ;; uint32 _destination_id
    4
    ;; duration _duration
    8
    ;; geometry_msgs/Transform _transform
    (send _transform :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _id
       (write-long _id s)
     ;; uint32 _source_id
       (write-long _source_id s)
     ;; uint32 _destination_id
       (write-long _destination_id s)
     ;; duration _duration
       (write-long (send _duration :sec) s) (write-long (send _duration :nsec) s)
     ;; geometry_msgs/Transform _transform
       (send _transform :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _id
     (setq _id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _source_id
     (setq _source_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint32 _destination_id
     (setq _destination_id (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; duration _duration
     (send _duration :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _duration :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; geometry_msgs/Transform _transform
     (send _transform :deserialize buf ptr-) (incf ptr- (send _transform :serialization-length))
   ;;
   self)
  )

(setf (get ratslam_ros::TopologicalEdge :md5sum-) "c5998f5af8b3f0379746951076b5511a")
(setf (get ratslam_ros::TopologicalEdge :datatype-) "ratslam_ros/TopologicalEdge")
(setf (get ratslam_ros::TopologicalEdge :definition-)
      "uint32 id
uint32 source_id
uint32 destination_id
duration duration
geometry_msgs/Transform transform
================================================================================
MSG: geometry_msgs/Transform
# This represents the transform between two coordinate frames in free space.

Vector3 translation
Quaternion rotation

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :ratslam_ros/TopologicalEdge "c5998f5af8b3f0379746951076b5511a")


