# import relevent packages
import csv
import os

py_file= os.path.abspath(__file__) # path to main.py
py_dir = os.path.dirname(py_file) # path to the parent dir of main.py

# set wd
os.chdir(py_dir)


csv_name = open('data/csv_name.txt','r').read()


# open the CSV file in write mode
with open(f"data/{csv_name}.csv", 'w', encoding='utf-8-sig', newline='') as file:
    
    w = csv.writer(file)
    
    # Write the headers
    w.writerow(["Date",
                "Time",
                "Mood_Level_(1-10)", 
                "Energy_Level_(1-10)",
                "Stress_Level_(1-10)",
                "Activities", 
                "Hours_of_Sleep", 
                "Location",
                "Weather",
                "Temperature_\u00B0C"])    
    
