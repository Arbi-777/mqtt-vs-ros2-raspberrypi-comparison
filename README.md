
# Experimental Comparison of MQTT and ROS 2 Communication on Raspberry Pi

## Overview

This repository contains the implementation and experimental evaluation for my seminar work comparing MQTT and ROS 2 communication on Raspberry Pi devices.

## Objective

The objective is to compare MQTT and ROS 2 with respect to:

- Communication latency
- Round-trip time (RTT)
- System architecture
- Resource requirements
- Suitability for IoT and robotics applications

## Experimental Setup

Hardware
- Raspberry Pi 4 (Publisher)
- Raspberry Pi 4 (Subscriber/Broker)

Software
- Raspberry Pi OS
- Python 3
- Eclipse Mosquitto
- ROS 2 Humble
- VS Code

## Repository Structure

01_Data/
Experimental CSV results

02_figures/
Graphs generated from the experiments

03_src/
MQTT and ROS 2 implementation

04_Screenshots/
Experimental screenshots

## Results

The experiments show that MQTT provides significantly lower communication latency than ROS 2 for this experimental setup.

Average MQTT latency: approximately 12 ms

Average ROS 2 latency: approximately 54 ms

## Author

Mohammed Arbaaz Khan

Seminar:
Experimental Comparison of MQTT and ROS 2 Communication on Raspberry Pi Devices

Ostfalia Hochschule für angewandte Wissenschaften
