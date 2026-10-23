def func1():
    pass

class Student:
    print("Hi")
    amount_of_students = 0
    def __init__(self, height=160):
        self.height = height
        print("Hello")
        Student.amount_of_students += 1
    def grow(self, height = 1):
        self.height += height

    def __str__(self):
        return f"I am a student. Height is: {self.height}"

    def __del__(self):
        print("Training is over. I am now an expert!")

    #==========================================================
    def __bool__(self):
        return self.height > 160

    def __len__(self):
        return self.height


print(Student.amount_of_students)
first_student = Student()
second_student = Student(height=360)
print(bool(first_student))
print(first_student.height)
print(second_student.height)
print(Student.amount_of_students)
print(f"Amount of students in second student: {second_student.amount_of_students}")
print("Grow!")
first_student.grow(200)
second_student.grow(-50)
print(f"First student's height: {first_student.height}")
print(f"Second student's height: {second_student.height}")
print