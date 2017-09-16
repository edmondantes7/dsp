# advanced_python_dict
# R. Dewey

from collections import OrderedDict
from collections import Counter
import sys
import numpy as np
import pandas as pd
import csv
import re

matched_row = []
matched_row2 = []
matched_row3 = []
with open("faculty.csv", "r") as file:
    # Read file as a CSV delimited by tabs.
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        matched_row.append(row[3])
        matched_row2.append(row[1])
        matched_row3.append(row[2])

c = Counter(matched_row2)
d = Counter(matched_row3)
print(c.items())
print(d.items())


test_dict = {}
test_dict = OrderedDict()
matched_row = []
last = []
with open("faculty.csv", "r") as file:
    # Read file as a CSV delimited by tabs.
    reader = csv.reader(file, delimiter=',')
    # This aspect strips the last names for matching purposes
    for row in reader:
    	new = row[0].split(' ') # Breaks up the names
        matched_row.append(new) 
        last.append(new[-1]) # Creates a list of last names only
        b = len(last)
        c = new[-1]
        print(c)
        if c in test_dict:
            test_dict[c].append((row[1],row[2],row[3]))
        else:
            test_dict[c] = [(row[1],row[2],row[3])]  
    #sorted(test_dict.items())  # Alternative method for sorting the dictionary

print(test_dict)


test_dict = {}
test_dict = OrderedDict()
matched_row = []
last = []
with open("faculty.csv", "r") as file:
    # Read file as a CSV delimited by tabs.
    reader = csv.reader(file, delimiter=',')
    # This aspect strips the last names for matching purposes
    for row in reader:
    	new = row[0].split(' ') # Breaks up the names
        matched_row.append(new) 
        last.append(new[-1]) # Creates a list of last names only
        #c = (new[-1],new[1])
        print(new[-1])
        print(new[0])
        test_dict[new[-1],new[0]] = [(row[1],row[2],row[3])]  
    #sorted(test_dict.items())  # Alternative method for sorting the dictionary

print(test_dict)


with open('test_file2.csv', 'wb') as f:
	w = csv.writer(f)
	w.writerows(test_dict.items())
