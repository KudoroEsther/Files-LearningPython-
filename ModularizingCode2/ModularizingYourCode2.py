#DIFFERENT WAYS TO IMPORT MODULES

#Import the  whole module
import math
#the module's name must be specified when calling a function within it
print(math.sqrt(9)) #this prints the squareroot of 9

#import as an alias
import math as m
print(m.sqrt(25))

#Importing specific functions or variables
from math import sqrt, pi #this imports the functions squareroot and pie from the module called math
print(sqrt(36))
print(pi)

#Importing everythin from a module
from math import *
print(sqrt(49))
print(pi)
