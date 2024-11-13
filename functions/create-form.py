# import relevent packages
import csv
import pandas as pd


# define the path of we will be working in
path = "C:/Users/15kof/OneDrive/Documents/Coding Projects/Data Form/"


# open the CSV file in write mode
with open(f"{path}data.csv", 'w', encoding='utf-8-sig', newline='') as file:
    
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
    
# Read the CSV file into a DataFrame
df = pd.read_csv(f"{path}data.csv")

# Display the DataFrame
print(df)