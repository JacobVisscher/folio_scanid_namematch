from collections import defaultdict
import os
import xml.etree.ElementTree as ET
from Levenshtein import distance as lev
import csv
import pandas as pd
import re
import math

# set inventaris number
print("input the inventaris number: for example '1' ")
inumber = input()
print("input the matching quota between 0 and 1, 0.5 is the recommended lower bound ")
match_percentage = input()
match_percentage = float(match_percentage)
# batch should iterate


# set path
path = "/data/"

path_folder = "/home/rutger/python/"

inputfolder = os.path.join("/home", "rutger", "python", "output_step0")
inputfolder_2 = os.path.join("/home", "rutger", "python", "output_step2")
outputfolder = os.path.join("/home", "rutger", "python", "output_step3")

# set the base string for file names
basestring = "NL-HaNA_2.01.15_"  # change x to location

# set base string for inventaris links
archive_directory = "2.01.15/"

# set directory. /data/2.01.15/118/page    '/data/2.01.15/195/page'
directory = "{}{}{}/page".format(path, archive_directory, inumber)
directory = directory
print(directory)
data = []
data_bulk = []

# set batch name list
names = []

# set name list
name_list_filename = "{}{}.csv".format(basestring, inumber)

print(name_list_filename)
name_list = pd.read_csv(
    "/" + inputfolder + "/" + name_list_filename, na_filter=False, header=None
)

print(name_list)
names = []

# input file
input_list_filename = "sorted_data_{}{}.csv".format(basestring, inumber)

# output file
output_filename = "output_{}{}.csv".format(basestring, inumber)
print(output_filename)
f = open("/" + outputfolder + "/" + output_filename, "w", newline="")
f.truncate
f.close()

# split namelist per batch based on folio nummer NL-HaNA_2.01.15_7.csv

# for loop taking only the part of the batch list with the same folio nummer
# then loop the batch namelist filtered on folio number against the the namelist filtered on folionumber.
# when match is above 70 percent, stop the loop. make a new output file with an additional column in which scan number is put.

# step 1. select input files and build output file V


max_inv = 500
selected_names_dict = defaultdict(list)

# Read the name list file and store the rows in a list
with open("/" + inputfolder + "/" + name_list_filename, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    name_list_rows = list(reader)

# Read the input list file and store the rows in a list
with open("/" + inputfolder_2 + "/" + input_list_filename, newline="") as csvfile2:
    reader2 = csv.reader(csvfile2, delimiter=",")
    input_list_rows = list(reader2)

# Loop over the inventory pages
for i in range(1, max_inv):
    names = []
    uid = []
    string_to_check = "2.01.15/{}//{}//".format(inumber, i)

    # Loop over the rows in the name list
    for row in name_list_rows:
        if string_to_check in row[2]:
            selected_names = row[0].split()
            names.extend(selected_names)
            selected_names = row[1].split()
            names.extend(selected_names)
            uid.append(row[3])

    if len(names) == 0:
        print("No names found for page {}".format(i))
        continue
    print("Names in index for page {}".format(i))
    print(names)

    # Loop over the rows in the input list
    for row2 in input_list_rows:
        selected_names2 = row2[0].split(",")
        selected_names_set = set(selected_names2)
        common_names_set = set(names) & selected_names_set
        percentage = len(common_names_set) / len(names)
        if percentage > match_percentage:
            print("Names in htr output for page")
            print(selected_names2)
            print(percentage)
            print(uid)
            for id in uid:
                selected_names_dict[id].append(selected_names2[0])
            names = "test"
            input_list_rows.remove(row2)
            break


name_dict = {}
with open("/" + inputfolder + "/" + name_list_filename, newline="") as name_file:
    name_reader = csv.reader(name_file, delimiter=",")
    for row in name_reader:
        name_dict[row[3]] = row[0:2]

# Write the output file using the selected_names_dict defaultdict
with open("/" + outputfolder + "/" + output_filename, "w+", newline="") as file:
    writer = csv.writer(file)
    for id, names in selected_names_dict.items():
        # Write the rows with all the information
        if id in name_dict:
            for name in names:
                writer.writerow([id] + name.split(",") + name_dict[id])


# improvemmts

# regularize the names from the namelist

# check ahead. if a matched page is higher then the next matched page, one of these pages are wrong.
