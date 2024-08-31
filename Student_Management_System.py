class Person:

	def __init__(self, name, id_number):
		self.name = name
		self.id_number = id_number

	def __str__(self):
		return f"Name: {self.name} ID: {self.id_number}"

if __name__ == "__main__":
		person1 = Person("Peter Olusoga", "Altsch1435")
		print(person1)
		pass
class Student(Person):
	def __init__(self, name, id_number, major):
		super().__init__(name, id_number) #Inherit from the Person class
		self.major = major

	def __str__(self):
			return f"{super().__str__()}, Major: {self.major}"
class Instructor(Person):
	def __init__(self, name, id_number, department):
		super().__init__(name, id_number) #Inherit from the Person class
		self.department = department

	def __str__(self):
		return f"{super().__str__()}, Department: {self.department}"

if __name__ == "__main__":
	student1 = Student("Theresa Karmaru", "Altsch9345", "Data Engineering")
	instructor1 = Instructor("Mr Emmanuel Ovwode", "309", "School of Data")

	print(student1)
	print(instructor1)
class Course:
	def __init__(self, course, course_id):
		self.course = course
		self.course_id = course_id
		self.enrolled_students = []

	def add_student(self, student):
		self.enrolled_students.append(student)

	def remove_student(self, student):
		self.enrolled_students.append(student)	

	def __str__(self):
		return f"Course: {self.course}, Course_ID: {self.course_id}, Enrolled_Students: {len(self.enrolled_students)}"

if __name__ == "__main__":
	course1 = Course("Python", "Py201")
	course1.add_student(student1)

	print(course1)
class Enrollment:
	def __init__(self, student, course):
		self.student = student
		self.course = course
		self.grade = None

	def assign_grade(self, grade):
		self.grade = grade

	def __str__(self):
		return f"Student: {self.student.name}, Course: {self.course.course_id}, Grade: {self.grade}"

if __name__ == "__main__":
	
	student1 = Student("Theresa Karmaru", "Altsch9345", "Data Engineering")
	course1 = Course("Python 201", "Py201")

	enrollment1 = Enrollment(student1, course1)
	enrollment1.assign_grade("F")

	#Above code runs, but this is where I can take it to, Thank you. From student management system i got stock

	print(enrollment1)
class StudentManagementSystem:
	def __init__(self):
		self.students = []
		self.instructors = []
		self.courses = []
		self.enrollments = []

	#Method to add a student
	def add_student(self):
		self.students.append(student)

	#Thank you sir, this is where i end. I am sorry, I would do better next time. I love you sir...

