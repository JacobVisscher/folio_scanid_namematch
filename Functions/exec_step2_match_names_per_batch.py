import os
import xml.etree.ElementTree as ET
from Levenshtein import distance as lev
import csv
import pandas as pd
import re
import math


def run(inum, toegangsnummer):
    # set inventaris number
    print("input the inventaris number: for example '1' ")
    inumber = inum

    # set path
    path = "/media/rutger/NAHD653/"

    path_folder = "/data/folio_scanid_namematch/"

    inputfolder = os.path.join("/data", "folio_scanid_namematch", "output_step1")

    outputfolder = os.path.join("/data", "folio_scanid_namematch", "output_step2")

    # set the base string for file names
    basestring = "NL-HaNA_{}_".format(toegangsnummer)

    # set base string for inventaris links
    archive_directory = "{}/".format(toegangsnummer)

    # set directory. /data/2.01.15/118/page    '/data/2.01.15/195/page'
    directory = "{}{}{}/page".format(path, archive_directory, inumber)
    directory = directory
    print(directory)
    data = []
    data_bulk = []

    # set batch strings
    batch_filenames = []
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
    if xml_pages > pages:
        print("yes")
        for i in range(batch_amount):
            begin_batch = e * pages
            end_batch = (e + 1) * pages
            print(begin_batch, end_batch)
            batch_filename = (
                "/"
                + inputfolder
                + "/"
                + "batch_{}{}_{}-{}.csv".format(
                    basestring, inumber, begin_batch, end_batch
                )
            )
            batch_filenames.append(batch_filename)
            e = e + 1
            print(e)

            continue
    if xml_pages < pages:
        begin_batch = e * pages
        end_batch = (e + 1) * pages
        print(begin_batch, end_batch)
        batch_filename = (
            "/"
            + inputfolder
            + "/"
            + "batch_{}{}_{}-{}.csv".format(basestring, inumber, begin_batch, end_batch)
        )
        batch_filenames.append(batch_filename)

    names = []

    # generate output file
    output_filename = "data_{}{}.csv".format(basestring, inumber)
    f = open("/" + outputfolder + "/" + output_filename, "w", newline="")
    f.truncate
    f.close()

    with open("/" + outputfolder + "/" + output_filename, "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            print(row)

    # set percentage of string that does not have to match in levenstein distance
    percentage_string_small = 0
    percentage_string_medium = 0.25
    percentage_string_large = 0.33
    filenames = []

    # find if the names in the batch of the name_list index are present in the htr.
    print(filenames)
    e = 0
    for batch_filename in batch_filenames:
        print(batch_filename)
        if os.stat(batch_filename).st_size == 0:
            print(f"Skipping empty file: {batch_filename}")
            continue
        filenames = []
        name_list_filename = batch_filename
        name_list = pd.read_csv(name_list_filename, na_filter=False, header=None)
        begin_batch = e * pages
        end_batch = (e + 1) * pages
        for file in os.listdir(directory):
            filename = os.fsdecode(file)
            if e == 0:
                for i in range(begin_batch, end_batch):
                    endstring = "00{}.xml".format(i)
                    if filename.endswith(endstring):
                        filenames.append(filename)
            else:
                for i in range(begin_batch, end_batch):
                    endstring = "0{}.xml".format(i)
                    if filename.endswith(endstring):
                        filenames.append(filename)
        print(batch_filename)
        e = e + 1
        for file in filenames:
            filename = os.fsdecode(file)
            if filename.endswith(".xml"):
                data_page = []
                tree = ET.parse(os.path.join(directory, filename))
                data_page.append(filename)
                data_bulk.append(filename)
                root = tree.getroot()
                text = ""
                PlainText = root.iter(
                    "{http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15}PlainText"
                )
                for PlainText in root.iter(
                    "{http://schema.primaresearch.org/PAGE/gts/pagecontent/2013-07-15}PlainText"
                ):
                    text = text + PlainText.text + " "
                    continue
                text = re.sub(r"[\W_]+", " ", text)
                splitText = text.split()
                # print(splitText)
                for index, row in name_list.iterrows():
                    firstname = row[0]
                    lastname = row[1]
                    names.append(firstname)
                    names.append(lastname)
                    continue
                # print(names)
                for word in splitText:
                    for name in names:
                        space = " "
                        if space in name:
                            name = name.split()
                            for subname in name:
                                string_length = len(subname)
                                l = lev(subname, word)
                                # print(lev(name, PlainText.text))
                                if string_length <= 2:
                                    continue
                                if (
                                    string_length == 3
                                    and l < percentage_string_small * string_length
                                ):
                                    name.remove(subname)
                                    data_page.append(subname)
                                    data_bulk.append(subname)
                                    # print(data)
                                    continue
                                if (
                                    string_length >= 4
                                    and string_length < 7
                                    and l < percentage_string_medium * string_length
                                ):
                                    name.remove(subname)
                                    data_page.append(subname)
                                    data_bulk.append(subname)
                                    # print(data)
                                    continue
                                if (
                                    string_length >= 7
                                    and l < percentage_string_large * string_length
                                ):
                                    name.remove(subname)
                                    data_page.append(subname)
                                    data_bulk.append(subname)
                                    # print(data)
                                    continue
                        else:
                            string_length = len(name)
                            l = lev(name, word)
                            if (
                                string_length <= 3
                                and l < percentage_string_small * string_length
                            ):
                                names.remove(name)
                                data_page.append(name)
                                data_bulk.append(name)
                                # print(data)
                                continue
                            if (
                                string_length >= 4
                                and string_length < 7
                                and l < percentage_string_medium * string_length
                            ):
                                names.remove(name)
                                data_page.append(name)
                                data_bulk.append(name)
                                # print(data)
                                continue
                            if (
                                string_length >= 7
                                and l < percentage_string_large * string_length
                            ):
                                names.remove(name)
                                data_page.append(name)
                                data_bulk.append(name)
                                # print(data)
                                continue
                            continue
                        continue
                    continue
                original_list = data_page
                unique_list = [
                    x for i, x in enumerate(original_list) if x not in original_list[:i]
                ]
                data.append(unique_list)
                continue
            continue

    file = open("/" + outputfolder + "/" + output_filename, "w+", newline="")

    # writing the data into an output file
    with file:
        write = csv.writer(file)
        write.writerows(data)

    print("matches found")
    print(data_bulk)

    print(data)

    reader = csv.reader(open("/" + outputfolder + "/" + output_filename), delimiter=" ")
    sortedlist = sorted(reader, key=lambda row: row[0])

    # take the output and put it into a sorted list. For example "sorted_data_2.01.15_1.csv"
    print(sortedlist)
    output_filename = "sorted_data_{}{}.csv".format(basestring, inumber)
    f = open("/" + outputfolder + "/" + output_filename, "w", newline="")
    f.truncate
    f.close()

    file = open("/" + outputfolder + "/" + output_filename, "w+", newline="")

    with file:
        write = csv.writer(file)
        write.writerows(sortedlist)
