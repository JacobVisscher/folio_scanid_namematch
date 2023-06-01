import sqlite3
import csv
import pandas as pd
import math
import os

# set path
path_folder = os.path.join("/home", "rutger", "python")

inputfolder = os.path.join("/home", "rutger", "python", "input")

outputfolder = os.path.join("/home", "rutger", "python", "output_step0")

# set the base string for file names
basestring = "NL-HaNA_2.01.15_"

# set base string for inventaris links
archivelink_incomplete = "NL-HaNA/2.01.15/"

# how many inventarisses are in the archive
print(
    "input the amount on inventarories in the archive. if you are not sure how many there are, be sure to input a number that is at least larger then the amount there are in reality. (for example, if there are around 450 inventories, input 500)"
)
max_arch = input()
max_arch = int(max_arch)

# create csv files
for i in range(1, max_arch):
    filename = "{}{}.csv".format(basestring, i)
    f = open("/" + outputfolder + "/" + filename, "w", newline="")
    f.close()
    continue

print("csv files created")

# iterate through inventory based on nadere toegang document

# set nadere toegang document. document must be in the same folder as this script.
# look at how many indexes you have for the archive, and then put them in the blocks below. 1 block per index file, from target file to the print statement.
target_file = "NT00239_PERSOON.csv"
target_file = os.path.join(inputfolder, "NT00239_PERSOON.csv")
print(target_file)

for i in range(1, max_arch):
    filename = "{}{}.csv".format(basestring, i)
    archivelink = "{}{}/".format(archivelink_incomplete, i)
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
        if archivelink in row["vwz_archivelink"]:
            f = open("/" + outputfolder + "/" + filename, "a", newline="")
            writer = csv.writer(f)
            writer.writerow(
                [
                    row["prs_voornamen"],
                    row["prs_achternaam"],
                    row["vwz_archivelink"],
                    row["prs_UUID"],
                ]
            )
            continue
        continue
    continue

print("first index done!")


target_file = os.path.join(inputfolder, "NT00242_PERSOON.csv")
print(target_file)


for i in range(1, max_arch):
    filename = "{}{}.csv".format(basestring, i)
    archivelink = "{}{}/".format(archivelink_incomplete, i)
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
        if archivelink in row["vwz_archivelink"]:
            f = open("/" + outputfolder + "/" + filename, "a", newline="")
            writer = csv.writer(f)
            writer.writerow(
                [
                    row["prs_voornamen"],
                    row["prs_achternaam"],
                    row["vwz_archivelink"],
                    row["prs_UUID"],
                ]
            )
            continue
        continue
    continue

print("second index done!")


target_file = os.path.join(inputfolder, "NT00243_PERSOON.csv")
print(target_file)
for i in range(1, max_arch):
    filename = "{}{}.csv".format(basestring, i)
    archivelink = "{}{}/".format(archivelink_incomplete, i)
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
        if archivelink in row["vwz_archivelink"]:
            f = open("/" + outputfolder + "/" + filename, "a", newline="")
            writer = csv.writer(f)
            writer.writerow(
                [
                    row["prs_voornamen"],
                    row["prs_achternaam"],
                    row["vwz_archivelink"],
                    row["prs_UUID"],
                ]
            )
            continue
        continue
    continue

print("third index done!")


target_file = os.path.join(inputfolder, "NT00245_PERSOON.csv")
print(target_file)

for i in range(1, max_arch):
    filename = "{}{}.csv".format(basestring, i)
    archivelink = "{}{}/".format(archivelink_incomplete, i)
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
        if archivelink in row["vwz_archivelink"]:
            f = open("/" + outputfolder + "/" + filename, "a", newline="")
            writer = csv.writer(f)
            writer.writerow(
                [
                    row["prs_voornamen"],
                    row["prs_achternaam"],
                    row["vwz_archivelink"],
                    row["prs_UUID"],
                ]
            )
            continue
        continue
    continue

print("fourth index done!")
