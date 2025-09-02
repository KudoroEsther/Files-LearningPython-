#Helper Module
import csv
from pathlib import Path
participant_file = Path("participant_pkg")
csv_file = participant_file/"csv_file.txt"

def save_participant(file_path, participant_dict):
    """
    Appends participant details to a CSV file (creates the file and writes a header if it doesn't exist.)    
    """
    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(participants)
    #Plans: I want it to accept user inputs regarding their details, unpack into a single variable, convert to a list and add to append not write to a CSV file
    #Use with open(csv_file, "a", newline= "", encoding)
    print(" ")

def load_participant():
    """
    Reads all participants from the CSV and returns them as a list of dictionaries.
    """
    #plans: use enumerate and join to read the rows from save_participant, use tuple unpacking to load variables into rows (might not be needed). The output has to be a list of dictionarires, how should I go about it?

    print(" ")