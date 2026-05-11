# STUDENT VARIABLE

student_name = "Jane Doe"
student_major = "Biol"

if student_major == "biol":
    major_name = "biology"
    office_name = "room 310"
elif student_major == "csci":
    major_name = "computer science"
    office_name = "room 314"
elif student_major == "eng":
    major_name = "english"
    office_name = "room 201"
elif student_major == "hist":
    major_name = "history"
    office_name =  "room 114"
elif student_major == "mkt":
    major_name = "marketing"
    office_name = "room 310"
else: 
    major_name = "unknown"
    office_name =""


print("Student Name: ", student_name)
print("Student Major: ", major_name)
