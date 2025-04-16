import json
import os

DATA_FILE = "students.json"

def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)

def display_all_students():
    students = load_students()
    if not students:
        print("No student records found.")
        return
    
    print("\nAll Student Details:\n")
    for student in students:
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Address: {student['address']}")
        print(f"Contact: {student['contact']}")
        print(f"Qualifications: {', '.join(student['qualifications'])}")
        print("-"*40)