#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stdint.h>

// ROS
#include <ros/ros.h>
#include <sensor_msgs/CompressedImage.h>
#include <sensor_msgs/Image.h>                // image message
#include <image_transport/image_transport.h>  // handles raw or compressed images
#include <cv_bridge/cv_bridge.h>              // publishing image
#include <geometry_msgs/Pose.h>               // pose message
#include <tf/transform_broadcaster.h>         // publishing transforms
#include <geometry_msgs/TransformStamped.h>   // transform message

// Lib Viso2
#include <viso_mono.h>

// OpenCV
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

VisualOdometryMono *viso = NULL;
Mat traj = Mat::zeros(500, 700, CV_8UC3);
Matrix pose = Matrix::eye(4);
ofstream fichier1, fichier2;
int in = 0;
int CAMERA_HZ = 10;
double rot_rad = 0.0;
double tran_x = 0.0;
double tran_y = 0.0;
double x = 0.0, y = 0.0;

double clip_rad_180(double angle) {
    while (angle > CV_PI)
        angle -= 2*CV_PI;
    while (angle <= -CV_PI)
        angle += 2*CV_PI;
  return angle;
}

void show_trajectory(Matrix C) {
	int x = 650 + int(C.val[0][3]);
    	int y = 200 - int(C.val[2][3]);
    	circle(traj, Point(x, y) ,1, CV_RGB(255,255,255), 1);
	circle(traj, Point(650,200), 3, CV_RGB(255, 100, 100), 1);
    	putText(traj, "START", Point(630, 240), FONT_HERSHEY_PLAIN, 1, CV_RGB(250,200,200), 1, 8);
    	imshow( "Trajectory", traj);
    	waitKey(1);
}

void print__() {
        double num_matches = viso->getNumberOfMatches();
        double num_inliers = viso->getNumberOfInliers();
        std::cout << ", Matches: " << num_matches;
        std::cout << ", Inliers: " << 100.0*num_inliers/num_matches << " %" << ", Current pose: " << std::endl;
        std::cout << pose << std::endl << std::endl;
	x = x + pose.val[0][3];
	y = y + pose.val[2][3];
        fichier1 << in << " " << pose.val[0][3] << " " << pose.val[2][3] << " " << x << " " << y << endl;
	show_trajectory(pose);
}

void image_callback(const sensor_msgs::ImageConstPtr& msg) {

    uint8_t *image_data;
    cv_bridge::CvImageConstPtr cv_ptr_clr,cv_ptr;
    try {
        cv_ptr_clr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);
	cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::MONO8);
    }
    catch (cv_bridge::Exception& error) {
	ROS_ERROR("error");
	return;
    }
    image_data = (uint8_t *)cv_ptr->image.data;
    int32_t dims[3] = {(int32_t)msg->width, (int32_t)msg->height, (int32_t)msg->width};

    // find motion
    bool ok = viso->process(cv_ptr_clr->image, image_data, dims);	
    // update pose and publish only if process() was successful
    if(ok) {
	Matrix T = viso->getMotion();
	pose = pose * Matrix::inv(T);
	rot_rad = clip_rad_180(asin(T.val[0][2]));
	tran_x = T.val[0][3];
tran_y = T.val[2][3];
	print__();
    }
    fichier2 << in << "\t" << tran_x << "\t" << tran_y << "\t" << rot_rad << endl;
    in++;
}

int main (int argc, char** argv) {

    ROS_INFO_STREAM("\t MONOCULAR VISUAL ODOMETRY \n");

    // need the topic
    if (argc < 2) {
       ROS_FATAL_STREAM("USAGE: " << argv[0] << " <topic_name>");
exit(-1);
    }
    
    ros::init(argc, argv, "RatSLAMMonocularVisualOdometry");
    ros::NodeHandle node;
