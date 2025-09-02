# #CLASSES

# #Initialization
# class Student:
#     def __init__(self, name, course, level): #sets up the basic information about the class Student
#         print("Creating a new student...")
#         self.name = name
#         self.course = course #this assigns course as an attribute of Student
#         self.level = level
#         print(f"Student {name} has been created.")

# #__init__ runs automatically
# Name = Student("Esther Kudoro", "Elect/Elect", 500)

# #How init and self work together
# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: Creating student object...")
#         self.name =name
#         self.state_of_origin = state #Step 3: assigns course to this object
#         self.course = course
#         self.student_id = self.generate_id() #Generates ID for this object
#         print(f"Step 6: {self.name} from {self.state_of_origin} is ready")

#     def generate_id(self):
#         import random
#         return f"UNISAIL {random.randint(1000, 9999)}"

# #Creating an instance
# ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")

# print(ayo.name) #prints the 
# print(ayo.student_id)

# #MORE EXAMPLE
# class PhoneUser:
#     def __init__(self, name, network):
#         self.name = name
#         self.network = network
#         self.airtime = 0
#         print(f"{self.name} joined {self.network} network")

#     def buy_airtime(self, amount):
#         self.airtime += amount #self ensures it goes to the RIGHT person
#         return f"{self.name} now has ₦{self.airtime} airtime"
    
# #creating instances of multiple users
# esther = PhoneUser("Esther Kudoro", "MTN")
# mary = PhoneUser("Mary Adeoye", "Airtel")

# print(esther.buy_airtime(500)) #500 is the amount which is an argument in the function buy_airitime
# print(mary.buy_airtime(1000)) #calling the function buy_airtime from the class

# print(esther.airtime) #this prints out the airtime amount for the instance esther
# print(mary.airtime)


# #Attributes
# #Defining attributes of a student
# class Student:
#     def __init__(self, name, course, level, state_of_origin):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.state_of_origin = state_of_origin
#         self.cgpa = 0.0

# Bolaji = Student("Bolaji Hamid", "Biochemistry", 300, "Ogun State")

# print(f"Your name is {Bolaji.name}, you're studying {Bolaji.course}, you are in {Bolaji.level} level and you are from {Bolaji.state_of_origin}")

# #Types attributes

# #instance attributes: Unique to each object
# student1 = Student("Anthony Joshua", "Engineering", 200,"Ogun")
# student2 = Student("Mary Adeoye", "Medicine", 400, "Lagos")

# print(student1.name)
# print(student2.level)

#Class attributes
class Student:
    university = "Federal University of Technology Akure"

    def __init__(self, name, course):
        self.name = name
        self.course = course
    
student1 = Student("Anthony Joshua", "Engineering")
student2 = Student("Mary Adeoye", "Medicine")

print(Student.university)
print(student1.university)
print(student2.university)