import sqlite3
import csv
import pandas as pd
import math
import os
import re


def run(toegangsnummer):
    # set path
    path_folder = os.path.join("/data", "2.01.15_matching_output_files")

    inputfolder = os.path.join("/data", "2.01.15_matching_output_files", "input")

    outputfolder = os.path.join(
        "/data", "2.01.15_matching_output_files", "output_step0.1"
    )
    basestring = "NL-HaNA_{}_".format(toegangsnummer)

    # set base string for inventaris links
    archive_directory = "{}/".format(toegangsnummer)

    # how many inventarisses are in the archive

    # iterate through inventory based on nadere toegang document

    # set nadere toegang document. document must be in the same folder as this script.
    # look at how many indexes you have for the archive, and then put them in the blocks below. 1 block per index file, from target file to the print statement.
    target_file_base = "NT00239_PERSOON.csv"
    target_file = os.path.join(inputfolder, "NT00239_PERSOON.csv")
    output_file = os.path.join(outputfolder, "NT00239_PERSOON.csv")

    headerList = [
        "prs_achternaam",
        "prs_voornamen",
        "prs_tussenvoegsels",
        "prs_initialen",
        "vwz_archivelink",
        "prs_UUID",
    ]
    print(target_file)

    f = open(output_file, "w", newline="")
    writer = csv.DictWriter(f, fieldnames=headerList)
    writer.writeheader()
    print("csv files created")

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
        pattern = re.compile(r"\s")

        # Remove all spaces
        result_string = re.sub(pattern, "", row["vwz_archivelink"])
        writer.writerow(
            {
                "prs_voornamen": row["prs_achternaam"],
                "prs_achternaam": row["prs_voornamen"],
                "prs_tussenvoegsels": row["prs_tussenvoegsels"],
                "prs_initialen": row["prs_initialen"],
                # row["vwz_archivelink"],
                "vwz_archivelink": result_string,
                "prs_UUID": row["prs_UUID"],
            }
        )
        continue
    print("first index done!")

    target_file_base = "NT00242_PERSOON.csv"
    target_file = os.path.join(inputfolder, "NT00242_PERSOON.csv")
    output_file = os.path.join(outputfolder, "NT00242_PERSOON.csv")
    print(target_file)

    f = open(output_file, "w", newline="")
    writer = csv.DictWriter(f, fieldnames=headerList)
    writer.writeheader()
    print("csv files created")

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
        pattern = re.compile(r"\s")

        # Remove all spaces
        result_string = re.sub(pattern, "", row["vwz_archivelink"])
        writer.writerow(
            {
                "prs_voornamen": row["prs_achternaam"],
                "prs_achternaam": row["prs_voornamen"],
                "prs_tussenvoegsels": row["prs_tussenvoegsels"],
                "prs_initialen": "",
                # row["vwz_archivelink"],
                "vwz_archivelink": result_string,
                "prs_UUID": row["prs_UUID"],
            }
        )
        continue
    print("second index done!")

    target_file_base = "NT00243_PERSOON.csv"
    target_file = os.path.join(inputfolder, "NT00243_PERSOON.csv")
    output_file = os.path.join(outputfolder, "NT00243_PERSOON.csv")
    print(target_file)

    f = open(output_file, "w", newline="")
    writer = csv.DictWriter(f, fieldnames=headerList)
    writer.writeheader()
    print("csv files created")

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
        pattern = re.compile(r"\s")

        # Remove all spaces
        result_string = re.sub(pattern, "", row["vwz_archivelink"])
        writer.writerow(
            {
                "prs_voornamen": row["prs_achternaam"],
                "prs_achternaam": row["prs_voornamen"],
                "prs_tussenvoegsels": row["prs_tussenvoegsels"],
                "prs_initialen": row["prs_initialen"],
                # row["vwz_archivelink"],
                "vwz_archivelink": result_string,
                "prs_UUID": row["prs_UUID"],
            }
        )
        continue
    print("third index done!")

    target_file_base = "NT00245_PERSOON.csv"
    target_file = os.path.join(inputfolder, "NT00245_PERSOON.csv")
    output_file = os.path.join(outputfolder, "NT00245_PERSOON.csv")
    print(target_file)

    f = open(output_file, "w", newline="")
    writer = csv.DictWriter(f, fieldnames=headerList)
    writer.writeheader()

    print("csv files created")

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
        pattern = re.compile(r"\s")

        # Remove all spaces
        result_string = re.sub(pattern, "", row["vwz_archivelink"])
        writer.writerow(
            {
                "prs_voornamen": row["prs_achternaam"],
                "prs_achternaam": row["prs_voornamen"],
                "prs_tussenvoegsels": row["prs_tussenvoegsels"],
                "prs_initialen": "",
                # row["vwz_archivelink"],
                "vwz_archivelink": result_string,
                "prs_UUID": row["prs_UUID"],
            }
        )
        continue
    print(" index done!")
