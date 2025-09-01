#Setting Up
import json
import csv
from pathlib import Path

# worskspace = Path("workspace_files")
# #exist_ok check if a file exists ir not
# worskspace.mkdir(exist_ok=True)
# file_path = worskspace/"notes.txt"
# file_path

# #Creating a file using w
# # fun = open(file_path, "w", encoding="utf-8")
# # fun.write("This is the first line in notes.txt\\n")
# # fun.close()

# # #Creating a file using exclusive create "x", x throws error if the file already exists
# # fun = open(worskspace/"Created_once.txt", "x", encoding="utf-8")
# # fun.write("This fill will only be created if it doesn't exist.\n")
# # fun.close()

# #Opening a file
# # #this will overwrite
# # fun = open(file_path, "w", encoding="utf-8")
# # fun.write("Replaced the old content with this line.\n")
# # fun.close()

# #Writing to a file
# fun = open(file_path, "w", encoding="utf-8")
# fun.write("Shopping List:\n")
# fun.write(" - Rice\n")
# fun.write(" - Beans\n")
# fun.write(" - Garri wine\n")
# fun.close()

# #Appending to a file using "a"
# fun = open(file_path, "a", encoding="utf-8")
# fun.write(" - Groundnut oil\n")
# fun.write(" - Maggi\n")
# fun.close()

# #READING FROM A FILE
# #Reading the whole file using read()
# fun = open(file_path, "r", encoding="utf-8")
# content = fun.read()
# fun.close()
# print(content)

# #Read line-by-line using readline()
# fun = open(file_path, "r", encoding="utf-8")
# print("First line:", fun.readline().rstrip())
# print("Next line:", fun.readline().rstrip())
# print("Next line:", fun.readline().rstrip())

# #Read as a list of lines using readlines()
# fun = open(file_path, "r", encoding="utf-8")
# lines = fun.readlines() #converts the texts to a list and outputs each line as an element in the list
# fun.close()
# print(lines)
# print("Lines list:", [element.rstrip() for element in lines]) #rstrip was used in removing the escapes sequences from the right side of texts

# #Iterating over lines (more memory-friendly)
# fun = open(file_path, "r", encoding="utf-8")
# for line in fun:
#     print("-->", line.rstrip()) #this prints all 
# fun.close()

# #Opening a file safely
# #this closes the file without having to use the .close() method
# with open(file_path, "w", encoding="utf-8") as fun:
#     fun.write("My Todo List:\n")
#     fun.write(" - Revise Python file handwriting\n")
#     fun.write(" - Practice error handling within a function")
#     fun.write(" - Practice JSON & CSV\n")

# #Appending safely
# with open(file_path, "a", encoding="utf-8") as f:
#     f.write(" - Build a small project\n")


#HANDLING ERRORS
# workspace = Path("workspace_files")
# workspace.mkdir(exist_ok=True)

# #Trying a read a file that doesn't exist
# try:
#     with open(workspace/"missing_file.txt", "r") as f: #tries to write to missing_file.txt, but since the file doesn't exist FileNotFoundError will be triggered
#         content = f.read()
#         print("File content:", content)
# except FileNotFoundError:
#     print("Oops! That file doesn't exist yet.")
#     print("Let's create it first!")

#     #Now create the file
#     with open(workspace / "missing_file.txt", "w") as f: #this creates the file missing_file.txt after dealing with the error using except:
#         f.write("Now I exist!")
#     print("File created successfully!")


#Checking if a file exists before using them
# workspace = Path("workspace_files")
# file_path = workspace / "notes.txt"

# #check if our file exists
# #This program essentially check if a file exists, prints out the file name, file size and opens the file, if not, it prints out the contents of else
# if file_path.exists():
#     print(f"Found the file: {file_path.name}")
#     #.st_size is used to get the size of a file in bytes, it is an attribute of .stat()
#     file_size = file_path.stat().st_size
#     print(f"File size: {file_size} bytes") 

#     #Read and show the content
#     with open(file_path, "r", encoding="utf-8") as f:
#         content = f.read()
#         #this prints out the first 50 characters in the file
#         print(f"Content preview: {content[:50]}...")
# else: 
#     print(f"File {file_path.name} doesn't exist")
#     print("You might want to create it first!")


# #WORKING WITH JSON FILES
# workspace = Path("workspace_files")

# #Creating a mini database of students
# student_data = {
#     "name": "Oyindamola",
#     "age": 16,
#     "courses": ["Python", "Data Science", "Wev Development"],
#     "grades": {"Python": "A", "Data Science": "B+", 'Web Development': "A-"},
#     "is_graduated": False
# }

# #Saving the data to a JSON file
# json_file = workspace/"student_data.json" #this joins the filename to the path in workspace
# with open(json_file, "w", encoding="utf-8") as f:
#     #this dumps the contents of student_data into the opened file with alias f
#     json.dump(student_data, f, indent=2) #indent=2 is to make it pretty and readable

# print("Student data saved to JSON file!")

# #Reading it back
# with open(json_file, "r", encoding="utf-8") as f:
#     loaded_data = json.load(f) #load is the equivalent of read() in pathlib

# print("\nData read from JSON file:")
# print(f"Student name: {loaded_data["name"]}") #this accesses the key 'name' from loaded_data
# print(f"Age: {loaded_data["age"]}")
# print(f"Course: {", ".join(loaded_data["courses"])}") #this prints the value for courses separated by commas, the output is not a lit
# print(f"Python grade: {loaded_data["grades"]["Python"]}") #this outputs the grade for python



#WORKING WITH CSV
# workspace = Path("workspace_files")
# csv_file = workspace / "students.csv" #joined the filename to the filepath

# # Create sample student data
# students = [
#     ["Name", "Age", "Course", "Grade"],  # Header row
#     ["Precious", 20, "Python", "A"], ["Favour", 22, "JavaScript", "B+"],
#     ["Ore", 21, "Python", "A-"],
#     ["Susan", 23, "Data Science", "A"]
# ]

# # Write data to CSV file
# with open(csv_file, "w", newline="", encoding="utf-8") as f: #newline= ensures that only csv newline formatting is applied, bascially, it disables python's newline formatting
#     writer = csv.writer(f)
#     writer.writerows(students)  # Write all rows at once

# print("Student data written to CSV file!")

# # Read the CSV file back
# print("\nReading CSV file:")
# with open(csv_file, "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
    
#     for row_number, row in enumerate(reader):
#         if row_number == 0:  # Header row
#             print(f"Headers: {' | '.join(row)}")
#             print("-" * 40)
#         else:  # Data rows
#             name, age, course, grade = row #kinda like tuple unpacking, it unpacks the contents of row into the variables
#             print(f"{name} ({age} years) - {course}: {grade}")

#Working with multiple files
workspace = Path("workspace_files")
input_file = workspace / "original.txt" #joined the filename to the filepath
output_file = workspace / "processed.txt"

# Create an input file with some text
sample_text = """hello world
python programming
file handling tutorial
learning is fun"""

with open(input_file, "w", encoding="utf-8") as f:
    f.write(sample_text) #open original.txt and write the content of sample_text into input_file

print("Created input file")

#opening input_file to be read with an alias infile
with open(input_file, "r", encoding="utf-8") as infile, \
     open(output_file, "w", encoding="utf-8") as outfile:
    #writing to output_file with outfile as an alias
    
    line_number = 1
    for line in infile:
        # Process each line: make it uppercase and add line numbers
        processed_line = f"Line {line_number}: {line.strip().upper()}\n"
        outfile.write(processed_line)
        line_number += 1

print("File processing complete!")