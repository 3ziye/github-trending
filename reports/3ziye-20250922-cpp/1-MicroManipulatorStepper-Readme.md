# Open Micro Manipulator

This project contains an open source low-cost, easy-to-build motorized **XYZ Micro-Manipulator** motion control platform achieving submicron precision.
It's designed for applications such as optical alignment, probing electronic components, and microscopy.

Check out the YouTube video for more information about the device and how it is built:<br>
[An Open Source Motorized XYZ Micro-Manipulator - Affordable sub µm Motion Control](https://youtu.be/MgQbPdiuUTw)

<div style="display: flex; gap: 2%;">
  <img src="images/overview.gif" alt="Image 1" width="49%">
  <img src="images/microscopy_die.gif" alt="Image 2" width="49%">
</div>

Thanks to its parallel kinematic structure and miniature ball joints, it achieves good mechanical stiffness and a large range of motion.
The motors are off the shelf stepper motors dr​iven by a 30 kHz closed loop controller and a very precise PWM signal.
A 'magnetic gearing' approach increases the resolution of the low-cost magnetic rotary encoders by a factor of 30 allowing for steps down to 50nm
(**Please mind the difference between resolution and accuracy**. The absolute accuracy is significantly worse.

The device can be controlled via simple G-Code commands over a USB serial interface and is thus easily integrated into other projects.
The firmware implements a complete motion planning stack with look-ahead for smooth and accurate path following capabilities.

## 🐍 NEW: Python-API

The lightweight Python API handles all serial communication and provides convenient command execution and debug message printing.
The interface includes functions to home, move, and calibrate the device, as well as to query device information.
Simply copy the [open_micro_stage_api.py](software/PythonAPI/open_micro_stage_api.py) file into your project (also install the dependencies in requirements.txt), and you’re ready to get started.

## Usage Example
```python
from open_micro_stage_api import OpenMicroStageInterface

# create interface and connect
oms = OpenMicroStageInterface(show_communication=True, show_log_messages=True)
oms.connect('/dev/ttyACM0')

# run this once to calibrate joints
# for i in range(3): oms.calibrate_joint(i, save_result=True)

# home device
oms.home()

# move to several x,y,z positions [mm]
oms.move_to(0.0, 0.0, 0.0, f=10)
oms.move_to(3.1, 4.1, 5.9, f=26)
oms.move_to(0.0001, 0.0, 0.0, f=10)

# wait for moves to finish
oms.wait_for_stop()
```

## API Functions (most relevant functions only)
```python
connect(port, baud_rate=921600)
disconnect()
set_workspace_transform(transform)
get_workspace_transform()
home(axis_list=None)
calibrate_joint(joint_index, save_result)
move_to(x, y, z, f, move_immediately, blocking, timeout)
set_pose(x, y, z)
dwell(time_s, blocking, timeout)
enable_motors(enable)
wait_for_stop(polling_interval_ms, disable_callbacks)
set_max_acceleration(linear_accel, angular_accel)
set_servo_parameter(pos_kp, pos_ki, vel_kp, vel_ki, vel_filter_tc)
```

## ✨ NEW: Firmware v1.0.1

This update improves calibration, homing, logging, and adds several new G-Code commands.

### Improvements
- **Homing**: parallel homing support, higher repeatability, more accurate geometric reference  
- **Joint calibration**: refined procedure, persistent flash storage (no recalibration after reboot)  
- **Logging**: clearer and more detailed output  

### New G-Code Commands
- `G28` — Home joints (supports homing multiple axis simultanously for faster startup)
- `G24` — Set pose command (directly sets servo targets, bypassing motion controller)  
- `M17/M18` — Enable/Disable motors (with pose recovery from encoders on enable)  
- `M51` — Read encoder values  
- `M55` — Set servo loop parameters 
- `M56` — Joint calibration (with save-to-flash option)  
- `M57` — Read various information about the device state  
- `M58` — Read firmware version

## ⚙ CAD-Files

All CAD models are made in **FreeCAD** to​ allow everyone to view and modify the design without subscribing or paying for a proprietary CAD solution.
Note that most components are already designed with the goal to make them easily machinable on a 3-Axis CNC-Mill.
You can also 3D-Print the parts but have to live with thermal drift (carbon filled filaments can reduce this problem).

<div style="display: flex;">
    <img src="images/FreeCAD-Model.jpg" alt="FreeCAD Model" width="50%">
</div>

<br>

The CAD files can be found here: [CAD Models](construction).
Please note that FreeCAD version **1.1.0dev** was used, and the files might not work with older versions.

STL files for printing can be found here: [STL Files](construction/STL_3D_Printing/)

## ⚙ Kinematic Model

The kinematic model is defined here: [kinematic_model_delta3d.cpp](firmware/MotionControllerRP/src/kinemtaic_models/kinematic_model_delta3d.cpp).
Please check the dimensions of your build against the values set in the constructor. In particular, make sure the arm length matches.

## ⚙ Electronics

IMPORTANT: If you fabricated PCB verion v1.2 (s