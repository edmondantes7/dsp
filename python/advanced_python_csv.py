# Metis Python Advanced Questions
# R. Dewey 9/15/2017
# Write email addresses

from collections import OrderedDict
import sys
import numpy as np
import pandas as pd
import csv
import re

matched_row = []
with open("faculty.csv", "r") as file:
    # Read file as a CSV delimited by tabs.
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        matched_row.append(row[3])

with open('emails.csv', 'wb') as f:
  w = csv.writer(f, delimiter=' ')
  w.writerows(matched_row)
