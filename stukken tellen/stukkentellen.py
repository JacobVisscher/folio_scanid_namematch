import csv
import pandas as pd

string_naam = "2.16.23.02_dataentry_def"

input_file = "{}.csv".format(string_naam)
output_file = "output{}cb.csv".format(string_naam)
column_a_name = "In Te Vullen Metadata"
column_b_name = "Springen en tonen website"
column_c_name = "Stuk"
column_d_name = "Hulp kolom aantalals Stuk"
column_e_name = "tellen Stuk"
column_f_name = "Totaal Stuk"


def read_cell(csv_file, row_index, column_index):
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == row_index:
                if column_index < len(row):
                    return row[column_index]
                else:
                    return None  # Column index out of range
    return None  # Row index out of range or file is empty


def update_row(csv_file, row_index, new_data):
    # Read the contents of the CSV file
    with open(csv_file, "r") as file:
        rows = list(csv.reader(file))

    # Update the desired row with new data
    rows[row_index] = new_data

    # Write the updated data back to the CSV file
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def update_column(csv_file, column_index, new_data):
    # Read the contents of the CSV file
    with open(csv_file, "r") as file:
        rows = list(csv.reader(file))

    # Update the desired column with new data
    for row in rows:
        row[column_index] = new_data

    # Write the updated data back to the CSV file
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def find_cells_with_value(csv_file, column_index, target_value):
    matching_cells = []
    cell_count = 0

    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > column_index and row[column_index] == target_value:
                matching_cells.append(row[column_index])
                cell_count += 1

    return cell_count


def update_cell(csv_file, row_index, column_index, new_data):
    # Read the contents of the CSV file
    with open(csv_file, "r") as file:
        rows = list(csv.reader(file))

    # Update the desired cell with new data
    rows[row_index][column_index] = new_data

    # Write the updated data back to the CSV file
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


string_naam = "2.16.23.02_dataentry_test"

csv_file = "{}.csv".format(string_naam)
output_file = "output{}cb.csv".format(string_naam)
column_a_name = "In Te Vullen Metadata"
column_b_name = "Springen en tonen website"
column_c_name = "Stuk"
column_d_name = "Hulp kolom aantalals Stuk"
column_e_name = "tellen Stuk"
column_f_name = "Totaal Stuk"


# stap 1: D tellen vanaf A, D increments als A ongelijk is aan A -1 en gelijk is aan stuk
with open(csv_file, "r") as file:
    n = 0
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        # print(read_cell(csv_file, row_index, 3), read_cell(csv_file, row_index, 9))

        # Update the desired cell in each row
        column_index = 11  # Index of the column you want to update (0-based)
        if row_index == 0 or row_index == 1:
            continue
        if read_cell(csv_file, row_index, 9) == "":
            continue
        if (
            read_cell(csv_file, row_index, 9) == read_cell(csv_file, row_index - 1, 9)
            and read_cell(csv_file, row_index, 3) == "Stuk"
            and read_cell(csv_file, row_index - 1, 3) != "Stuk"
        ):
            n = n + 1
            new_data = n  # New data for the cell
            update_cell(csv_file, row_index, column_index, new_data)
            # print(read_cell(csv_file, row_index, 11))
            continue
        if (
            read_cell(csv_file, row_index, 9) == read_cell(csv_file, row_index - 1, 9)
            and read_cell(csv_file, row_index, 3) == "Stuk"
        ):
            new_data = n  # New data for the cell
            update_cell(csv_file, row_index, column_index, new_data)
            # print(read_cell(csv_file, row_index, 11))
            continue
        if read_cell(csv_file, row_index, 9) != read_cell(csv_file, row_index - 1, 9):
            n = n + 1
            new_data = n  # New data for the cell
            update_cell(csv_file, row_index, column_index, new_data)
            # print(read_cell(csv_file, row_index, column_index))
        if (
            read_cell(csv_file, row_index, 9) == read_cell(csv_file, row_index - 1, 9)
            and read_cell(csv_file, row_index, 3) != "Stuk"
        ):
            n = n + 1
            new_data = n  # New data for the cell
            update_cell(csv_file, row_index, column_index, new_data)
            # print(read_cell(csv_file, row_index, column_index))
        else:
            continue
print("step 1 done")

# stap 2:  E tellen vanaf D; incremenets zolang Dn gelijk is aan Dn-1
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    n = 1
    for row_index, row in enumerate(reader):
        # print(read_cell(csv_file, row_index, 9), read_cell(csv_file, row_index, 11))
        if row_index == 0 or row_index == 1:
            continue
        if read_cell(csv_file, row_index, 9) == "":
            continue
        # Update the desired cell in each row
        column_index = 12  # Index of the column you want to update (0-based)
        if (
            read_cell(csv_file, row_index, 11) == read_cell(csv_file, row_index - 1, 11)
            and read_cell(csv_file, row_index, 3) != "Stuk"
        ):
            n = n + 1
            new_data = n  # New data for the cell
            update_cell(csv_file, row_index, column_index, new_data)
            # print(read_cell(csv_file, row_index, column_index))
        if (
            read_cell(csv_file, row_index, 11) == read_cell(csv_file, row_index - 1, 11)
            and read_cell(csv_file, row_index, 3) == "Stuk"
        ):
            n = n + 1
            new_data = n  # New data for the cell
            update_cell(csv_file, row_index, column_index, new_data)
            # print(read_cell(csv_file, row_index, column_index))
        else:
            n = 1
            new_data = n  # New data for the cell
            update_cell(csv_file, row_index, column_index, new_data)
            # print(read_cell(csv_file, row_index, column_index))
            continue

print("step 2 done")

# stap3: telt hoeveel D hetzelfde is aan Dn.
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        # print(read_cell(csv_file, row_index, 11), read_cell(csv_file, row_index, 12))
        if row_index == 0 or row_index == 1:
            continue
        if read_cell(csv_file, row_index, 9) == "":
            continue
        n = read_cell(csv_file, row_index, 11)
        # Update the desired cell in each row
        column_index = 13  # Index of the column you want to update (0-based)
        index_step = read_cell(csv_file, row_index, 11)
        new_data = find_cells_with_value(
            csv_file, 11, index_step
        )  # New data for the cell
        # print(new_data)
        update_cell(csv_file, row_index, column_index, new_data)

print("step 3 done")

# stap 4: svull colum 6, string 12 from 13.
with open(csv_file, "r") as file:
    reader = csv.reader(file)
    for row_index, row in enumerate(reader):
        if row_index == 0 or row_index == 1:
            continue
        if read_cell(csv_file, row_index, 9) == "":
            continue
        n = 0
        # Update the desired cell in each row
        column_index = 6  # Index of the column you want to update (0-based)
        # fill the index step
        index_step = read_cell(csv_file, row_index, 12)
        # select the total
        index_total = read_cell(csv_file, row_index, 13)
        # create string
        new_data = "{} van {}".format(index_step, index_total)
        update_cell(csv_file, row_index, column_index, new_data)

print("step 4 done")


# stap 5: fill the column 5 ith a string combining column 3 and column 6
# with open(csv_file, "r") as file:
#    reader = csv.reader(file)
#    for row_index, row in enumerate(reader):
#        if row_index == 0 or row_index == 1:
#            continue
#        if read_cell(csv_file, row_index, 9) == "":
#            continue
#        n = 0
#        # Update the desired cell in each row
#        column_index = 5  # Index of the column you want to update (0-based)
#        # fill the index step
#        doctype = read_cell(csv_file, row_index, 5)
#        # select the total
#        X_of_Y = read_cell(csv_file, row_index, 6)
#        # create string
#        new_data = "{}{}".format(doctype, X_of_Y)
#        update_cell(csv_file, row_index, column_index, new_data)

# print("step 5 done")
