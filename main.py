#main.py
#Importing the whole package
import my_package

print(my_package.add(5,3)) #this calls the function from my_package without having the call the module containing the function
print(my_package.subtract(10,4))
print(my_package.capitalize_text("python"))

#importing specific modules
from my_package import string_utils #this imports the module string_utils from the package my_package

#a module cannot be called directly without importing the module from the package
print(string_utils.reverse_text("hello"))