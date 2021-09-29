
#creating the parent class for highschool
#parent class attributes include basic information like name, address,
#age, emergency contact info, and classes
class CHSmember:
    name = 'No Name Provided'
    address = 'No Address Provided'
    age = 0
    emer_contact = '123-456-7890'
#when this classes attribute is shared to the child classes,
#the student class will have multiple classes taken so i made the
#value of this attribute a list
    classes = ['']

#first child class is the student class
#student class includes current gpa, graduation year,
#and their current grade year
class Student(CHSmember):
    cur_gpa = 0
    grad_year = 0
    cur_grade_year = 0


#second child class is the teacher class
#teacher class includes base pay, college degree,
#and the number of students they are responsible for
class Teacher(CHSmember):
    base_pay = 15.00
    college_degree = ''
    num_students = 0
    
