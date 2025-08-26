import first
import second

#Using the functions in first.py file
print("=== Math Functions ===")
print("5 + 3 =", first.add(5,3)) #calling the function add from the file first.py
print("10 - 4 =", first.subtract(10,4))
print("6 * 7 =", first.multiply(6,7))
print("20 / 5 =", first.divide(20,5))

#Using the function in the second.py file
print("\n=== String Funcitons ===")
print(second.greet("Ridwan"))
print("Reverse of 'Python' =", second.reverse_string("Python"))
print("Character count in sentence =", second.count_characters("Python modules are powerful"))
print("Word count in sentence =", second.count_words("Python modules are different"))