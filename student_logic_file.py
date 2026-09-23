import data_handle

def add_student():
    """Prompts the user for details and saves a new student to JSON."""
    # 1. Load the existing list of students from the JSON file
    students_list = data_handle.load_data()
    
    print("\n--- Enter New Student Details ---")
    student_id = input("Enter Student ID: ")
    
    # Check if the ID already exists to prevent duplicates
    for student in students_list:
        if student["id"] == student_id:
            print("Error: A student with this ID already exists!")
            return # Stops the function early

    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    grade = input("Enter Student Grade/Class: ")

    # 2. Package the data into a Python dictionary 
    # (This perfectly maps to a JSON Object)
    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade
    }

    # 3. Add the new dictionary to our list
    students_list.append(new_student)
    
    # 4. Save the updated list back to the JSON file
    data_handle.save_data(students_list)
    print(f"\nSuccess! {name} has been added to the system.")


def view_students():
    """Loads and prints all students from the JSON file."""
    students_list = data_handle.load_data()
    
    # Check if the list is empty
    if len(students_list) == 0:
        print("\nNo students found in the database.")
        return

    print("\n--- Enrolled Students ---")
    for student in students_list:
        # Format the output nicely
        print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}")
    print("-------------------------")

def update_student():
    """Finds a student by ID and updates their information."""
    students_list = data_handle.load_data()
    student_id = input("\nEnter the ID of the student to update: ")
    
    for student in students_list:
        if student["id"] == student_id:
            print(f"Found student: {student['name']}")
            print("Leave blank and press Enter to keep current value.")
            
            new_name = input(f"New Name [{student['name']}]: ")
            new_age = input(f"New Age [{student['age']}]: ")
            new_grade = input(f"New Grade [{student['grade']}]: ")
            
            # Update only if the user typed something new
            if new_name: student["name"] = new_name
            if new_age: student["age"] = new_age
            if new_grade: student["grade"] = new_grade
            
            data_handle.save_data(students_list)
            print("\nStudent updated successfully!")
            return
            
    print("\nError: Student ID not found.")

def delete_student():
    """Finds a student by ID and removes them from the JSON file."""
    students_list = data_handle.load_data()
    student_id = input("\nEnter the ID of the student to delete: ")
    
    # enumerate gives us both the index number (i) and the student data
    for i, student in enumerate(students_list):
        if student["id"] == student_id:
            confirm = input(f"Are you sure you want to delete {student['name']}? (y/n): ")
            if confirm.lower() == 'y':
                del students_list[i] # Removes the student from the list at index 'i'
                data_handler.save_data(students_list)
                print("\nStudent deleted successfully!")
            else:
                print("\nDeletion cancelled.")
            return
            
    print("\nError: Student ID not found.")