students = []
def main():
    print('''
    1. Add Student
    2. Search Student
    3. Update Student
    4. Delete Student
    5. Exit''')
    Search_option = input("Enter your search option : ")
    if Search_option == '1' or Search_option.lower() == "Add Student":
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
            print(student)
            students.append(student)
            print(students)
        Add_Student()
        print("Student added successfully.")
    elif Search_option == '2' or Search_option.lower() == "Search Student":
        # Searching Option
        def searching():
            search = input("Enter the name of the student to search: ")
            for student in students:
                print(student)
                if search.lower() == student["name"].lower() or search == student["student_id"].lower():
                    print(student)
                    break
                else: 
                    print("student not found")
    elif Search_option == "3" or Search_option.lower() == "Update Student":
        def update():
            given_id = input("Enter Student ID to update: ")
            for student in students:
                if given_id.lower() == student["student_id"]:
                    print(student)
                student
            










if __name__ == "__main__":
    print('Application started')
    while True:
        main()