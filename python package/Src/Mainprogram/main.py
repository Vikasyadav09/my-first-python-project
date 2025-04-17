import sys
import os
print(sys.path)

sys.path.append(r"D:\python package")

print("After Adding the path: ")



from Src.Domain import studentregisteration




from Src.Report.Activestudent import activestudent
from Src.Report.Inactivestudent import inactivestudent

def main():
     while True:
         print("\nMenu:")
         print("1. Register Student")
         print("2. Check Report")
         print("0. Exit")
         choice = input("Enter your choice: ")

         if choice == '1':
            studentregisteration.register_student()
            
         elif choice == '2':
             print("\nReport Options:")
             print("1. Search Active Students")
             print("2. Search Inactive Students")
             report_choice = input("Enter your choice: ")

             if report_choice == '1':
                 activestudent.show_active_students()
             elif report_choice == '2':
                 inactivestudent.show_inactive_students()
             else:
                 print("Invalid report option!")
         elif choice == '0':
             print("Exiting...")
             break
         else:
             print("Invalid choice!")
main()
