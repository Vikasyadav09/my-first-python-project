import json
import os

DATA_PATH = os.path.join(r'D:\python package\Src\Database\studentdetails.json')

def show_inactive_students():
    try:
        with open(DATA_PATH, 'r') as file:
            students = json.load(file)
            inactive_students = [s for s in students if s.get("status") == "inactive"]
            print("\nInactive Students:")
            for student in inactive_students:
                print(student)
    except Exception as e:
        print("Error reading student data:",e)