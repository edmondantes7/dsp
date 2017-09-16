# Regular Expression Python Code
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
domain = []
with open("faculty.csv", "r") as file:
    # Read file as a CSV delimited by tabs.
    reader = csv.reader(file, delimiter=',')
    headers = reader.next()
    for row in reader:
        matched_row.append(row[3])
        matched_row2.append(row[1])
        matched_row3.append(row[2])
    #print(matched_row)
    for emails in matched_row:
    	domain.append(re.search('@.*', emails).group())
    	

c = Counter(matched_row2)
d = Counter(matched_row3)
f = Counter(domain)
print(c.items())
print(d.items())
print(f.items())
