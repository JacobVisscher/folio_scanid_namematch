import os
import xml.etree.ElementTree as ET
from Levenshtein import distance as lev
import csv
import math
import pandas as pd
import re

# set inventaris number
print("input the inventaris number: for example '1' ")
inumber = input()

# set path
path = "/data/"

path_folder = "/home/rutger/python/"

inputfolder = os.path.join("/home", "rutger", "python", "output_step0")

outputfolder = os.path.join("/home", "rutger", "python", "output_step1")

# set the base string for file names
basestring = "NL-HaNA_2.01.15_"

# set base string for inventaris links
archive_directory = "2.01.15/"

# set directory.
directory = "{}{}{}/page".format(path, archive_directory, inumber)
directory = directory
print(directory)
data = []
data_bulk = []

# set name list
name_list_filename = "{}{}.csv".format(basestring, inumber)

print(name_list_filename)
name_list = pd.read_csv(
    "/" + inputfolder + "/" + name_list_filename, na_filter=False, header=None
)
print(name_list)


# calculate the amount of batches. Currently, the code works with batches of 50 pages. You can work with smaller or larger batches if you want. If you work with larger batches, the chance of overmatching increases, if you work with smaller batches, the code will have to run more iterations.
names = []
pages = 50
xml_pages = 0
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".xml"):
        xml_pages = xml_pages + 1

print(xml_pages)
batch_amount = math.ceil(xml_pages / pages)
print("batch amount is")
print(batch_amount)
e = 0

# create lists of names per batch from the inventaris number index.
if xml_pages > pages:
    print("yes")
    for i in range(batch_amount):
        begin_batch = e * pages
        end_batch = (e + 1) * pages
        print(begin_batch, end_batch)
        output_filename = "batch_{}{}_{}-{}.csv".format(
            basestring, inumber, begin_batch, end_batch
        )
        print(output_filename)
        f = open("/" + outputfolder + "/" + output_filename, "w", newline="")
        f.truncate
        f.close()
        for i in range(begin_batch, end_batch):
            full_string = "NL-HaNA/{}{}//{}/".format(
                archive_directory, inumber, i
            )  # NL-HaNA/2.01.15/153//10//
            full_string = full_string
            for index, row in name_list.iterrows():
                if full_string in row[2]:
                    data.append([row[0], row[1], row[2], row[3]])
                    continue
                continue
            continue
        file = open("/" + outputfolder + "/" + output_filename, "w+", newline="")
        # writing the data into the file
        with file:
            write = csv.writer(file)
            write.writerows(data)
        data = []
        e = e + 1
        print(e)
        continue
if xml_pages < pages:
    print("no")
    begin_batch = e * pages
    end_batch = (e + 1) * pages
    print(begin_batch, end_batch)
    output_filename = "batch_{}{}_{}-{}.csv".format(
        basestring, inumber, begin_batch, end_batch
    )
    print(output_filename)
    f = open("/" + outputfolder + "/" + output_filename, "w", newline="")
    f.truncate
    f.close()
    for i in range(begin_batch, end_batch):
        full_string = "NL-HaNA/{}{}//{}/".format(
            archive_directory, inumber, i
        )  # NL-HaNA/2.01.15/153//10//
        full_string = full_string
        for index, row in name_list.iterrows():
            if full_string in row[2]:
                data.append([row[0], row[1], row[2], row[3]])
                continue
            continue
        continue
    file = open("/" + outputfolder + "/" + output_filename, "w+", newline="")
    # writing the data into the file
    with file:
        write = csv.writer(file)
        write.writerows(data)
    data = []
    e = e + 1
    print(e)
