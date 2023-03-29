

students = []
courses = []
class course():
    id = 0
    def __init__(self, course_name, level):
        self.course_id = course.id
        self.name = course_name
        self.level = level
    id += 1

class student():
    id = 0
    def __init__(self, student_name, student_level):
        self.student_name = student_name
        self.student_id = student.id
        self.student_level = student_level
        self.student_courses = []
        student.id += 1
    def add_course(self):
        course_number = int(input("enter course id: "))
        for j in courses:
            if course_number == j.course_id:
                if j in self.student_courses:
                    print("course already exist")
                else:
                    self.student_courses.append(j)
                    print("course added successfully")
            else:
                print("course not exist")

    def student_info(self):
        print(f"student name: {self.student_name} ,student level: {self.student_level}")
        if len(self.student_courses) == 0:
            print("there is no courses yet")
        else:
            for i in range(len(self.student_courses)):
                print(f"course name: {self.student_courses[i].name}, level: {self.student_courses[i].level}")



choice = -1
while choice != 0:
    print("""select choice please:
    1.add new student
    2.remove student
    3.edit student
    4.display all students
    5.create new course
    6.add course to student
    0.exit""")
    choice = int(input())

    if choice == 1:
        student_name = input("enter student name: ")
        while True:
            student_level = input("enter student level: (A, B, or C) ")
            if student_level == 'A' or student_level == 'B' or student_level == 'C':
                break
            else:
                print("invalid level.")

        student1 = student(student_name=student_name, student_level=student_level)
        students.append(student1)
        print("student saved successfully")

    elif choice == 2:
        delete_id = int(input("enter student id: "))
        for i in students:
            if delete_id == i.student_id:
                output = 0
                delete_student = i
            else:
                output = -1
        if output == 0:
            students.remove(delete_student)
            print("student removed successfully")
        else:
            print("user not exist")

    elif choice == 3:
        update_id = int(input("enter student id: "))
        for i in students:
            if update_id == i.student_id:
                new_name = input("enter new name: ")
                i.student_name = new_name
                new_level = input("enter new level: (A, B or C)")
                i.student_level = new_level
                print("student removed successfully")
            else:
                print("user not exist")

    elif choice == 4:
        for i in students:
            i.student_info()

    elif choice == 5:
        course_name = input("enter class name: ")
        course_level = input("enter course level: (A, B, or C)")
        while True:
            if course_level == 'A' or course_level == 'B' or course_level == 'C':
                break
            else:
                print("invalid level.")
        course = course(course_name=course_name, level=course_level)
        courses.append(course)

    elif choice == 6:
        student_number = int(input("enter student number: "))
        for i in students:
            if student_number == i.student_id:
                i.add_course()
            else:
                print("student not exist")

    elif choice == 0:
        print("bye")

    else:
        print("invalid choice")
