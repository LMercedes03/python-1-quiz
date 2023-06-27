# In pb3.py, create a function that takes a dictionary of student names and their ages as
# input and returns the name of the youngest student.
def youngest_student(students):
    student_age = 120
    student_name = ""

    # Iterate through student items
    for name, age in students.items():
        if age < student_age:
            student_age = age
            student_name = name
    return student_name


# students = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
# print(youngest_student(students))  # Expected output: "Alice"
