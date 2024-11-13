# import relevent packages
import csv


# open the CSV file in write mode
with open("../data/csv_name.csv", 'w', encoding='utf-8-sig', newline='') as file:
    
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
    
