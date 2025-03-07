import os
import smtplib
import time
import cv2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Directory to watch
WATCH_DIR = os.path.expanduser('~/honeytoken/fake')

# Email details
SENDER_EMAIL = "gentleefforts@gmail.com"
RECEIVER_EMAIL = "160622733108@stanley.edu.in"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
APP_PASSWORD = "prxitcmadaispqqi"  # Use your Gmail App Password

# Email content
SUBJECT = "Honeypot Alert"
BODY = "A file in your honeytoken directory was accessed! Attached is the intruder's image."

# Path to monitor
TARGET_FILE = "data.txt"

# Define webcam capture function
def capture_image():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Give some time to initialize the webcam
    time.sleep(2)

    # Capture an image
    ret, frame = cap.read()
    if ret:
        # Save the captured image
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        image_filename = f"/Users/aishu/honeytoken/real/captured_{timestamp}.jpg"
        cv2.imwrite(image_filename, frame)
        print(f"Captured image: {image_filename}")
    else:
        print("Failed to capture image.")

    # Release the webcam
    cap.release()

    return image_filename  # Return the image file path

# Send email function with image attachment
def send_email(image_filename):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(BODY, 'plain'))

    # Attach the captured image
    with open(image_filename, 'rb') as image_file:
        img = MIMEImage(image_file.read())
        img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(image_filename))
        msg.attach(img)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
            print("Email sent successfully with image!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# File access handler
class FileAccessHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Check if the event is for the data.txt file
        if not event.is_directory and event.src_path.endswith(TARGET_FILE):
            print(f"File {TARGET_FILE} accessed!")
            image_filename = capture_image()  # Capture image
            send_email(image_filename)  # Send email with the captured image

# Set up the observer to watch the directory
def start_monitoring():
    event_handler = FileAccessHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_DIR, recursive=False)
    observer.start()
    print(f"Monitoring {WATCH_DIR} for file access...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_monitoring()

