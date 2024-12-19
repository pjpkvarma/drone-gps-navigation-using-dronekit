# Drone Navigation with DroneKit

## Overview

This repository contains a Python script for GPS-based autonomous navigation of a drone using the DroneKit Python library. The script demonstrates how to arm the drone, take off to a target altitude, navigate to a specified GPS waypoint, and return to the launch location. The implementation is designed to work with ArduPilot firmware on a compatible flight controller.

---

## Features

- Arm the drone and take off to a specified altitude.
- Navigate to a GPS waypoint using the `simple_goto` command.
- Return to launch (RTL) automatically after reaching the waypoint.
- Adjustable altitude and ground speed.

---

## Hardware Requirements

- **Flight Controller**: Pixhawk Orange Cube Plus.
- **GPS Module**: Here3 GPS module.
- **Frame**: x500v2 quadcopter frame.
- **Telemetry Module**: Required for communication with the ground control station.
- **Power Supply**: Adequate power module for the flight controller and motors.
- **Motors and ESCs**: Compatible with the x500v2 frame.

---

## Software Requirements

- **Firmware**: ArduPilot (Copter version).
- **DroneKit-Python Library**: Ensure DroneKit is installed.

---

## Setup Instructions

### 1. Hardware Setup
- Assemble the x500v2 quadcopter frame with the Pixhawk Orange Cube Plus and Here3 GPS module.
- Attach the motors, ESCs, and power module as per the frame's design.
- Ensure all connections are secure, and calibrate your flight controller using Mission Planner or QGroundControl.

### 2. Install Required Libraries
- Install Python 3.8+.
- Install DroneKit:
  ```bash
  pip install dronekit
