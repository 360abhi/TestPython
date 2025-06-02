class Student:

    school_name = "NCS" # class var

    def __init__(self,name):
        self.name = name
        
    # Instance method
    def getname(self):
        return self.name
    
    # Class method
    @classmethod
    def changeSchool(cls,new_name):
        cls.school_name = new_name
        return f"School changed to {cls.school_name}"
    
    @staticmethod
    def gradeToLetter(score):
        if score>=90:
            return 'A'
        elif score >=80:
            return 'B'
        else:
            return 'C'
        
s = Student('Abhishek')
print(s.school_name)
s.school_name = 'Instance school' # Creates NEW instance attribute
print(Student.school_name)        # Still the same
Student.school_name = 'New Schol'
print(Student.school_name)
print(Student.changeSchool('KV2'))
print(Student.school_name)
    