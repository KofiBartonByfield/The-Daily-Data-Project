import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox


# set wd
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# define path to the CSV file
csv_name = open('../data/csv_name.txt','r').read()
path = f"../data/{csv_name}.csv"


# function to remove entry
def remove_last_entry():
    df = pd.read_csv(path)
    if not df.empty:
        df = df[:-1]
        df.to_csv(path, index=False)
        messagebox.showinfo("Success", "Last entry removed successfully.")
    else:
        messagebox.showwarning("Warning", "The CSV file is empty. No rows to delete.")


# function to load last entry
def load_last_entry():
    
    # clear existing data display
    for widget in data_frame.winfo_children():
        widget.destroy()  
    
    # if file exists
    if os.path.isfile(path):
        df = pd.read_csv(path)
        
        # if there is data inside
        if not df.empty:
            
            # get the last row of the df
            last_row = df.iloc[-1] 
            for i, (col_name, value) in enumerate(last_row.items()):
                tk.Label(data_frame, 
                         text=col_name + ":",
                         font=("TkDefaultFont", 10, "bold"),
                         anchor="w").grid(row=i, 
                                          column=0, 
                                          sticky="w", 
                                          padx=5, 
                                          pady=2)
                tk.Label(data_frame, 
                         text=str(value), 
                         anchor="w").grid(row=i, 
                                          column=1, 
                                          sticky="w", 
                                          padx=5, 
                                          pady=2)
        else:
            tk.Label(data_frame, 
                     text="The CSV file is empty.").grid(row=0,
                                                         column=0, 
                                                         columnspan=2, 
                                                         padx=5, 
                                                         pady=5)
    else:
        tk.Label(data_frame, text="Invalid file path.").grid(row=0, 
                                                             column=0, 
                                                             columnspan=2, 
                                                             padx=5, 
                                                             pady=5)


# ask user to confirm removal of last entry
def confirm_and_remove():
    if os.path.isfile(path):
        response = messagebox.askyesno(
            "Confirm", "Do you want to remove the last row?"
        )
        if response:
            remove_last_entry()
            load_last_entry()
    else:
        messagebox.showerror("Error", "Invalid file path. Please check the path.")




# Tkinter GUI setup
root = tk.Tk()
root.title("CSV Row Remover")


# frame for displaying last entry data in a landscape format
data_frame = tk.Frame(root)
data_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Confirm button
tk.Button(root, text="Remove Last Entry", command=confirm_and_remove).grid(row=1, column=0, columnspan=2, pady=10)

# Load the last entry on startup
load_last_entry()

root.mainloop()