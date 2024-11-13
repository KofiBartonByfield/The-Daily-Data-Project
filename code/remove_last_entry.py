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




path = "../data/data.csv"

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
