filename = "Students.txt"

with open(filename, "a"):  
    pass

def load_students():
    students = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            student_id, first_name, last_name = parts[:3]
            class_standing, major_exam = map(float, parts[3:])
            students.append((student_id, (first_name, last_name), class_standing, major_exam))
    return students

def display_students(sorted_students):
    print("\nStudent Records:\n")
    for student in sorted_students:
        final_grade = (student[2] * 0.6) + (student[3] * 0.4)
        print(f"Student No.: {student[0]}\nFull Name: {student[1][0]} {student[1][1]}\nFinal Grade: {final_grade:.2f}\n")

def save_students(students, file_name):
    with open(file_name, "w") as file:
        for student in students:
            file.write(f"{student[0]},{student[1][0]},{student[1][1]},{student[2]},{student[3]}\n")

def find_student(student_id, students):
    return next((s for s in students if s[0] == student_id), None)

students = load_students()

while True:
    print("\nStudent Record Management System")
    print("1. Show All Student Records")
    print("2. Show Student Record")
    print("3. Add Record")
    print("4. Edit Record")
    print("5. Delete Record")
    print("6. Save File")
    print("7. Save As File")
    print("8. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        sub_choice = input("\n1. Ordered by Last Name\n2. Ordered by Grade\nEnter your choice: ")
        
        if sub_choice == "1":
            display_students(sorted(students, key=lambda x: x[1][1]))
        elif sub_choice == "2":
            display_students(sorted(students, key=lambda x: (x[2] * 0.6 + x[3] * 0.4), reverse=True))
        else:
            print("Invalid choice.")
    
    elif choice == "2":
        student_id = input("Enter Student ID: ")
        student = find_student(student_id, students)
        
        if student:
            final_grade = (student[2] * 0.6) + (student[3] * 0.4)
            print(f"\nStudent No.: {student[0]}\nFull Name: {student[1][0]} {student[1][1]}\nClass Standing: {student[2]}\nMajor Exam Score: {student[3]}\nFinal Grade: {final_grade:.2f}")
        else:
            print("Student not found!")
    
    elif choice == "3":
        while True:
            student_id = input("Enter Student ID (6 digits): ")
            if len(student_id) == 6 and student_id.isdigit():
                break
            print("Invalid Student ID. Must be exactly 6 digits.")
        
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = float(input("Enter Class Standing Grade: "))
        major_exam = float(input("Enter Major Exam Grade: "))
        
        students.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully!")
    
    elif choice == "4":
        student_id = input("Enter Student ID to edit: ")
        for i, student in enumerate(students):
            if student[0] == student_id:
                first_name = input("Enter New First Name: ")
                last_name = input("Enter New Last Name: ")
                class_standing = float(input("Enter New Class Standing Grade: "))
                major_exam = float(input("Enter New Major Exam Grade: "))
                students[i] = (student_id, (first_name, last_name), class_standing, major_exam)
                print("Record updated successfully.")
                break
        else:
            print("Student not found.")
    
    elif choice == "5":
        student_id = input("Enter Student ID to delete: ")
        students = [s for s in students if s[0] != student_id]
        print("Record deleted successfully.")
    
    elif choice == "6":
        save_students(students, filename)
        print("File saved successfully.")
    
    elif choice == "7":
        new_filename = input("Enter new filename: ")
        save_students(students, new_filename)
        print("File saved successfully.")
    
    elif choice == "8":
        print("Exiting program...")
        break
    
    else:
        print("Invalid choice! Please try again from the choices.")
