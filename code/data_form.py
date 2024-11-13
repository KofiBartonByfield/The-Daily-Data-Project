# import libraries
import tkinter as tk
from datetime import date
import os
from ctypes import windll
from time import strftime



py_file= os.path.abspath(__file__) # path to main.py
py_dir = os.path.dirname(py_file) # path to the parent dir of main.py

# set wd
os.chdir(py_dir)






# import homemade functions
from fetch_weather_temperature import fetch_weather
from fetch_location import fetch_location
from write_to_csv import write_to_csv

# define path
csv_name = open('../data/csv_name.txt','r').read()



csv_file = f"../data/{csv_name}.csv"

# imporve resolution
windll.shcore.SetProcessDpiAwareness(1)


# colours and fonts
bg_color = "white"
accent_color = "#91cce1"
text_color = "black"
input_font = ("Garamond", 15)
label_font = ("Garamond", 16, "bold")

# function
def submit_data(event=None):
    # pull weather api key 
    api_key = os.getenv("OPENWEATHER_API_KEY")
    
    # user information
    today = date.today()
    now = strftime("%H:%M")
    mood = mood_entry.get()
    energy = energy_entry.get()
    stress = stress_entry.get()
    activities = activities_entry.get()
    sleep_hours = sleep_entry.get()
    location = fetch_location()
    weather, temp = fetch_weather(location, api_key)

    # group the information
    data_to_write = [today, 
                     now,
                     mood, 
                     energy, 
                     stress, 
                     activities, 
                     sleep_hours, 
                     location, 
                     weather, 
                     temp]
    
    # put the info into the csv
    write_to_csv(csv_file, data_to_write)

    # close the window
    root.destroy()

# Tkinter setup
root = tk.Tk()
root.title("Data Collection Form")
root.configure(bg=bg_color)


# frame for input fields
form_frame = tk.Frame(root, bg=bg_color, padx=20, pady=20)
form_frame.pack(padx=10, pady=10)

# Define labels and entries with styling
fields = [("Mood Level (1-10):", "mood_entry"), 
          ("Energy Level (1-10):", "energy_entry"), 
          ("Stress Level (1-10):", "stress_entry"), 
          ("Activities:", "activities_entry"), 
          ("Hours of Sleep:", "sleep_entry")]

entries = {}

for idx, (label_text, entry_name) in enumerate(fields):
    
    # label details
    label = tk.Label(form_frame, 
                     text=label_text, 
                     bg=bg_color, 
                     fg=text_color, 
                     font=label_font)
    # show labels
    label.grid(row=idx, column=0, sticky="w", pady=5)
    
    # input entries
    entry = tk.Entry(form_frame, font=input_font, width=10)
    entry.grid(row=idx, column=1, padx=5, pady=5)
    entries[entry_name] = entry  # Store each entry widget


# save the entries as variables
mood_entry = entries["mood_entry"]
energy_entry = entries["energy_entry"]
stress_entry = entries["stress_entry"]
activities_entry = entries["activities_entry"]
sleep_entry = entries["sleep_entry"]


# submit button styling
submit_button = tk.Button(root, text="Submit", 
                          command=submit_data, 
                          font=label_font, 
                          bg=accent_color, 
                          fg="white")
submit_button.pack(pady=10)

# function to move to the next field on "Enter" or submit if on the last field
def focus_next(event):
    widget = event.widget  # Get the current widget with focus
    next_widget = widget.tk_focusNext()  # Get the next widget in line
    
    # If we are in the last entry field, call submit_data
    if next_widget is submit_button:
        submit_data()
    else:
        next_widget.focus()  # Move to the next widget

# bind the Enter key to focus_next for each entry field
for entry in [mood_entry, energy_entry, stress_entry, activities_entry, sleep_entry]:
    entry.bind('<Return>', focus_next)


root.mainloop()
