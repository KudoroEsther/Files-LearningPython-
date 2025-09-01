# #RUNTIME ERROR
# #Try Except for a specific exception
# try:
#     x = 10/0
#     print("Result:", x)
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# #Multiple exception
# try:
#     number = int("abc")
#     result = 10/0
# except ValueError:
#     print("Invalid conversion to integer.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# #the finally block
# try:
#     f = open("sample.txt", "r")
#     content = f.read()
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Closing file if it was not opened.")

# #More try-except
# balance = 5000
# print("Welcome to the ATM")
# amount = input("Enter amount to withdraw: ")

# try:
#     amount = float(amount)
#     if amount > balance:
#         raise ValueError("Insufficient funds.")
#     balance -= amount
#     print("Withdrawal successful. New balance: ₦", balance)

# except ValueError as a: #Assigned the error to a
#     print("Error:", a) #this prints out the string: interpretation of the error that occurred and the input responsible for the error
# except Exception as e:
#     print("Unexpected error:", e)
# finally:
#     print("Transaction session closed.")


#SEMANTIC ERROR
#Wrong condition in logic
age = 18
if age > 18: #this logic doesn't consider 18 years olds as eligible to vote
    print("Eligible to vote")
else:
    print("Not eligible")

#Wrong formula/computation
length = 10
width = 5
area = length + width #should be multiplication
print("Area:", area)

#Wrong variable used
marks = [70, 80, 90]
total = marks[0] * marks[1] *marks[2] #should be addition
print("Total:", total)