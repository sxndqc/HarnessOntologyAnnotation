# runs/api/s2-propbank/gpt-6-astra-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 48.1 | 50.0 | 49.1 | 76.2 | no (2) | 65.4 | 63.7 |
| zh-0028 | 12 | 46.9 | 57.5 | 51.6 | 62.1 | no (2) | 44.9 | 44.5 |
| zh-0032 | 6 | 42.1 | 47.3 | 44.6 | 54.7 | no (1) | 41.5 | 35.5 |
| **zh** (2/15 files) | 18 | 44.5 | 3.8 | 7.0 | 8.0 | 0/2 | 43.2 | 40.0 |
| **en** (1/5 files) | 9 | 48.1 | 1.9 | 3.6 | 5.3 | 0/1 | 65.4 | 63.7 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 80.6 | 80.6 | 80.6 | 94.0 | 94.0 | 94.0 |
| a_entity_found | 90.5 | 94.8 | 92.6 | 96.2 | 90.9 | 93.5 |
| a_event_concept | 75.6 | 75.6 | 75.6 | 87.1 | 87.1 | 87.1 |
| a_event_found | 97.7 | 98.9 | 98.3 | 96.9 | 100.0 | 98.4 |
| a_granularity | 96.4 | 98.1 | 97.2 | 97.1 | 95.7 | 96.4 |
| b_event_sense | 100.0 | 100.0 | 100.0 | 80.0 | 80.0 | 80.0 |
| c_aspect | 59.0 | 48.6 | 53.3 | 76.2 | 64.0 | 69.6 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 66.7 | 33.3 | 44.4 | 100.0 | 100.0 | 100.0 |
| c_polarity | 66.7 | 66.7 | 66.7 | – | – | – |
| c_refer | 85.7 | 31.6 | 46.2 | 91.7 | 91.7 | 91.7 |
| d_core_args_abstract | 27.5 | 45.8 | 34.4 | 83.3 | 83.3 | 83.3 |
| d_core_args_event | 64.5 | 61.0 | 62.7 | 59.5 | 77.0 | 67.1 |
| d_peripheral_entity | 39.6 | 40.5 | 40.1 | 60.4 | 60.4 | 60.4 |
| d_peripheral_event | 29.0 | 23.8 | 26.1 | 85.4 | 68.3 | 75.9 |
| e_core_labels | 85.4 | 85.4 | 85.4 | 90.9 | 90.9 | 90.9 |
| e_peripheral_labels | 73.6 | 73.6 | 73.6 | 90.9 | 90.9 | 90.9 |
| f_name_tokens | 57.9 | 40.7 | 47.8 | 68.8 | 73.3 | 71.0 |
| f_wiki | – | – | – | 0.0 | – | 0.0 |
| g_reentrancy | 44.4 | 14.5 | 21.9 | 50.0 | 70.0 | 58.3 |
| h_temporal | 34.7 | 20.5 | 25.8 | 52.6 | 33.3 | 40.8 |
| i_modal | 56.2 | 43.5 | 49.1 | 93.2 | 73.2 | 82.0 |
| j_coref_chain | 44.7 | 7.2 | 12.4 | 100.0 | 52.4 | 68.8 |
| j_coref_subset | – | 0.0 | 0.0 | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
