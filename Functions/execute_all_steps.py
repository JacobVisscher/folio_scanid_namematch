import exec_step1_select_batch_name
import exec_step2_match_names_per_batch
import exec_step3_5_tiered_match_names_per_folio
import exec_step3_match_names_per_folio

print(
    'voer in welk toegangsnummer je de naamsherkenning op wilt uitvoeren. deze toegang moet al wel volledig ge-HTR\'d zijn, en het step0 script moet al uitgevoerd zijn. het format voor het toegangsnummer is "2.01.15" '
)
gekozen_toegangsnummer = input()
range_index = 333

for i in range(100, range_index):
    exec_step1_select_batch_name.run(i, gekozen_toegangsnummer)
    exec_step2_match_names_per_batch.run(i, gekozen_toegangsnummer)
    exec_step3_match_names_per_folio.run(i, gekozen_toegangsnummer)
    exec_step3_5_tiered_match_names_per_folio.run(i, gekozen_toegangsnummer)
