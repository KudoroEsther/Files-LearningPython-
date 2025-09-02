#TASK 7

#Task 3 Days and activities pairing
week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
activity = []
# day_activity = {}

for i in week_days[::3]:
    act = input(f"Please input an activity for {i}: ")
    activity.append(act)

day_activity = zip(week_days[::3], activity)
    # day_activity = {week:acti for week, acti in zip(week_days[::3], activity) }

print("Day \t\tActivity")
for (key, value) in day_activity:
    print(f"{key}: \t{value}")



# #Task 4 Unique Members registration
# names = input("Please enter three names separated by commas: ").strip().split(", ")
# set_names = set(names)

# dict_names= {}
# dict_names = {names: len(names) for names in set_names}

# print(dict_names)



# #Task 5 Contact Quick Lookup
# names = ("Esther", "Eunice", "Elizabeth")
# phone_number = ("09012345678", "08012345678", "07012345678")

# details = dict(zip(names, phone_number))
# # print(details )

# print("Contact Lookup".center(50,"."))
# try:
#     look_up = input("Please enter a name: ").title()
#     if look_up in names:
#         print("Name \t Phone number")
#         print(f"{look_up} -> {details[look_up]}")
#     else:
#         print("Contact hasn't bee registered")
# except ValueError as v:
#     print("Error", v)
# except TypeError as t:
#     print("Error", t)
# except Exception as e:
#     print("Error", e)