# oops example 1
class OnlineCourse:

    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor
        self.students = []

    def enroll_student(self, student_name):
        self.students.append(student_name)
        print(f"{student_name} has enrolled in the {self.course} successfully")

    def get_course_details(self):
        print(f"Course : {self.course}")
        print(f"Imstructor name : {self.instructor}")
        print(f"enrolled students :{' , '.join(self.students)}")

    def complete_course(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"{student_name} completed course successfull...")
        
        else: 
            print(f"{student_name} is not enrolled in this course")

course1 = OnlineCourse("python", "sugumar")
course1.enroll_student("Revathi")
course2 = OnlineCourse("Java", "Kaviya")
course2.enroll_student("Abishek")
course2.enroll_student("Yuvaraj")
course2.get_course_details()
course1.get_course_details()

