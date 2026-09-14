
Ros notes [notes](https://app.notion.com/p/Ros2-Notes-3b4d1244b87f8098bd5bdc5268838718?source=copy_link) provided by sir 


**setup.py** :- configure package installation and executable paths .

**colcon build** :- compiles workspace and creates symbolic links for python  code .

**source/install/setup.bash** :- loads workspace executable into terminal context

**ros2 run <pkg> <exec>** :- started a ROS2 node executable process


# Understanding the ROS 2 Build Command

      ros2 has dds(data distributed service) while ros1 hasn't

The command `colcon build --symlink-install --packages-select my_pkg` is used to compile and configure your ROS 2 workspace package efficiently.

## Breakdown of Each Part

1. **`colcon`**
   - The official build tool used in ROS 2 (short for *collective construction*). It handles building code and organizing the workspace structure.

2. **`build`**
   - The verb command telling colcon to build the packages found in your workspace's `src` folder.

3. **`--symlink-install`**
   - A major developer time-saver. Instead of copying Python scripts and configuration files into the `install` folder during every build, it creates symbolic links (shortcuts). 
   - **Benefit:** You can edit your Python source files (`talker.py`, `listener.py`) and test them immediately without re-running `colcon build`.

4. **`--packages-select my_pkg`**
   - Instructs colcon to compile **only** the specified package (`my_pkg`) rather than scanning and building every package in your entire workspace.



# build command
* ament
* colcon  

## ament function

it is only use for source folder 
* cmd for installation of ament function (first start server using cmd  source /opt/ros/jazzy/setup.bash , then ) - 

ros2 pkg create --build-type ament_python my_pkg


## colcon function 
it is used to create workspace automatically but it doesn't create src 

command use for build/compilation :- colcon build --packages-select <my_pkg>


# open cv (computer vision module ) working steps 
* ## image acquisition 

capture raw visual data using digital sensors , cameras or medical scanners.
convert the visual scene into a digital image format made of pixels.

*  ## image preprocessing 
 
* ## feature extarction

* ## data capturing

* ## action / output

# node 

 
# Topic

It provides a medium / channel

# 
**publisher** :- can connect only one node at a time

**subscriber** :- can connect to multiple node at a single time 


# URDF fundamentals 

URDF = unified robot description format 

URDF is an XML based format ros2 uses to model a robot as a tree of link connected by joints . it's not simulation soecific .Rviz use it for visualization , gazebo 

      aisa robot jo multiple nodes se milke bana ho , 
## cmd for udrf 

* check_urdf  
* joint_state_publisher 
* lf2_echo
* robot_state_publisher
* view_frames

# Tools 

### Rviz 
 used to create environment for simulation/visualization

### .sdf file
structure delay/Description  format-

   Native format for the Gazebo simulator.Describes entire simulation environments (terrain, lighting, multiple robots, and non-robot objects like walls).Handles complete physics and sensor parameters natively.


## pyserial 
a python library which helps hardware to understand code
      "printenv ROS_DISTRO" - to know the environment created in ros

## command

* ommand **winget install usbipd** :- to connect arduino ide with wsl

* sudo usermod -a -G dialout $USER


# arm bridge repo 

ros2 pkg create arm_bridge --build-type amanet_python --dependencies rclpy sensor_msgs


      

# security 



# debugging 
      ros topic hz /topic  # measure publish rate
      ros topic bw /topicn #measure bandwidth 
      ros2 bag record/play #data logging and replay (SQLite /MCAP storage back)
      rqt_graph # visualize node/topic graph
      ros2 doctor # sanity-check environment config 
      rviz2 # 3d visualize of tf , sensor data , costmaps , planning scenes 

# 1. custom interfaces (msg/srv/action)
      beyond built-in types you define your own in a dedicated _msgs/_interfaces package 

 command -  **msg/BatteryState.msg**

