import sqlite3
import csv
import pandas as pd
import math
import os
import re

# set path
path_folder = os.path.join("/data", "2.01.15_matching_output_files")

inputfolder = os.path.join("/data", "2.01.15_matching_output_files", "output_step0.1")

outputfolder = os.path.join("/data", "2.01.15_matching_output_files", "output_step0.2")

# set the base string for file names
basestring = "NL-HaNA_2.01.15_"

# set base string for inventaris links
archivelink_incomplete = "NL-HaNA/2.01.15/"

list_of_inventarisnummers = []
# iterate through inventory based on nadere toegang document
target_file = os.path.join(inputfolder, "NT00239_PERSOON.csv")
filename = "list_of_entries.csv"
# set nadere toegang document. document must be in the same folder as this script.
# look at how many indexes you have for the archive, and then put them in the blocks below. 1 block per index file, from target file to the print statement.
name_list = pd.read_csv(
    target_file,
    usecols=[
        "prs_achternaam",
        "prs_voornamen",
        "prs_tussenvoegsels",
        "vwz_archivelink",
        "prs_UUID",
    ],
    converters={
        "prs_achternaam": str,
        "prs_voornamen": str,
        "prs_tussenvoegsels": str,
        "vwz_archivelink": str,
        "prs_UUID": str,
    },
)

for index, row in name_list.iterrows():
    # print(row["vwz_archivelink"])
    split = row["vwz_archivelink"].split(",")
    # print(split)
    for entry in split:
        # print(entry)
        pattern = entry.removeprefix(archivelink_incomplete)
        to_remove = re.compile(r"//.*")
        result_string = re.sub(to_remove, "", pattern)
        list_of_inventarisnummers.append(result_string)
        # print(result_string)
        continue
    continue

print(list_of_inventarisnummers)

# iterate through inventory based on nadere toegang document
target_file = os.path.join(inputfolder, "NT00242_PERSOON.csv")
filename = "list_of_entries.csv"
# set nadere toegang document. document must be in the same folder as this script.
# look at how many indexes you have for the archive, and then put them in the blocks below. 1 block per index file, from target file to the print statement.
name_list = pd.read_csv(
    target_file,
    usecols=[
        "prs_achternaam",
        "prs_voornamen",
        "prs_tussenvoegsels",
        "vwz_archivelink",
        "prs_UUID",
    ],
    converters={
        "prs_achternaam": str,
        "prs_voornamen": str,
        "prs_tussenvoegsels": str,
        "vwz_archivelink": str,
        "prs_UUID": str,
    },
)
for index, row in name_list.iterrows():
    # print(row["vwz_archivelink"])
    split = row["vwz_archivelink"].split(",")
    # print(split)
    for entry in split:
        # print(entry)
        pattern = entry.removeprefix(archivelink_incomplete)
        to_remove = re.compile(r"//.*")
        result_string = re.sub(to_remove, "", pattern)
        list_of_inventarisnummers.append(result_string)
        # print(result_string)
        continue
    continue

print(list_of_inventarisnummers)

# iterate through inventory based on nadere toegang document
target_file = os.path.join(inputfolder, "NT00243_PERSOON.csv")
filename = "list_of_entries.csv"
# set nadere toegang document. document must be in the same folder as this script.
# look at how many indexes you have for the archive, and then put them in the blocks below. 1 block per index file, from target file to the print statement.
name_list = pd.read_csv(
    target_file,
    usecols=[
        "prs_achternaam",
        "prs_voornamen",
        "prs_tussenvoegsels",
        "vwz_archivelink",
        "prs_UUID",
    ],
    converters={
        "prs_achternaam": str,
        "prs_voornamen": str,
        "prs_tussenvoegsels": str,
        "vwz_archivelink": str,
        "prs_UUID": str,
    },
)
for index, row in name_list.iterrows():
    # print(row["vwz_archivelink"])
    split = row["vwz_archivelink"].split(",")
    # print(split)
    for entry in split:
        # print(entry)
        pattern = entry.removeprefix(archivelink_incomplete)
        to_remove = re.compile(r"//.*")
        result_string = re.sub(to_remove, "", pattern)
        list_of_inventarisnummers.append(result_string)
        # print(result_string)
        continue
    continue

print(list_of_inventarisnummers)


# iterate through inventory based on nadere toegang document
target_file = os.path.join(inputfolder, "NT00245_PERSOON.csv")
filename = "list_of_entries.csv"
# set nadere toegang document. document must be in the same folder as this script.
# look at how many indexes you have for the archive, and then put them in the blocks below. 1 block per index file, from target file to the print statement.
name_list = pd.read_csv(
    target_file,
    usecols=[
        "prs_achternaam",
        "prs_voornamen",
        "prs_tussenvoegsels",
        "vwz_archivelink",
        "prs_UUID",
    ],
    converters={
        "prs_achternaam": str,
        "prs_voornamen": str,
        "prs_tussenvoegsels": str,
        "vwz_archivelink": str,
        "prs_UUID": str,
    },
)
for index, row in name_list.iterrows():
    # print(row["vwz_archivelink"])
    split = row["vwz_archivelink"].split(",")
    # print(split)
    for entry in split:
        # print(entry)
        pattern = entry.removeprefix(archivelink_incomplete)
        to_remove = re.compile(r"//.*")
        result_string = re.sub(to_remove, "", pattern)
        list_of_inventarisnummers.append(result_string)
        # print(result_string)
        continue
    continue


list_of_inventarisnummers = set(list_of_inventarisnummers)
print(list_of_inventarisnummers)
list_of_inventarisnummers = sorted(list_of_inventarisnummers)
print(list_of_inventarisnummers)

f = open("/" + outputfolder + "/" + filename, "w", newline="")
writer = csv.writer(f)
writer.writerows([list_of_inventarisnummers])
