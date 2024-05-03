# Object Avoiding Car

## Project Overview
This project consists of the code and resources for a self-navigting car that can avoid objects in its path. It uses sensors, and motors controlled by Python scripts to navigate through its environment.

## Features
- **Autonomous Navigation:** Ability to navigate without human intervention.
- **Object Avoidance:** Uses an ultrasonic sensor to detect obstacles and avoid collisions.
- **Modular Code:** Separate scripts for handling different components such as motor control and distance sensing, making it easy to modify and extend.

## Hardware Components
- Raspberry Pi Pico W (or any other compatible microcontroller)
- DC Motors
- Servo Motor
- Ultrasonic Sensor
- Battery Pack
- Chassis
- 2 Tires
- 1 Swivel Tire

## File Descriptions
- `main.py`: The main script that initializes the car's functionalities and controls the operational flow.
- `motor.py`: Controls the DC motors for movement.
- `servo.py`: Manages the servo motor for directional control.
- `ultrasonic.py`: Handles the distance measurement using the ultrasonic sensor.

## Setup and Installation
1. **Assemble the hardware:** Connect all the components based on the YouTube video provided here:[Object Avoiding Car Raspberry Pi Pico W - MicroPython Project](https://youtu.be/DBFbXrDwuZE?si=dCfnAfBYhmaXDY2W).
2. **Install the software:** Ensure Pico or similar microcontroller is set up and good to go.
3. **Run the code:** Execute the `main.py` script to start the car.

## Authors
- **[Karam Haddad](https://github.com/karamhaddad)** - *The entire work*

## License
This project is licensed under the GNU General Public License (GPL) - see the [LICENSE.md](LICENSE) file for details.
