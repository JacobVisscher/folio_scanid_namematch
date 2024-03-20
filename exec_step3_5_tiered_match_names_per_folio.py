from collections import defaultdict
import os
import xml.etree.ElementTree as ET
from Levenshtein import distance as lev
import csv
import pandas as pd
import re
import math


def run(inum, toegangsnummer, folder_path):
    # set inventaris number
    print("input the inventaris number: for example '1' ")
    inumber = inum
    # set path
    path = "/data/"

    inputfolder = os.path.join(folder_path, "output_step0")
    inputfolder_2 = os.path.join(folder_path, "output_step2")
    outputfolder = os.path.join(folder_path, "output_step3")

    # set the base string for file names
    basestring = "NL-HaNA_{}_".format(toegangsnummer)

    # set base string for inventaris links
    archive_directory = "{}/".format(toegangsnummer)

    # input directory for the csv file
    directory_csv = "~/python/output_step0"
    name_list_filename = "{}{}.csv".format(basestring, inumber)
    path_namelist = os.path.join(inputfolder, name_list_filename)
    if os.path.isfile(path_namelist):

        def string_exists_in_csv(csv_file, string):
            with open(csv_file, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if string in row:
                        return True
            return False

        # set directory.
        directory = "{}{}{}/page".format(path, archive_directory, inumber)
        directory = directory
        print(directory)

        # set batch name list
        names = []

        # set name list, this is the nadere toegang index split for this inventory.
        name_list_filename = "{}{}.csv".format(basestring, inumber)

        print(name_list_filename)
        # name_list = pd.read_csv(name_list_filename, na_filter=False, header=None)

        # print(name_list)
        names = []

        # input file: this is the sorted data made in step 2.
        input_list_filename = "sorted_data_{}{}.csv".format(basestring, inumber)

        # output file
        output_filename = "output_{}{}.csv".format(basestring, inumber)
        print(output_filename)
        f = open("/" + outputfolder + "/" + output_filename, "w", newline="")
        f.truncate
        f.close()

        # set max inventory and
        print(
            "input the max inventory number. make sure this is the same number you used in step 1. "
        )
        max_page = 600
        match_percentages = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]

        # Read the name list file and store the rows in a list
        with open("/" + inputfolder + "/" + name_list_filename, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            name_list_rows = list(reader)

        # Read the input list file and store the rows in a list
        with open(
            "/" + inputfolder_2 + "/" + input_list_filename, newline=""
        ) as csvfile2:
            reader2 = csv.reader(csvfile2, delimiter=",")
            input_list_rows = list(reader2)

        with open("/" + outputfolder + "/" + output_filename, "r") as file:
            reader = csv.reader(file)
            csv_rows = list(reader)

        # loop over the match percentages. The code takes the highest match percentage first, and then lowers its demands each cycle. This time the best matches are linked first.
        for match_percentage in match_percentages:
            print(match_percentage)
            selected_names_dict = defaultdict(lambda: defaultdict(list))
            with open("/" + outputfolder + "/" + output_filename, "r") as file:
                reader = csv.reader(file)
                csv_rows = list(reader)
            # Loop over the inventory folio numbers
            for i in range(1, max_page):
                names = []
                uid = []
                folionumber = []
                rest = []
                string_to_check = "{}/{}//{}//".format(toegangsnummer, inumber, i)

                # check if i allready assigned to output?
                # print(csv_rows)
                if string_exists_in_csv(
                    "/" + outputfolder + "/" + output_filename, string_to_check
                ):
                    print(string_to_check)
                    continue

                # Loop over the rows in the inventory name list index.
                for row in name_list_rows:
                    if string_to_check in row[4]:
                        selected_names = row[0].split()
                        names.extend(selected_names)
                        selected_names = row[1].split()
                        names.extend(selected_names)
                        uid.append(row[5])

                # skip empty folionumbers, if they are not empty, print the names found in the index.
                if len(names) == 0:
                    print("No names found for page {}".format(i))
                    continue
                print("Names in index for page {}".format(i))
                print(names, rest, uid)

                # Loop over the rows in names found int he htr of xml pages.
                for row2 in input_list_rows:
                    selected_names2 = row2[0].split(",")
                    # print(selected_names2)
                    # print(names)
                    selected_names_set = set(selected_names2)
                    common_names_set = set(names) & selected_names_set
                    percentage = len(common_names_set) / len(names)
                    percentage_corrected = percentage * (
                        (500 + len(names)) / (500 + len(selected_names2))
                    )
                    if percentage_corrected > match_percentage:
                        print("Names in htr output for page")
                        print(selected_names2)
                        print(percentage)
                        print(uid)
                        for id in uid:
                            selected_names_dict[id][string_to_check].append(
                                selected_names2[0]
                            )
                        names = "test"
                        input_list_rows.remove(row2)
                        break

            # select the columns that contain the names from the index in a dictionary
            name_dict = {}
            with open(
                "/" + inputfolder + "/" + name_list_filename, newline=""
            ) as name_file:
                name_reader = csv.reader(name_file, delimiter=",")
                for row in name_reader:
                    print("name dict before is:")
                    print(name_dict)
                    print("row in namereader is:")
                    print(row)
                    name_dict[row[5]] = row[0:4]
                    print("name dict is")
                    print(name_dict)

            # Write the output file using the selected_names_dict defaultdict
            with open(
                "/" + outputfolder + "/" + output_filename, "a", newline=""
            ) as file:
                writer = csv.writer(file)
                for id, string_dict in selected_names_dict.items():
                    # Write the rows with all the information, that is: the xml id, the names split, the UUID of that name, and with what match percentages it is matched.
                    if id in name_dict:
                        for string_to_check, names in string_dict.items():
                            for name in names:
                                writer.writerow(
                                    [id]
                                    + name.split(",")
                                    + [string_to_check]
                                    + name_dict[id]
                                    + [match_percentage]
                                )

        # Read the input CSV file and store the rows in a list
        with open("/" + outputfolder + "/" + output_filename, newline="") as input_file:
            reader = csv.reader(input_file)
            input_rows = list(reader)

        # Sort the input rows based on the second column
        sorted_rows = sorted(input_rows, key=lambda x: x[1])
        sorted_output_filename = "output_{}{}_sorted.csv".format(basestring, inumber)

        print(sorted_output_filename)
        # f = open(sorted_output_filename, "w", newline="")
        # f.truncate
        # f.close()

        # Write the sorted rows to the output CSV file output_NL-HaNA_2.13.04_94_sorted.csv
        with open(
            "/" + outputfolder + "/" + sorted_output_filename, "w+", newline=""
        ) as output_file:
            writer = csv.writer(output_file)
            writer.writerows(sorted_rows)
