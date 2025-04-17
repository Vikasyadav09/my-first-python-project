import json
import os

DATA_PATH = os.path.join(r'D:\python package\Src\Database\studentdetails.json')

def show_active_students():
    try:
        with open(DATA_PATH, 'r') as file:
            students = json.load(file)
            active_students = [s for s in students if s.get("status") == "active"]
            print("\nActive Students:")
            for student in active_students:
                print(student)
    except Exception as e:
        print("Error reading student data:",e)