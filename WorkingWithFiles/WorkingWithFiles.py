#getting the current working directory
import os
from pathlib import Path

# print("Current working directory:", os.getcwd())


# #Absolute vs Relative path
# #Absolute path
# absolute_path = r"C:\Users\ncc\Desktop\my_path.py" #r is used to tell python to ignore the escape sequences \

# #Relative path example
# relative_path = r"my_path.py"

# print("Absolute Path:", absolute_path)
# print("Relative Path:", relative_path)


# #Joining paths
# folder = "C:/Users/Chris/Desktop"
# filename = "my_path.py"
# #joins the filepath to the folder path
# path = os.path.join(folder, filename)
# print("Full path:", path)

# pth = r"C:\Users\ncc\Desktop\Learning_Python\Week_4_General\WorkingWithFiles\WorkingWithFiles.py"

# #checks if the filename in variable path exists or not
# if os.path.exists(pth):
#     print("Yes, the file exists!")
# else:
#     print("File not found")


# #Using pathlib(modern way)

# #Current working director
# print("current_directory:", Path.cwd())

#Creating a Path object
# i
# #Checking if a file exists
# print("File exists:", file.exists()) #noticed that this only works if you're in the folder containing the file

# #Combining paths
# folder = Path("C:/Users/Chris/Desktop")
# full_path = folder / "myfile.txt"
# print("Full path", full_path)

# #Navigating folders with pathlib
# print("\n\nParent folder:", Path.cwd().parent)

# #Listin all files in a directory
# for file in Path.cwd().iterdir():
#     print(file)