students = []


def main():
    print("""
    1. Add Student
    2. Search Student
    3. Update Student
    4. Delete Student
    5. Exit
    """)

    search_option = input("Enter your option: ")

    # Add Student
    if search_option == "1" or search_option.lower() == "add student":

        def add_student():
            name = input("Enter name: ")
            student_id = input("Enter ID: ")
            department = input("Enter department: ")

            student = {
                "name": name,
                "student_id": student_id,
                "department": department
            }

            students.append(student)
            print("Student added successfully.")
            print(student)

        add_student()


    # Search Student
    elif search_option == "2" or search_option.lower() == "search student":

        def searching():
            search = input("Enter student name or ID: ")

            found = False

            for student in students:
                if (search.lower() == student["name"].lower()
                        or search == student["student_id"]):
                    print("Student Found:")
                    print(student)
                    found = True
                    break

            if not found:
                print("Student not found.")

        searching()


    # Update Student
    elif search_option == "3" or search_option.lower() == "update student":

        def update():
            given_id = input("Enter Student ID to update: ")

            found = False

            for student in students:
                if given_id == student["student_id"]:
                    print("Current Information:")
                    print(student)

                    student["name"] = input("Enter new name: ")
                    student["department"] = input("Enter new department: ")

                    print("Student updated successfully.")
                    print(student)

                    found = True
                    break

            if not found:
                print("Student not found.")

        update()


    # Delete Student
    elif search_option == "4" or search_option.lower() == "delete student":

        def deleting():
            deleting_id = input("Enter student's ID whom you want to delete: ")

            found = False

            for student in students:
                if deleting_id == student["student_id"]:
                    students.remove(student)
                    print("Student deleted successfully.")
                    found = True
                    break

            if not found:
                print("Student not found.")

        deleting()


    # Exit
    elif search_option == "5" or search_option.lower() == "exit":
        print("Application closed.")
        exit()


    else:
        print("Invalid option.")


if __name__ == "__main__":
    print("Application started")

    while True:
        main()