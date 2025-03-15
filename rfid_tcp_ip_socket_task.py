import socket
import json
import logging
from time import sleep

"""
Test Scenario: Testing Embedded RFID Reader Software

Description:
You are testing embedded software for an RFID reader.
The software sends RFID data over TCP/IP to a server. Write a Python script to:

    Simulate an RFID reader by sending JSON data over TCP/IP.

    Validate that the server receives the data correctly.

    Log progress.

Steps:

    Create a TCP/IP client in Python to send JSON data.

    Simulate sending multiple RFID entries.

    Validate the server’s response.


Expected Output:

    Successful data transmission and server response.
    Proper error handling for network issues.
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

# Server configuration
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 65432

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


def send_rfid_data(entry_data):
    """
    https://realpython.com/python-sockets/#echo-client
    Good example of the thing.
    """
    # Connect to the server
    ...
    # Convert data to JSON and send it
    ...
    # Wait for the server's response
    ...
    # Validate the response
    return

# Simulate sending multiple RFID entries
for entry in rfid_data:
    send_rfid_data(entry)
    sleep(1)  # Add a delay between transmissions