#main.py Project entry point

import data
import utils

#Adding some students
data.add_student("Paul", "AI Engineering") #uses positional arguments
data.add_student("Blessing", "AI Development")

#print formatted student records
for s in data.get_students(): #this should return the student data inputted using .add_student
    print(utils.format_students(s)) 
#the last line calls the function format_students from utils and prints out students using the specified format