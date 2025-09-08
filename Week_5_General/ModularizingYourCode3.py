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

# #Class attributes
# class Student:
#     university = "Federal University of Technology Akure"

#     def __init__(self, name, course):
#         self.name = name
#         self.course = course
    
# student1 = Student("Anthony Joshua", "Engineering")
# student2 = Student("Mary Adeoye", "Medicine")

# print(Student.university)
# print(student1.university)
# print(student2.university)



# # #METHODS
# class Student:
#     def __init__(self, name, course, level):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.cgpa = 0.0 
#         self.fees_paid = False
    
#     #Method: action the student can do
#     def pay_school_fees(self):
#         self.fees_paid = True
#         return f"{self.name} has paid school fees for {self.level} level."
    
#     def register_courses(self):
#         if self.fees_paid:
#             return f"{self.name} has registered courses for {self.course}."
        
#     #Method: calculates CGPA
#     def calculate_cgpa(self, grades):
#         if grades:
#             self.cgpa = sum(grades)/len(grades)
#             return f"{self.name}'s CGPA is now {self.cgpa:.2f}"
#         return "No grades provided."


# # #Using methods
# # Esther = Student("Esther Kudoro", "Engineering", 500)
# # print(Esther.pay_school_fees())
# # print(Esther.register_courses())
# # print(Esther.calculate_cgpa([4.5, 4.64, 4.89, 4.98, 5.0]))

# #Types of methods
# #Instance methods: works with specific object data
# #self refers te the specific student
#     def pay_school_fees(self):
#         return f"{self.name} has paid school fees"
    
# #Class methods: works with class-level data
# #this applies the defines method to all instances
# @classmethod
# def get_university(cls):
#     return cls.university

# #Static methods: don't need object or class data
# #Arguments can be omitted when defining methods within the class
# @staticmethod
# def academic_calendar():
#     return "Academic session runs from September to July."


#HOW ATTRIBUTES AND METHODS WORK TOGETHER
class BankAccount:
    def __init__(self, owner, bank_name, balance = 0):
        #Attributs: what the account has
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        self.account_number = self.generate_account_number()

    #Methods: what the account can do
    def deposit(self, amount):
        """Adds money to the account."""
        if amount > 0:
            self.balance += amount #Method changes attribute
            return f"₦ {amount:,} deposited to {self.owner}'s {self.bank_name} account. New balance: ₦{self.balance:,}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        "Removes money from the account."
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} withdrawn from {self.owner}'s account. New balance: ₦{self.balance:,}"
        return "Insufficient funds or invalid amount."
    
    def transfer(self, amount, recipient):
        """Transfer money to another account"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"₦{amount:,} transferred from {self.owner} to {recipient}. Remaining balance: ₦{self.balance}"
        return "Transer failed: Insufficient funds."
    
    def check_balance(self):
        """Checks current balance"""
        return f"{self.owner}'s {self.bank_name} account balance: ₦{self.balance:,}"
    
    def generate_account_number(self):
        """Generates a unique account number"""
        import random 
        return f"01{random.randint(10000000, 99999999)}"
    
#creating and using the account
esther_account = BankAccount("Esther Kudoro", "Kuda Bank", 5000)

#Attributes (characteristics)
print(f"Owner: {esther_account.owner}")
print(f"Account Number: {esther_account.account_number}")
print(f"Balance: {esther_account.balance}")

#Methods (actions)
print(esther_account.deposit(250000))
print(esther_account.withdraw(1000))
print(esther_account.transfer(15000, "Mary Adeoye"))