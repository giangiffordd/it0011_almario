fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = int(input("Enter your age: "))
cnumber = input("Enter your contact number: ")
course = input("Course: ")

student_info = f"Name: {fname} {lname}, Age: {age}, Contact Number: {cnumber}, Course: {course}\n"

with open("C:\\Users\\202311131\\Documents\\GitHub\\it0011_almario\\TFA2\\students.txt", "w") as f:
    f.write(student_info)

print("Student information has been saved to 'students.txt'")