## 🚨 NOTE

**⚠️ SCoPP project code will be uploaded after the associated journal paper is officially published. Thank you for your patience!**


# Drone Navigation with DroneKit

## Overview

This repository contains a Python script for GPS-based autonomous navigation of a drone using the DroneKit Python library. The script demonstrates how to arm the drone, take off to a target altitude, navigate to a specified GPS waypoint, and return to the launch location. The implementation is designed to work with ArduPilot firmware on a compatible flight controller.

## Features

- Arm the drone and take off to a specified altitude.
- Navigate to a GPS waypoint using the `simple_goto` command.
- Return to launch (RTL) automatically after reaching the waypoint.
- Adjustable altitude and ground speed.

## Hardware Requirements

- **Flight Controller**: Pixhawk Orange Cube Plus.
- **GPS Module**: Here3 GPS.
- **Frame**: x500v2 quadcopter frame.
- **Telemetry Module**: For communication with the ground control station.
- **Power Supply**: Adequate for flight controller and motors.
- **Motors and ESCs**: Compatible with x500v2 frame.

## Software Requirements

- **Firmware**: ArduPilot (Copter version).
- **DroneKit-Python Library**: Install using `pip install dronekit`.

## Setup Instructions

1. Connect your drone hardware, including the Pixhawk Orange Cube Plus and Here3 GPS, to your x500v2 frame.
2. Calibrate the flight controller using Mission Planner or QGroundControl.
3. Modify the script:
   - Update the connection string (`/dev/ttyACM0` or `COMx`).
   - Add the target GPS waypoint (`lat`, `lon`, `alt`).
4. Run the script:
   ```bash
   python gps_navigation.py

### Safety Guidelines
1. Ensure the flight area is clear of obstacles and comply with local regulations.
2. Perform pre-flight checks for hardware and software readiness.

### Disclaimer
This code is provided for educational purposes. Test it in a controlled environment before real-world use. The authors are not responsible for any issues arising from its use.
