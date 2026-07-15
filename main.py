Search_opition = input("Enter your search option (e.g., 'name', 'date', 'category'): ")

if Search_opition == '1' or "Add Student":
    def Add_student(student)
    name = input("Enter student's name: ")
    date = input("Enter enrollment date (YYYY-MM-DD): ")
    category = input("Enter student's category: ")
    # Add student to the database or list
    print(f"Student {name} added successfully.")
if Search_opition == '2' or Search_opiton == "Search Student":
    # Code to search for a student
    search_name = input("Enter the name of the student to search: ")
    # Search logic here
    print(f"Searching for student {search_name}...")
if Search_opition == '3' or Search_opiton == "Delete Student":
    # Code to delete a student
    delete_name = input("Enter the name of the student to delete: ")
    # Delete logic here
    print(f"Student {delete_name} deleted successfully.")
if Search_opition == '4' or Search_opiton == "Update Student":
    # Code to update a student's information
    update_name = input("Enter the name of the student to update: ")
    new_name = input("Enter the new name (leave blank to keep current): ")
    new_date = input("Enter the new enrollment date (YYYY-MM-DD, leave blank to keep current): ")
    new_category = input("Enter the new category (leave blank to keep current): ")
    # Update logic here
    print(f"Student {update_name} updated successfully.")  
if Search_opition == '5' or Search_opiton == "View All Students":
    # Code to view all students
    # View logic here
    print("Displaying all students...")
if Search_opition == '6' or Search_opiton == "Exit":
    print("Exiting the program.")
    exit()
if Search_opition not in ['1', '2', '3', '4', '5', '6']:
    print("Invalid option selected. Please try again.")


    