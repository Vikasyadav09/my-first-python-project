import studentragisteration
import studentdetail
import searchstudent

def main():
    while True:
        try:
            print("\nStudent Management System")
            print("1. Register Student")
            print("2. Display All Students")
            print("3. Search Student by ID")
            print("4. Search Student by Qualification")
            print("5. Exit")

            choice = int(input("Choose an option: "))

            if choice == 1:
                studentragisteration.register_student()
            elif choice == 2:
                studentdetail.display_all_students()
            elif choice == 3:
                searchstudent.search_by_id()
            elif choice == 4:
                searchstudent.search_by_qualification()
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Invalid option. Please try again.")

        except Exception as e:
            print(f"An error occurred: {e}")
    

    
main()