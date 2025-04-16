import json
import os

DATA_FILE = "students.json"

def load_students():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)

def search_by_id():
    students = load_students()
    sid = input("Enter student ID to search: ").strip()
    found = False

    for student in students:
        if student["id"] == sid:
            print("Student Found:")
            print(student)
            found = True
            break
    if not found:
        print("Student not found.")

def search_by_qualification():
    students = load_students()
    qualification = input("Enter qualification to search: ").strip().lower()
    found = False

    for student in students:
        if qualification in [q.lower() for q in student["qualifications"]]:
            print("Student Found:")
            print(student)
            found = True

    if not found:
        print("No student found with that qualification.")