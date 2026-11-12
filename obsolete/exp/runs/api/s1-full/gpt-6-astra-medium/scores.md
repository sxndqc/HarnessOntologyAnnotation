# runs/api/s1-full/gpt-6-astra-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 50.7 | 60.4 | 55.2 | 83.7 | no (10) | 79.4 | 76.2 |
| zh-0028 | 12 | 42.7 | 51.8 | 46.8 | 60.2 | no (6) | 44.5 | 42.3 |
| zh-0032 | 6 | 41.2 | 44.6 | 42.8 | 50.7 | no (14) | 33.7 | 31.1 |
| **zh** (2/15 files) | 18 | 41.9 | 3.5 | 6.4 | 7.6 | 0/2 | 39.1 | 36.7 |
| **en** (1/5 files) | 9 | 50.8 | 2.3 | 4.4 | 6.3 | 0/1 | 79.4 | 76.2 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 80.7 | 80.7 | 80.7 | 94.1 | 94.1 | 94.1 |
| a_entity_found | 91.0 | 95.3 | 93.1 | 98.1 | 91.1 | 94.4 |
| a_event_concept | 68.8 | 68.8 | 68.8 | 96.8 | 96.8 | 96.8 |
| a_event_found | 90.9 | 100.0 | 95.2 | 96.9 | 93.9 | 95.4 |
| a_granularity | 96.1 | 97.1 | 96.6 | 98.5 | 98.5 | 98.5 |
| b_event_sense | 91.8 | 91.8 | 91.8 | 96.3 | 96.3 | 96.3 |
| c_aspect | 53.4 | 50.8 | 52.1 | 81.0 | 85.0 | 82.9 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 57.1 | 28.6 | 38.1 | 100.0 | 100.0 | 100.0 |
| c_polarity | 66.7 | 66.7 | 66.7 | – | – | – |
| c_refer | 71.4 | 45.5 | 55.6 | 83.3 | 62.5 | 71.4 |
| d_core_args_abstract | 46.1 | 60.3 | 52.2 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 45.3 | 46.3 | 45.8 | 76.5 | 80.2 | 78.3 |
| d_peripheral_entity | 47.5 | 45.6 | 46.5 | 83.3 | 76.9 | 80.0 |
| d_peripheral_event | 29.8 | 24.3 | 26.8 | 75.0 | 85.7 | 80.0 |
| e_core_labels | 79.5 | 79.5 | 79.5 | 100.0 | 100.0 | 100.0 |
| e_peripheral_labels | 90.0 | 90.0 | 90.0 | 91.7 | 91.7 | 91.7 |
| f_name_tokens | 40.0 | 30.8 | 34.8 | 76.5 | 76.5 | 76.5 |
| f_wiki | – | – | – | 100.0 | 94.1 | 97.0 |
| g_reentrancy | 22.2 | 8.2 | 11.9 | 100.0 | 82.4 | 90.3 |
| h_temporal | 25.4 | 17.2 | 20.5 | 73.7 | 51.9 | 60.9 |
| i_modal | 51.9 | 47.3 | 49.4 | 77.3 | 68.0 | 72.3 |
| j_coref_chain | 32.0 | 5.6 | 9.5 | 100.0 | 57.9 | 73.3 |
| j_coref_subset | – | 0.0 | 0.0 | – | – | – |
| k_doc_format | 98.5 | 98.5 | 98.5 | 99.0 | 99.0 | 99.0 |
