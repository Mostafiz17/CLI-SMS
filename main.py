def main():
    print('''
    1. Add Student
    2. View Students
    3. Search Student
    4. Update Student
    5. Delete Student
    6. Exit''')
    students = []
    Search_option = input("Enter your search option : ")
    if Search_option == '1' or Search_option == "Add Student":
        # Adding Student
        def Add_Student():
            name = input("Enter student's name: ")
            student_id = input("Enter student ID: ")
            department = input("Enter student's department: ")

            student = {
                "name": name,
                "student_id": student_id,
                "department": department
            }

            students.append(student)
        Add_Student()
        print("Student added successfully.")
    elif Search_option == '2' or Search_option == "Search Student":
        # Searching Option
            search = input("Enter the name of the student to search: ")
            for student in students:
                if search == student["name"] or search == student["student_id"]:
                    print(student)
                break
            else: 
                print("student not found")

if __name__ == "__main__":
    print('Application started')
    while True:
        main()