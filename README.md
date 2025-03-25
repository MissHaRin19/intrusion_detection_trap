# Intrusion Detection Trap: Monitoring Unauthorized Access

Overview

This project implements an Intrusion Detection Trap that detects unauthorized file access by redirecting all file interactions to a decoy, capturing the intruder’s image via webcam, and sending an email alert with the captured image.

Features

Decoy Redirection – All file accesses are redirected to a fake file.

Webcam Capture – Captures the intruder’s image upon file access.

Email Alerts – Sends an email notification with the captured image.

Continuous Monitoring – Actively tracks file interactions for potential security threats.



Installation



Prerequisites:

Python 3.x

OpenCV (cv2)

smtplib for email services

OS and shutil libraries for file operations


How It Works

The monitor.py script continuously tracks file accesses in a designated directory. When any file is opened, it redirects the request to a decoy file, activates the webcam to capture the intruder’s image, and sends an email alert with the attached image. The link.sh script facilitates file redirection, ensuring all access attempts are monitored.
