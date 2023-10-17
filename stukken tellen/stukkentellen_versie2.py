import csv
import pandas as pd
import itertools
from array import array

string_naam = "Kopie_2.04.01_dataentry_conc_VN"

input_file = "{}.csv".format(string_naam)
column_a_name = "In Te Vullen Metadata"
column_b_name = "Springen en tonen website"
column_c_name = "Stuk"
column_d_name = "Hulp kolom aantalals Stuk"
column_e_name = "tellen Stuk"
column_f_name = "Totaal Stuk"


def read_cell(reader, row_index, column_index):
    print("read_cell started")
    for i, row in enumerate(reader):
        if i == row_index:
            if column_index < len(row):
                return row[column_index]
            else:
                return None  # Column index out of range
    return None  # Row index out of range or file is empty


def update_row(writer, rows, row_index, new_data):
    print("update_row started")
    # Update the desired row with new data
    rows[row_index] = new_data

    # Write the updated data back to the CSV file
    writer.writerows(rows)


def update_column(writer, rows, column_index, new_data):
    print("update_column started")
    # Update the desired column with new data
    for row in rows:
        row[column_index] = new_data
        # Write the updated data back to the CSV file
        writer.writerows(rows)


def find_cells_with_value(reader, column_index, target_value):
    print("find_cell_with_value started")
    matching_cells = []
    cell_count = 0
    for row in reader:
        if len(row) > column_index and row[column_index] == target_value:
            matching_cells.append(row[column_index])
            cell_count += 1
        return cell_count


def update_cell(writer, rows, row_index, column_index, new_data):
    print("update_cell started")
    # Update the desired cell with new data
    rows[row_index][column_index] = new_data

    # Write the updated data back to the CSV file
    writer.writerows(rows)


string_naam = "Kopie_2.04.01_dataentry_conc_VN"

csv_file = "{}.csv".format(string_naam)

# step 0: open the file
with open(csv_file, "r+") as file_update:
    new_fieldnames = [
        "Niveau",
        "Afbeelding",
        "Data entry",
        "Label",
        "In te vullen metadata",
        "Herkomst",
        "springen en tonen website",
        "Stuk",
        "Hulp kolom aantalals Stuk",
        "tellen Stuk",
        "Totaal Stuk",
        "Bestandsnaam1",
        "Bestandsnaam2",
        "Bestandsnaam3",
        "Bestandsnaam4",
    ]
    writer = csv.writer(file_update)
    print(writer)
    fieldnames = [
        "Niveau",
        "Afbeelding",
        "Data entry",
        "Label",
        "In te vullen metadata",
        "Herkomst",
    ]
    reader = csv.reader(file_update)
    reader0, reader1, reader2, reader3, reader4, reader5, reader6 = itertools.tee(
        reader, 7
    )
    results = []
    # for row_index, row in enumerate(reader6):
    # if row_index == 0:
    # print(row)
    # print("above is the first row, should have been the headers")

    for row_index, row in enumerate(reader0):
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        row.append("")
        results.append(row)
    del reader0
    del reader1
    print(results[0])
    # step 0:  splitsen naam
    n = 0
    column_to_update_name1 = new_fieldnames.index("Bestandsnaam1")
    column_to_update_name2 = new_fieldnames.index("Bestandsnaam2")
    column_to_update_name3 = new_fieldnames.index("Bestandsnaam3")
    column_to_update_name4 = new_fieldnames.index("Bestandsnaam4")
    column_afbeelding = new_fieldnames.index("Afbeelding")
    column_label = new_fieldnames.index("Label")
    column_herkomst = new_fieldnames.index("Herkomst")
    # print(column_afbeelding, column_label, column_herkomst)
    names1 = []
    names2 = []
    names3 = []
    names4 = []
    # row_count = sum(1 for row in reader2)
    # print(row_count)
    for row_index, row in enumerate(reader2):
        # print(row_index)
        # print(row)
        if row_index == 0:
            # print(results[row_index])
            continue
        else:
            names_split = row[column_afbeelding].split("_")
            # print(results[row_index])
            names1.append(names_split[0])
            names2.append(names_split[1])
            names3.append(names_split[2])
            names4.append(names_split[3])
            results[row_index][column_to_update_name1] = names_split[0]
            results[row_index][column_to_update_name2] = names_split[1]
            results[row_index][column_to_update_name3] = names_split[2]
            results[row_index][column_to_update_name4] = names_split[3]

            # print(results[row_index - 1])
            # print(results[row_index])
    string_naam_output = "{}_output.csv".format(string_naam)

    with open(string_naam_output, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(results)
    print("test two done")
    del reader2
    n = 0
    # stap 1: D tellen vanaf A, D increments als A ongelijk is aan A -1 en gelijk is aan stuk
    column_to_update = new_fieldnames.index(
        "Hulp kolom aantalals Stuk"
    )  # Index of the column you want to update (0-based)
    for row_index, row in enumerate(reader3):
        # Update the desired cell in each row
        if row_index == 0:
            continue
        if results[row_index][column_to_update_name3] == "":
            # print(results[row_index])
            continue
        if (
            results[row_index][column_to_update_name3]
            == results[row_index - 1][column_to_update_name3]
            and results[row_index][column_label] == "Stuk"
            and results[row_index - 1][column_label] != "Stuk"
        ):
            n = n + 1
            new_data = n  # New data for the cell
            results[row_index][column_to_update] = new_data
            # print(results[row_index])
            continue
        if (
            results[row_index][column_to_update_name3]
            == results[row_index - 1][column_to_update_name3]
            and results[row_index][column_label] == "Stuk"
        ):
            new_data = n  # New data for the cell
            results[row_index][column_to_update] = new_data
            # print(results[row_index])
            continue
        if (
            results[row_index][column_to_update_name3]
            != results[row_index - 1][column_to_update_name3]
        ):
            n = n + 1
            new_data = n  # New data for the cell
            results[row_index][column_to_update] = new_data
            # print(results[row_index])
        if (
            results[row_index][column_to_update_name3]
            == results[row_index - 1][column_to_update_name3]
            and results[row_index][column_label] != "Stuk"
        ):
            n = n + 1
            new_data = n  # New data for the cell
            results[row_index][column_to_update] = new_data
            # print(results[row_index])
        else:
            continue

    print("step 1 done")
    del reader3
    # stap 2:  E tellen vanaf D; incremenets zolang Dn gelijk is aan Dn-1
    n = 1
    column_to_update = new_fieldnames.index(
        "tellen Stuk"
    )  # Index of the column you want to update (0-based)
    column_stuk = new_fieldnames.index("Hulp kolom aantalals Stuk")
    for row_index, row in enumerate(reader4):
        # print(read_cell(csv_file, row_index, 9), read_cell(csv_file, row_index, 11))
        if row_index == 0:
            continue
        if results[row_index][column_to_update_name3] == "":
            continue
        # Update the desired cell in each row
        if (
            results[row_index][column_stuk] == results[row_index - 1][column_stuk]
            and results[row_index][column_label] != "Stuk"
            # and
            # read_cell(csv_file, row_index, column_stuk) == read_cell(csv_file, row_index - 1, column_stuk)
            # and read_cell(csv_file, row_index, column_label) != "Stuk"
        ):
            n = 1
            new_data = n  # New data for the cell
            results[row_index][column_to_update] = new_data
            # print(results[row_index])
            # update_cell(csv_file, row_index, column_to_update, new_data)
            # print(read_cell(csv_file, row_index, column_to_update))
        if (
            results[row_index][column_stuk] == results[row_index - 1][column_stuk]
            and results[row_index][column_label] == "Stuk"
            # read_cell(csv_file, row_index, column_stuk) == read_cell(csv_file, row_index - 1, column_stuk)
            # and read_cell(csv_file, row_index, column_label) == "Stuk"
        ):
            n = n + 1
            new_data = n  # New data for the cell
            results[row_index][column_to_update] = new_data
            # print(results[row_index])
            # update_cell(csv_file, row_index, column_to_update, new_data)
            # print(read_cell(csv_file, row_index, column_to_update))
        else:
            n = 1
            new_data = n  # New data for the cell
            results[row_index][column_to_update] = new_data
            # print(results[row_index])
            # update_cell(csv_file, row_index, column_to_update, new_data)
            # print(read_cell(csv_file, row_index, column_to_update))
            continue
    print("step 2 done")
    del reader4

    with open("test_inbetween", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(results)
    # stap3: telt hoeveel D hetzelfde is aan Dn.

    for row_index, row in enumerate(results):
        column_to_update = new_fieldnames.index(
            "Totaal Stuk"
        )  # Index of the column you want to update (0-based)
        column_amount_stuk = new_fieldnames.index("tellen Stuk")
        # print(read_cell(csv_file, row_index, 11), read_cell(csv_file, row_index, 12))
        if results[row_index][column_to_update] != "":
            # print("skipped because column allready filled ")
            continue
        if row_index == 0:
            # print("skipped bfirst row")
            continue
        if results[row_index][column_to_update_name3] == "":
            continue
        if results[row_index][column_to_update] == "":
            n = results[row_index][column_amount_stuk]
            # Update the desired cell in each row

            index_step = results[row_index][column_stuk]
            # print("processing index number:")
            # print(results[row_index])
            matching_cells = []
            cell_count = 0
            for row_index, row in enumerate(results):
                if row[column_to_update] != "":
                    continue
                if len(row) > column_amount_stuk and row[column_stuk] == index_step:
                    # print(index_step)
                    matching_cells.append(row_index)
                    cell_count += 1
                    new_data = cell_count
                else:
                    continue
            for cell in matching_cells:
                results[cell][column_to_update] = new_data
                # print(results[cell][column_to_update])
    print("step 3 done")

    # stap 4: svull colum 6, string 12 from 13.

    for row_index, row in enumerate(reader5):
        column_total_stuk = new_fieldnames.index("Totaal Stuk")
        column_to_update = new_fieldnames.index("springen en tonen website")
        if row_index == 0:
            continue
        if results[row_index][column_to_update_name3] == "":
            continue
        n = 0
        # Update the desired cell in each row
        # Index of the column you want to update (0-based)
        # fill the index step
        index_step = results[row_index][column_amount_stuk]
        # select the total
        index_total = results[row_index][column_total_stuk]
        # create string
        new_data = "{} van {}".format(index_step, index_total)
        # print(row_index)
        results[row_index][column_to_update] = new_data
        # print(results[row_index])
    print("step 4 done")
    del reader5

    string_naam_output = "{}_output.csv".format(string_naam)

    with open(string_naam_output, "w+", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(results)

    # stap 5: fill the column 5 ith a string combining column 3 and column 6
    for row_index, row in enumerate(results):
        if row_index == 0:
            continue
        if results[row_index][column_herkomst] == "":
            continue
        n = 0
        # Update the desired cell in each row
        # Index of the column you want to update (0-based)
        column_to_update = new_fieldnames.index("Stuk")
        column_springen_en_tonen_website = new_fieldnames.index(
            "springen en tonen website"
        )
        # fill the index step
        doctype = results[row_index][column_label]
        # select the total
        X_of_Y = results[row_index][column_springen_en_tonen_website]
        # create string
        new_data = "{} {}".format(doctype, X_of_Y)
        results[row_index][column_to_update] = new_data
        # print(results)
    print("step 5 done")

string_naam_output = "{}_output.csv".format(string_naam)

with open(string_naam_output, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(results)
