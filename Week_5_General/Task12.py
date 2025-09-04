#User Authentication
from pathlib import Path
import csv

"""
Ask the farmer to create their username and password, check the csv file to be sure that the username doesn't overlap, ask them to confirm their password
store in a csv file with the username as the key and the password as the value
Ask user to login using their username and password, check if username and password are correct by calling the password using the username
"""

workspace= Path("AgroBusiness")
workspace.mkdir(exist_ok=True)
path = workspace/"sign_up.csv"


dict_1 = {}

def sign_up(username, password):
    print("Welcome!")
    # print(f"Your username is {username} and your password is {password}")
    # dict_1[username] = password
    # print(dict_1)

    with open(path, "a", encoding="utf-8", newline="") as f:
        fieldnames = ["Username", "Password"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        dict_1[username] = password
        writer.writeheader()
        writer.writerow(dict_1)

    return f"Your username is {username} and your password is {password}"

for n in range(2):
    username1 = input("Please enter your username: ")
    password1 = input("Please enter your password: ")
    print(sign_up(username1, password1))
    # break