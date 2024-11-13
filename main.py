# Data Entry

# import libraries
import os
import os.path as op


# extract wd
py_file= os.path.abspath(__file__) # path to main.py
py_dir = os.path.dirname(py_file) # path to the parent dir of main.py

# set wd
os.chdir(py_dir)

# extract cvs name
csv_name = open('data/csv_name.txt','r').read()




# fill in csv
if op.isfile(f"data/{csv_name}.csv"):
    
    # file already exists
    # run code to input data
    exec(open('code/data_form.py').read())



else:
    # create file
    exec(open('code/create_form.py').read())
    # run code to input data
    exec(open('code/data_form.py').read())








