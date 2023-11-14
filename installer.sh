#!/bin/bash
echo "allowing universe and other repos"
sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo add-apt-repository restricted

echo "allowing to get packages from packages.ros.org"
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
echo "registering server public keys"
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

echo "updating ..."
sudo apt update

echo "installing ros noetic"
sudo apt install ros-noetic-desktop-full

echo "setting up noetic enviroment"
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc

echo "installing depencies for building ros packages (python3)"
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

sudo rosdep init
rosdep update

echo "installing realsense sdk"
git clone https://github.com/IntelRealSense/librealsense.git
cd ~/librealsense/

echo "Installing core packages:"
sudo apt-get install git libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev

sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev at
./scripts/setup_udev_rules.sh
./scripts/patch-realsense-ubuntu-lts.sh
mkdir build && cd build

echo "running CMake"
cmake ../ -DBUILD_EXAMPLES=true

echo "recompiling"
sudo make uninstall && make clean && make && sudo make install

echo "installing ros wrapper"
cd /
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src/
git clone https://github.com/IntelRealSense/realsense-ros.git
cd realsense-ros/
git checkout `git tag | sort -V | grep -P "^2.\d+\.\d+" | tail -1`
cd ..

echo "initializing catkin workspace and cloning ddynamic reconfigure"
catkin_init_workspace
cd ..
catkin_make clean
git clone https://github.com/pal-robotics/ddynamic_reconfigure.git
catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release
catkin_make install

echo "setting up the enviroment"
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc

echo "installing SLAM noetic packages"
sudo apt-get install ros-noetic-imu-filter-madgwick
sudo apt-get install ros-noetic-rtabmap-ros
sudo apt-get install ros-noetic-robot-localization