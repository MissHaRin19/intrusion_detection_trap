# Intrusion Detection Trap: Monitoring Unauthorized Access


This project is designed to enhance security by detecting unauthorized access using honeytokens. It is structured into three phases:

Phase 1: Intrusion Detection Trap (Current Phase)

Initially developed a basic security mechanism where all file accesses redirected to a decoy, triggering an alert.

Phase 2: Honeytoken System 

Created a system that monitors specific files (honeytokens) for unauthorized access.
Captures an image of the intruder using a webcam.
Logs details (file accessed, timestamp, intruder’s IP) into a database.
Sends an email alert with the captured image and details of the accessed file.


__Overview__

This project implements an Intrusion Detection Trap that detects unauthorized file access by redirecting all file interactions to a decoy, capturing the intruder’s image via webcam, and sending an email alert with the captured image.

__Features__

Decoy Redirection – All file accesses are redirected to a fake file.

Webcam Capture – Captures the intruder’s image upon file access.

Email Alerts – Sends an email notification with the captured image.

Continuous Monitoring – Actively tracks file interactions for potential security threats.



**Installation**



__Prerequisites:__

Python 3.x

OpenCV (cv2)

smtplib for email services

OS and shutil libraries for file operations


**How It Works**

The monitor.py script continuously tracks file accesses in a designated directory. When any file is opened, it redirects the request to a decoy file, activates the webcam to capture the intruder’s image, and sends an email alert with the attached image. The link.sh script facilitates file redirection, ensuring all access attempts are monitored.
