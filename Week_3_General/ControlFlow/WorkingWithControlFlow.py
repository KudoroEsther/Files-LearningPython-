#CONDITIONAL STATEMENTS
#If statement
age = 20
if age >= 18:
    print("You are eligibel to vote")

#if-else statement (provides two alternative paths)
wallet = 400
price = 500
if wallet >= 500:
    print("Purchase successful")
else:
    print("Insufficient balance")

#if-elif-else statement (used for multiple conditions)
score = 50
if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Grade C")

#Nested if
age = 19
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")


#Loops
#For loop
#Iterating through each element
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}") #This prints all the element in the list on a new line with the string

#Iterating through each element in a tuple
coordinates = (0.34324, - 0.45284, 0.57477)
for point in coordinates:
    print(f"Point: {point}") #prints each of the element in the tuple on a new line

student = {"name": "Tunde", "age": 16, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}") #prints each key-value pair on a new line

#Iterating through each element in a string
word = "PYTHON"
for char in word:
    print(char) #prints each word in the string on a new line


#WHILE LOOP (repeats a block of code as long as a particular condition is true)
#Using while loop
count = 1
while count <= 5: #stops running when count is greater than 5
    print("Number:", count) #prints Number: count's current value
    count +=1 #adds one to count's current value

#Incrementing with while
num = 1
while num <= 10:
    print(num, end= "-") #end= "" indicates what should be printed at the end of the print execution
    num += 1

#Decrementing with while
timer = 10
while timer > 0:
    print("Countdown: ", timer)
    timer -= 1 #subtracts one from the current value of timer

#While with user input
# password = ""
# while password != "python123":
#     password = input("Entr the password: ") #keeps accepting input from the user until the input is theh same as python123
print("Access Granted!")

#WHILE TRUE
# while True:
#     name = input("Enter your name (type 'exit' to quit): ")
#     if name.lower() == "exit":
#         print("Goodbye!")
#         break
#     print(f"Hello, {name}")


#LOOP CONTROL STATEMENTS (BREAK, CONTINUE, PASS)
#Break (stops loops immediately a condtion is met)
for num in range (1,10):
    if num == 5:
        break #Numbers within a range of 1 - 10 is printed out until num = 5. The loop breaks once num = 5
    print(num)

#Continue (skips the current iteration and moves to the next one)
for num in range (1,6):
    if num == 3: 
        continue #this skips number and prints the next number in the range
    print(num)

#Pass (A placeholder to avoid errors)
for num in range(1,6):
    if num == 3:
        pass #The outcome of num ==3 has not be decided so pass is used to hold the space
    else:
        print(num)

# #While True again
# while True:
#     print("\nMenu:")
#     print("1. Say Hello")
#     print("2. Say Goodbye")
#     print("3. Exit")
# #executes the if-elif-else code block until the user chooses to exit the program, then then break is initiated
#     choice = input("Choose an option: ")
#     if choice == "1":
#         print("Hello")
#     elif choice == "2":
#         print("Goodbye")
#     elif choice == "3":
#         print("Exiting program...")
#         break
#     else:
#         print("Invalid choice, Try again.") #this is executed if the user input a number that's neither 1,2, or 3

#While True for validation
# while True:
#     age = input("Enter your age: ")
#     if age.isdigit():
#         print(f"Your age is {age}")
#         break
#     else:
#         print("Invalid input. Please enter a number.")

#Guess game
secret = "Python"
while True:
    guess = input("Guess the secret word: ")
    #checks if the inputted word is the same as the secret, teh loop is broken using break if the condition is satisfied
    if guess.title() == secret: 
        print("Correct! You guessed the word.")
        break
    else:
        print("Wrong! Try again")

balance = 1000
while True:
    print("\n ATM Menu:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")
    
    if choice == "1":
        print(f"Your balance is {balance}")
    elif choice == "2": #if user chooses the withdrawal option, the program accepts withdrawal amount from the user.
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance: #checks if the inputted amount is less than or equal to balance, if it is, it subtracts the inputted amount from the balance
            balance -= amount
            print(f"Withdrawal successful. New balance: {balance}")
        else:
            print("Insufficient funds.")
    elif choice == "3":
        print("Thank you for using our ATM. Goodbye!")
        break
    else:
        print("Invalid option. Try again")