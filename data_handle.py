import json
import os
import sys

# This finds the directory where the script (or exe) is located
if getattr(sys, 'frozen', False):
    # If running as an .exe
    BASE_DIR = os.path.dirname(sys.executable)
else:
    # If running as a .py script
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_NAME = os.path.join(BASE_DIR, 'students.json')

def load_data():
    """Reads the JSON file and returns a Python list of dictionaries."""
    if not os.path.exists(FILE_NAME):
        return [] 
    
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

def save_data(data):
    """Takes a Python list and writes it back to the JSON file."""
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=4)