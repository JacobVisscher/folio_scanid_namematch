import exec_step0_monsterboek_fill_files
import exec_step0_1_monsterboek_normalisation_index
import exec_step0_2_monsterboek_find_list
import exec_step1_select_batch_name
import exec_step2_match_names_per_batch
import exec_step3_5_tiered_match_names_per_folio
import exec_step3_match_names_per_folio
import os
import pandas as pd

print('voer in welk toegangsnummer je de naamsherkenning op wilt uitvoeren. deze toegang moet al wel volledig ge-HTR\'d zijn, en het step0 script moet al uitgevoerd zijn. het format voor het toegangsnummer is "2.01.15" '
      )

# set inventorynumber number
gekozen_toegangsnummer = "2.01.15"

# set path to functions and output
folder_path = os.path.join("/data", "folio_scanid_namematch")
# set path to files
path_to_files = "/media/rutger/NAHD653/2.01.15/"
# make a list of the inventories that exist in the scanned archive.
list_of_inventarisnummers = os.listdir(path_to_files)

skipped_files = "skipped_files.txt"
if os.path.isfile(skipped_files) == False:
    open(skipped_files, "x")

#exec_step0_1_monsterboek_normalisation_index.run(gekozen_toegangsnummer, folder_path)
#exec_step0_2_monsterboek_find_list.run(gekozen_toegangsnummer, folder_path)
#exec_step0_monsterboek_fill_files.run(gekozen_toegangsnummer, folder_path)
print(list_of_inventarisnummers)
for i in list_of_inventarisnummers:
    print(i)
    exec_step1_select_batch_name.run(
        i, gekozen_toegangsnummer, folder_path, path_to_files
    )
    print(i)
    exec_step2_match_names_per_batch.run(
        i, gekozen_toegangsnummer, folder_path, path_to_files
    )
    print(i)
    #exec_step3_match_names_per_folio.run(
    #    i, gekozen_toegangsnummer, folder_path, path_to_files
    #)
    exec_step3_5_tiered_match_names_per_folio.run(
        i, gekozen_toegangsnummer, folder_path
    )
