"""
This module provides functionality for handling threat database operations.
It includes importing necessary libraries and setting the folder path for the JSON file location.
"""

import hashlib
import os
import json

FOLDER_PATH= 'db/threat_db'   # json file location

threat_db = []

for filename in os.listdir(FOLDER_PATH):
    if filename.endswith('.json'):
        file_path = os.path.join(FOLDER_PATH, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if 'tlsh' and 'name' in data:
                threat_db.append(data['tlsh'])
                # threat_db.append(data['name'])

print("\n", threat_db)

# db =['5d41402abc4b2a76b9719d911017c592',
#     '69a329523ce1ec88bf63061863d9cb14']

def check (signature_to_check):
    print(f"signature: {signature_to_check}")
    if signature_to_check in threat_db:
        print('Malicious')
    else:
        print('Clean')

file_list = os.listdir(".")
for exe_file in file_list:
    if exe_file.endswith(".exe"):
        print(f"Checking file: {exe_file}")
        with open(exe_file, 'rb') as f:
            file_data = f.read()
            result = hashlib.md5(file_data)
            signature= print(result.hexdigest())
            print(signature)
            check(signature)