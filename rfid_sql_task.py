"""
You need to store valid RFID data in a SQL database. Write a Python script to:

    Create a SQL table to store RFID data (tag_id, timestamp, location, status).

    Insert valid RFID entries into the table.

    Query the database to retrieve all entries with a specific status (e.g., active).

Steps:

    Connect to a SQLite database.

    Create a table if it doesn’t already exist.

    Insert valid RFID entries into the table.

    Query the database for entries with a specific status.
"""
import sqlite3

RFID_DATA = [
    {"tag_id": "12345", "timestamp": "2023-10-01T12:00:00", "location": "Warehouse A", "status": "active"},
    {"tag_id": "67890", "timestamp": "2023-10-01T12:05:00", "location": "Warehouse B"},
    {"tag_id": "54321", "timestamp": "2023-10-01T12:10:00", "location": "Warehouse C", "status": "inactive"}
]

def fetch_all(cursor_):
    # Query all data from the table
    select_all_query = '''
    SELECT * FROM rfid_entries;
    '''
    cursor.execute(select_all_query)
    return cursor.fetchall()
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('rfid_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# SQL command to create the table
create_table_query = '''
CREATE TABLE IF NOT EXISTS rfid_entries (
    id INTEGER PRIMARY KEY,
    tag_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    location TEXT NOT NULL,
    status TEXT NOT NULL
);
'''

try:
    # Execute the SQL command to create the table
    cursor.execute(create_table_query)
    print("Table 'rfid_entries' created successfully or already exists.")
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    # Commit the changes and close the connection
    conn.commit()

