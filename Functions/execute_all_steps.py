import exec_step0_monsterboek_fill_files
import exec_step0_1_monsterboek_normalisation_index
import exec_step0_2_monsterboek_find_list
import exec_step1_select_batch_name
import exec_step2_match_names_per_batch
import exec_step3_5_tiered_match_names_per_folio
import exec_step3_match_names_per_folio
import os
import pandas as pd

print(
    'voer in welk toegangsnummer je de naamsherkenning op wilt uitvoeren. deze toegang moet al wel volledig ge-HTR\'d zijn, en het step0 script moet al uitgevoerd zijn. het format voor het toegangsnummer is "2.01.15" '
)
gekozen_toegangsnummer = "2.01.15"
inputlist_folder = os.path.join(
    "/data", "2.01.15_matching_output_files", "output_step0.2"
)

exec_step0_1_monsterboek_normalisation_index.run(gekozen_toegangsnummer)
exec_step0_2_monsterboek_find_list.run(gekozen_toegangsnummer)

input_list_file = os.path.join(inputlist_folder, "list_of_entries.csv")
input_list = pd.read_csv(input_list_file)

exec_step0_monsterboek_fill_files.run(gekozen_toegangsnummer)
for i in input_list:
    exec_step1_select_batch_name.run(i, gekozen_toegangsnummer)
    exec_step2_match_names_per_batch.run(i, gekozen_toegangsnummer)
    exec_step3_match_names_per_folio.run(i, gekozen_toegangsnummer)
    exec_step3_5_tiered_match_names_per_folio.run(i, gekozen_toegangsnummer)
