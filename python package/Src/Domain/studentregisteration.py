import json
import os

DATA_PATH =os.path.join(r'D:\python package\Src\Database\studentdetails.json')

def register_student():
    student = {
        "id": input("Enter ID: "),
        "name": input("Enter Name: "),
        "contact": input("Enter Contact: "),
        "address": input("Enter Address: "),
        "status": input("Enter Status (active/inactive): ").lower()
    }

    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, 'r') as file:
            try:
                students = json.load(file)
            except json.JSONDecodeError:
                students = []
    else:
        students = []

    students.append(student)

    with open(DATA_PATH, 'w') as file:
        json.dump(students, file, indent=4)
    print("Student registered successfully!")
#register_student()    


def getdata():
    print("This is Domain method ")