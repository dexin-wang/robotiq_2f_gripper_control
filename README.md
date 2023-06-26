# robotiq_2f_gripper_control

A package for facilitating the use of Robotiq Gripper in ROS.

## Install
(1) Install robotiq ros package follow the steps of https://github.com/ros-industrial/robotiq.

(2) Replace `robotiq_2f_gripper_control` with this package and recompile.

## Usage
(1) In launch file of ROS, add the following code:
```python
<node pkg="robotiq_2f_gripper_control" type="Robotiq2FGripperRtuNode_my.py" name="Robotiq2FGripperRtuNode_my" output="screen" /> 
<node pkg="robotiq_2f_gripper_control" type="Robotiq2FGripperSimpleController_my.py" name="Robotiq2FGripperSimpleController_my" output="screen" />
```

(2) After running the launch file, control the movement of robotiq gripper by sending `std_msgs/String` messages to the topic `/robotiq/gripper_cmd`, Commonly used commands correspond to the following messages:
> Reset: r
> Activate: a
> Close: c
> Open: o
> Opening width: 0-255
> 
