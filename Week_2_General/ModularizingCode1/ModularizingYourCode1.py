# #FUNCTIONS

# #range()
# for i in range(3):
#     print(i)

# #zip
# names = ["Esther", "Precious", "Kennie"]
# scores = [85,90,75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)

# #map and lambda
# nums = [1,2,3,4] 
# squared = list(map(lambda x: x**2, nums)) #map is used to apply a function to every item of an iterable
# print(squared)

# even_nums = list(filter(lambda x: x%2 == 0, nums)) #filter, extracts the elements that match the specified conditions. In this case, it filters out the even numbers
# print(even_nums)

# # Student Performance & Feedback System

# # Step 1: Input student data
# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + ": "))

# name2 = input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2 + ": "))

# name3 = input("Enter third student name: ")
# score3 = int(input("Enter score for " + name3 + ": "))

# # Step 2: Store in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# # Step 3: Display data
# print("\nStudent Data:")
# #enumerate tracks the index and value
# for indexx, (n, s) in enumerate(zip(names, scores)): #assigns indexx to enumerate(which contains tracks the index and value), assigns n, s to names and scores.
#     print(f"{indexx + 1}. {n} - {s}") #prints out the index number +1 with the individual names and scores on new lines following the format in the print statement

# # Step 4: Summary using built-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance Summary:")
# print("Total Score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# # Step 5: Ranking (using sorted and zip)
# ranked = sorted(zip(scores, names), reverse=True) #sorts according to score from largest value to smallest value
# print("\nRanking:")
# #enumerate takes two arguments, enumerate(iterable, where count starts)

# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# # Step 6: Check data types
# print("\nData Type Checks:")
# print("Type of names:", type(names)) #returns the data type for names
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names)) #returns the unique id of names in memory
# print("ID of scores list:", id(scores))

# # Step 7: Filter passing students (>=50)
# passing = list(filter(lambda s: s >= 50, scores))
# print("\nPassing Scores:", passing)

# # Step 8: Map names to uppercase
# upper_names = list(map(lambda n: n.upper(), names)) #converts the contents of the variable names to upper case
# print("Uppercase Names:", upper_names)

# # Step 9: Use help() to show documentation of len
# print("\nHelp on len():")
# help(len) #tells us the funciton of len


#USER DEFINED FUNCTION
#Defining a function
# def greet():
#     print("Hello, welcome to AI Fellowship")
# greet() #calling the defined function greet

# #Function with an argument
# # name = input("Enter your name")
# def greet(name): #defined a function greet with an argument 'name'
#     print("Hello", name, "welcome to Python learning!")
# greet("Class rep") #calling the function with the parameter 'class rep'
# greet("Ridwan")

# #print(), return and yield keywords inside a function
# #print() doesn't store the value
# def greet(name):
#     print("Hello", name)
# result = greet("Esther")
# print("Result:", result) #prints result as None

# #return() sends a value back to the function caller. The function ends immedaiately once it hits  return
# def add(a,b):
#     return a+b #the function 'add', adds a and b
# result = add(4,6)
# print("The sum is:", result)

# #yield() works like return, but instead of ending the function, it pauses it and remembers its state.
# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1 #this function adds all numbers until i is greater than n

# for number in count_up_to(5):
#     print(number)


# #TYPES OF ARGUMENTS
# #Positional arguments (order matters)
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track, ".")

# introduce("Ngozi", "AI Engineering") #the order in which the parameters are inputted must match the argument order
# introduce("AI Engineering", "Ngozi") #this doesn't match the argument order

# #Keyword arguments (Parameter's name must be explicitly mentiones when calling the function)
# def introduce(name, track):
#     print("\nMy name is", name)
#     print("I am learning", track, ".")

# introduce(name = "Ngozi", track= "AI Engineering") #specifying parameters' names
# introduce(track= "AI Engineering", name= "Ngozi")

# #Default arguments
# def introduce(name, track = "AI Engineering"): #track is given the default value AI Engineering
#     print("My name is", name)
#     print("I am learning", track, ".")

# introduce("Tunji Paul", track= "AI Development") #overwrites the default value of track
# introduce("Paul")


# #Varying length arguments
# #non-keyword (tuple) *args. Collect extra positional arguments into tuple.
# def add_numbers(*args):
#     total = 0
#     for num in args: 
#         total += num #adds nums to total
#     print("\nSum:", total)

# add_numbers(2,4,6) #adds parameters 2,4,6
# add_numbers(10,20,30,40)

# #keyword argument (dictionary). Collects extra keyword arguments into a dictionary
# def student_details(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)

# student_details(name= "Peter", track= "AI Engineering", interest = "Block chain")

# """
# Generate a profile for a bootcamp participant using different types of arguments
# """
# def participant_profile(name, age, track = "AI Development", *skills, **extra_info):
#     profile = f"\n --- Bootcamp Participant Profile ---\n"
#     profile += f"Name: {name}\n"
#     profile += f"Age: {age}\n"
#     profile += f"Track: {track}\n"

#     #Skills from *args
#     if skills:
#         profile += "Skills: "+ ",".join(skills)+ "\n"
#     else:
#         profile += "Skills: Not yet specified\n"

#     #Extra info from *kwargs
#     if extra_info:
#         profile += "Additional Info:\n"
#         for key, value in extra_info.items():
#             profile += f"- {key.capitalize()}: {value}\n"
#     return profile
# print(participant_profile("Peter", 24)) #using positional argument
# print(participant_profile("Ridwan", 29, track= "AI Engineering")) #overwriting  default argument
# print(participant_profile("David", 27, "Data Science", "Python", "Machine Learning")) #adds python and ml to *skills
# print(participant_profile(
#     "Sophia", 30, "Cybersecurity",
#     "Networking", "Ethical Hacking", "Python",
#     interest = "Blockchain", city = "Shanghai", phone= "0812345879"
# )) #adds interest, city, and phone to **extra info


# #NAMESPACES AND SCOPE
# #Global namespace
# employee = "General Employee"

# def IT_department():
#     #Local namespace inside IT_department
#     employee = "Chris(IT)"
#     print("Inside IT Department:", employee)

# def Training_department():
#     #Local namespace inside training_department
#     employee = "Chris(Training)"
#     print("Inside Training Department:", employee)
# print("In Global Namespace:", employee)

# IT_department() #calls employee in the function IT_department
# Training_department()

# #using a built-in namespace function
# print("Length of 'Python':", len("Python"))


# #SCOPE
# x = "global x" #Global Namespace

# def outer():
#     x = "enclosing x" #Enclosing Namespace


#     def inner(): #defining a function inner within the function outer
#         x = "local x" #Local Namespace
#         print("Inside inner:", x) #local wins


#     inner() #calling function inner within outer while still defining the funciton outer
#     print("Inside outer:", x) #Enclosing

# outer() #calling the function outer

# #outer() starts by printing out the content of the local function inner, then it prints out the enclosing function outer()
# print("In global:", x) #Global



# ### Global keyword
# #used to modify a global variable inside a function

# x = 5
# print(x)

# def change_global():
#     global x
#     x = 10 #modifies the content of the global variable x to 10

# change_global()
# print(x)

# ### Nonlocal keyword
# #used in nested functions when you want to modify the variable from the enclosing scope (not global)

# def outer(): #enclosing scope
#     x = "outer x"

#     def inner():
#         nonlocal x
#         x = "changed by inner"
#         print("Inside inner:", x)

#     inner()
#     print("Inside outer:", x)
# outer()
# #this prints out the local function inner with the new content of x that has been changed to "changed by inner", then it prints out the enclosing function outer with the new content of x

# #LAMBDA FUNCTION
# #Uses the syntax lambda arguments:expression
# #Normal function
# def square(x):
#     return x ** 2
# square_lambda = lambda x: x ** 2 #defines a function that generates the squares of a specified number

# print(square(5))
# print(square_lambda(5))

# add = lambda a,b: a+b
# print(add(3,7))

# #Using lambda to apply the square function to a list
# numbers = [1,2,3,4]
# squares = list(map(lambda x: x**2, numbers)) #this squares each element in the list
# print(squares)

# #Using lambda to filter even numbers
# numbers = [10, 15, 20, 25, 30]
# evens = list(filter(lambda x: x%2 == 0, numbers)) #filters out the even numbers
# print(evens)

#Using lambda to sort the tuple within a list
students = [("Ayo", 20), ("Bola", 18), ("Chika", 22)]
#sort by age
sorted_students = sorted(students, key=lambda student: student[1]) #sorts with the index number 1, in this case the ages
print(sorted_students)

students_sorted_descending = sorted(students, key=lambda student: student[1], reverse=True) #sorts from lowest to highest
print(students_sorted_descending)

students_sorted_alphabetically = sorted(students, key=lambda student: student[0]) #sorts with index number 0, in this case with alphabets
print(students_sorted_alphabetically)