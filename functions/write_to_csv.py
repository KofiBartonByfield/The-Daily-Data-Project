import csv

def write_to_csv(file_path, data):

    with open(file_path, 'a', encoding='utf-8', newline='') as file:
        w = csv.writer(file)
  
    
        w.writerow(data)
