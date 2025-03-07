# file_honeytoken

Honeytoken: Invisible Traps for Cyber Intruders

Overview

Honeytokens are deceptive security mechanisms designed to detect unauthorized access and potential cyber threats. This project implements a honeytoken system that redirects unauthorized access attempts to a fake folder, captures the attacker's face via a webcam, and sends an email alert with the captured image.

Features

Fake Folder Redirection: Sensitive files are hidden, and unauthorized access attempts are directed to a decoy folder.

Webcam Capture: The attacker's image is captured using the system's webcam.

Email Alert: An email notification is sent with the captured image to alert the system owner of the intrusion.

Stealthy Monitoring: Operates discreetly to avoid detection by intruders.

Installation

Prerequisites

Python 3.x

OpenCV (cv2)

smtplib for email services

OS and shutil libraries for file operations

The **honeytoken.py** script is responsible for continuously monitoring a designated directory for unauthorized access. When an intrusion is detected, it activates the system’s webcam to capture an image of the intruder and sends an email alert with the captured image attached. Additionally, **link.sh** is used to redirect sensitive files to a decoy folder, ensuring that unauthorized users are lured into interacting with the honeytoken system. This combination helps in identifying and tracking potential security threats in real time.
