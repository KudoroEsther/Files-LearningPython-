# #Comparison operators
# a = 10
# b = 20
# print(a == b)
# print(a != b)
# print(a > b)
# print(a >= 10)
# print(b <= 25)

# #Student exam result
# score = 75
# print(score >= 50)
# print(score < 50)
# print(score == 100)

#Assignment operators
# x  = 10
# print("Initial value:", x)

# x += 5 
# print("After x += 5:", x)

# x -= 2
# print("After x -= 2:", x)

# x *= 3
# print("After x *=3:", x)

# x /= 4
# print("After /=4", x)

# x %= 3
# print("After %= 3:", x)

# x = 4
# x **= 2
# print("After x **= 2:", x)

# x //= 3
# print("After x //= 3:", x)

# #Example
# balance = 1000
# deposit = 200
# withdraw = 150

# balance += deposit #this adds deposit to balance
# balance -= withdraw
# print("Updated Balance:", balance)

# #Logical Operators
# x = 10
# y = 20

# print(x > 5 and y > 15)
# print(x < 5 or y > 15)
# print(not(x == 10)) #since the specified condition is True, the finally output is False

#Example: Scholarship eligibility
age = 17
score = 85

eligible = (age <18) and (score>80) #Must be younger than 18 and have a score above 18
print("Scholarship Eligible:", eligible)

#Example2: Event access
age = 27
has_ticket = False
can_enter = (age >= 18) and (has_ticket or age <25) #Will be True if age is greater-than-or-equal to 18 AND must have a ticket or be less than 25 years. That is people above 25 must have a ticket
print("Access Granted:", can_enter)