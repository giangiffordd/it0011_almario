fname =input("Enter your first name: ")
lname =input("Enter your last name: ")
age = int(input("Enter your age: "))
fullname = fname +" "+ lname
slicedname = fullname[0:3]

print(fullname)
print("Full name: ", fname +" "+ lname)
print("Sliced Name: ", fullname[0:3])

txt = "Greeting Message: Hello, {}! Welcome. You are {} years old."

print(txt.format(slicedname, age))
    


