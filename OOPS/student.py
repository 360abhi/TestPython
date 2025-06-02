class Student:

    def __init__(self,name,id,courses=[]):
        self.name = name
        self.id = id
        self.courses = courses

    def addCourse(self,course):
        self.courses.append(course)

    def removeCourse(self,course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{course} removed ")
        else:
            print(f"course {course} not found , please enroll first")

    def displayCourses(self):
        for course in self.courses:
            print(f"course = {course}")

abhi = Student('Abhishek','001')
abhi.addCourse('english')
abhi.addCourse('hindi')
abhi.addCourse('sst')
abhi.addCourse('science')
abhi.displayCourses()
abhi.removeCourse('science')
print(abhi.courses)
abhi.removeCourse('german')
        