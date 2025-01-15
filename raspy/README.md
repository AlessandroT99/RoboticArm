# Raspberry PI 3B+ exec files and procedure
The project is run physical on a raspberry pi 3B+.

## OS Installation
It is suggested the latest version of Raspian OS 64 bit desktop-release without reccomended software, which can be found [here](https://www.raspberrypi.com/software/operating-systems/). In order to ensure getting the correct one for your Raspoberry module please use [Raspberry PI Imager](https://www.raspberrypi.com/software/). 

To run the files in this folder it is necessary to run Raspberry in CLI avoiding RAM saturation. The best option is to boot it directly into CLI mode. If it is needed to use the GUI, run:
```bash
startx
```

## Appicatives and dependencies
ROS 2 is necessary for this project, however, the last version jazzy is easily available on raspian and it shall be installed using a docker as suggest from the [Jazzy Documentation for Raspberry](https://docs.ros.org/en/jazzy/How-To-Guides/Installing-on-Raspberry-Pi.html). The following procedure will help you to get ready.

### Firstly install docker
This commands will get you the latest stable release.
```bash
curl -fsSL https://get.docker.com -o get-docker.sh   
sudo sh get-docker.sh
```

### Then pull the jazzy image for docker
```bash
sudo docker pull ros:jazzy-ros-core
```

### Now clone this project and enter in this folder
```bash
git clone https://github.com/AlessandroT99/RoboticArm.git
cd RoboticArm/raspy
``` 

### Then you are ready to execute the Docker File and create the image we will need
```bash
sudo docker build -t "jazzy_custom"
```

Wait and be patient, at the end your image will be ready.

### Lastly, you can create and start the container with our custom image
```bash
sudo docker compose up 
```

In this way the container will run directly into the terminal. If you want to let it go in background use:
```bash
sudo docker compose up -d
```

## Configure your pc
You will need to run on your PC also ROS2, so please use the ubuntu OS version 24.04.1 LTS.

Then install the required libraries for ROS2 Jazzy as explained [here](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html). 

Then when everythings ready just paste the following commands:
```bash
source /opt/ros/$ROS_DISTRO/setup.bash
export ROS_DOMAIN_ID=0
```

If you will avoid to run `source` command each terminal you open, you can run just once time this:
```bash
echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc
```