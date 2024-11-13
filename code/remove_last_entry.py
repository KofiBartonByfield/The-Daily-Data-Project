import pandas as pd

def remove_last_entry(path):
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(path)
    
    # Check if there are rows to delete
    if not df.empty:
        # Remove the last row
        df = df[:-1]
        
        # Write the updated DataFrame back to the CSV file (without the index column)
        df.to_csv(path, index=False)
        print("Last entry removed successfully.")
    else:
        print("The CSV file is empty. No rows to delete.")



import os

py_file= os.path.abspath(__file__) # path to main.py
py_dir = os.path.dirname(py_file) # path to the parent dir of main.py

# set wd
os.chdir(py_dir)





csv_name = open('../data/csv_name.txt','r').read()

path = f"..\data\{csv_name}.csv"

#path = f"../data/{csv_name}.csv"

# read the CSV file into a DataFrame
df = pd.read_csv(path)


# inspect the last entry
print(df.iloc[len(df)-1])

# ask user
user_input = input("Do you want to remove this row? (y or n): ").strip().lower()


# remove last enrty if user responds "y" and show user
if user_input == "y":
    remove_last_entry(path)
    print(pd.read_csv(path))

else:
    print("No changes made to the file.")
    print(pd.read_csv(path))
