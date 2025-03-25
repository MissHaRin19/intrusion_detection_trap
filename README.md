# Intrusion Detection Trap: Monitoring Unauthorized Access

This project is designed to enhance security by detecting unauthorized access using **honeytokens**. It is structured into three phases:

## Project Roadmap

### **Phase 1: Intrusion Detection Trap (Current Phase)**
- Developed a basic security mechanism that redirects all unauthorized file access to a **decoy file**, triggering an alert.

### **Phase 2: Honeytoken System**  
- Implemented a system that monitors specific files (**honeytokens**) for unauthorized access.  
- Captures an image of the intruder using a **webcam**.  
- Logs critical details (**file accessed, timestamp, intruder’s IP**) into a **database**.  
- Sends an **email alert** with the captured image and access details.  
- [GitHub Repository: Honeytoken System](https://github.com/MissHaRin19/honeytoken_system)

---

## **Overview**

This project implements an **Intrusion Detection Trap** that detects unauthorized file access by:
- Redirecting all file interactions to a **decoy file**.
- Capturing the **intruder’s image** via a webcam.
- Sending an **email alert** with the captured image and access details.

---

## **Features**

✅ **Decoy Redirection** – All unauthorized file accesses are redirected to a fake file.  

✅ **Webcam Capture** – Captures the intruder’s image upon file access.  

✅ **Email Alerts** – Sends an email notification with the captured image.  

✅ **Continuous Monitoring** – Actively tracks file interactions for potential security threats.  

---

## **Installation & Setup**

### **Prerequisites**
Ensure you have the following installed:

- **Python 3.x**
- **OpenCV** (`cv2`)
- **smtplib** (for email services)
- **OS** and **shutil** libraries (for file operations)

### **How It Works**
1. The `monitor.py` script continuously tracks **file accesses** in a designated directory.  
2. If a file is opened, the request is **redirected** to a **decoy file**.  
3. The system then activates the **webcam** to capture the intruder’s image.  
4. An **email alert** is sent with the captured image as an attachment.  
5. The `link.sh` script ensures **all access attempts are monitored** by facilitating file redirection.
