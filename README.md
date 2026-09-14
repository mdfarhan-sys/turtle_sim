#  ROS 2 Turtle Simulation

A collection of custom Python scripts and automation tools built on top of the **ROS 2 Turtlesim** package for learning and experimenting with robot kinematics and control.

---

## Repository Structure

```text
.
├── dual_turtle_sim.py   # Script to manage and control multiple turtles simultaneously
├── turtle_sim.py        # Custom node for controlling the turtlesim environment
├── notes.md             # Personal development notes and commands
└── .gitignore           # Git ignore rules for build artifacts
```



### 1. Source the main ROS 2 environment (replace 'humble' with your distro if needed)
source /opt/ros/humble/setup.bash

### 2. Build your workspace (if you made changes to code)
colcon build

#### 3. Source your local workspace setup file
source install/setup.bash

### 4. Start the turtlesim simulation (Terminal 1)
ros2 run turtlesim turtlesim_node



### In your second terminal:
source /opt/ros/humble/setup.bash
source install/setup.bash
cd ~/turtle_sim
python3 dual_turtle_sim.py