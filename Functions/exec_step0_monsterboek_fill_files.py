import sqlite3
import csv
import pandas as pd
import math
import os


def run(toegangsnummer):
    # set path
    path_folder = os.path.join("/data", "2.01.15_matching_output_files")

    inputfolder = os.path.join(
        "/data", "2.01.15_matching_output_files", "output_step0.1"
    )

    inputlist_folder = os.path.join(
        "/data", "2.01.15_matching_output_files", "output_step0.2"
    )

    outputfolder = os.path.join(
        "/data", "2.01.15_matching_output_files", "output_step0"
    )

    # set the base string for file names
    basestring = "NL-HaNA_{}_".format(toegangsnummer)
    # set base string for inventaris links
    archivelink_incomplete = "NL-HaNA/{}/".format(toegangsnummer)

    # how many inventarisses are in the archive
    input_list_file = os.path.join(inputfolder, "list_of_entries.csv")
    input_list = pd.read_csv(input_list_file)
    # create csv files
    for i in input_list:
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

    for i in input_list:
        filename = "{}{}.csv".format(basestring, i)
        archivelink = "{}{}/".format(archivelink_incomplete, i)
        name_list = pd.read_csv(
            target_file,
            usecols=[
                "prs_achternaam",
                "prs_voornamen",
                "prs_tussenvoegsels",
                "prs_initialen",
                "vwz_archivelink",
                "prs_UUID",
            ],
            converters={
                "prs_achternaam": str,
                "prs_voornamen": str,
                "prs_tussenvoegsels": str,
                "vwz_archivelink": str,
                "prs_initialen": str,
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
                        row["prs_tussenvoegsels"],
                        row["prs_initialen"],
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

    for i in input_list:
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
                        row["prs_tussenvoegsels"],
                        "",
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
    for i in input_list:
        filename = "{}{}.csv".format(basestring, i)
        archivelink = "{}{}/".format(archivelink_incomplete, i)
        name_list = pd.read_csv(
            target_file,
            usecols=[
                "prs_achternaam",
                "prs_voornamen",
                "prs_tussenvoegsels",
                "prs_initialen",
                "vwz_archivelink",
                "prs_UUID",
            ],
            converters={
                "prs_achternaam": str,
                "prs_voornamen": str,
                "prs_tussenvoegsels": str,
                "vwz_archivelink": str,
                "prs_initialen": str,
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
                        row["prs_tussenvoegsels"],
                        row["prs_initialen"],
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

    for i in input_list:
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
                        row["prs_tussenvoegsels"],
                        "",
                        row["vwz_archivelink"],
                        row["prs_UUID"],
                    ]
                )
                continue
            continue
        continue

    print("fourth index done!")
