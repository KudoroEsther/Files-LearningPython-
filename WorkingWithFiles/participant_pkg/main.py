import csv
from pathlib import Path

participant_file = Path("participant_pkg")
csv_file = participant_file/"csv_file.txt"

name = input("Please enter your name: ").lower().strip()

try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Invalid input, try again.")
    age = int(input("Please enter your age: "))




track = input("Please enter your program track: ").lower().strip()
phone = int(input("Please enter your 11 digits phone number: "))

"""
Define csv file path.
accept inputs, use escape sequences.
Use try except on age input to handle invalid inputs like texts, if invalid show an error message and reprompt.
Validate all inputs using if else, account for empty inputs, incorrect phone number lengths, invalid data types.
Store inputs in a dictionary with keys:name, age, phone, track. Feels like this will be a nested dictionary
Save the dictionary using file_ops.save_participant(), use try and except to catch errors. Use while loop to allow the addition of multiple participants.
After exiting the loop, call file_load_participants() to display a summary.

"""