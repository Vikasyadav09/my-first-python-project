import json
import os

DATA_FILE = "students.json"

def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)

def register_student():
    students = load_students()
    student = {}
    student["id"] = input("Enter student ID: ")
    student["name"] = input("Enter name: ")
    student["address"] = input("Enter address: ")
    student["contact"] = input("Enter contact: ")
    
    qualifications = []
    for i in range(1):
        qualifications.append(input(f"Enter qualification {i + 1}: "))
        qualifications.append(input(f"Enter passing year"))
    
    while True:
        more = input("Do you want to add more qualifications? (yes/no): ").strip().lower()
        if more == "yes":
            qualifications.append(input("Enter another qualification: "))
            qualifications.append(input(f"Enter passing year"))
        elif more == "no":
            break
        else:
            print("Please enter yes or no.")
    
    student["qualifications"] = qualifications
    students.append(student)
    save_students(students)
    print("Student registered successfully.")