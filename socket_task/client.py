import socket
import json
import logging
from time import sleep
"""
Make sure to run server.py file first before running this file!
"""


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("rfid_reader_test.log"),  # Log to a file
        logging.StreamHandler()  # Log to the console
    ]
)

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# Sample RFID data to send
rfid_data = [
    {
        "tag_id": "12345",
        "timestamp": "2023-10-01T12:00:00",
        "location": "Warehouse A",
        "status": "active"
    },
    {
        "tag_id": "67890",
        "timestamp": "2023-10-01T12:05:00",
        "location": "Warehouse B",
        "status": "inactive"
    },
    {
        "tag_id": "54321",
        "timestamp": "2023-10-01T12:10:00",
        "location": "Warehouse C",
        "status": "active"
    }
]
def send_rfid_data(data):
    """
    https://realpython.com/python-sockets/#echo-client
    Good example of the thing.
    """
    # Connect to the server
    ...
    # Convert data to JSON (binary) and send it
    ...
    # Wait for the server's response
    ...
    # Validate the response
    return

# Simulate sending multiple RFID entries
for entry in rfid_data:
    send_rfid_data(entry)
    sleep(1)