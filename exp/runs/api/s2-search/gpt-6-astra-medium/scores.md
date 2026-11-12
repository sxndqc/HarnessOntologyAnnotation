# runs/api/s2-search/gpt-6-astra-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 51.4 | 61.3 | 55.9 | 86.3 | no (3) | 81.0 | 76.8 |
| zh-0028 | 12 | 48.4 | 58.3 | 52.9 | 64.7 | no (1) | 48.1 | 47.5 |
| zh-0032 | 6 | 43.4 | 45.7 | 44.5 | 54.2 | no (1) | 39.3 | 33.7 |
| **zh** (2/15 files) | 18 | 45.9 | 3.8 | 6.9 | 8.1 | 0/2 | 43.7 | 40.6 |
| **en** (1/5 files) | 9 | 51.4 | 2.3 | 4.4 | 6.3 | 0/1 | 81.0 | 76.8 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 83.8 | 83.8 | 83.8 | 94.1 | 94.1 | 94.1 |
| a_entity_found | 89.2 | 93.8 | 91.5 | 98.1 | 92.7 | 95.3 |
| a_event_concept | 73.8 | 73.8 | 73.8 | 96.8 | 96.8 | 96.8 |
| a_event_found | 95.5 | 98.8 | 97.1 | 96.9 | 93.9 | 95.4 |
| a_granularity | 96.3 | 98.1 | 97.2 | 98.5 | 98.5 | 98.5 |
| b_event_sense | 89.3 | 89.3 | 89.3 | 96.3 | 96.3 | 96.3 |
| c_aspect | 58.3 | 49.3 | 53.4 | 81.0 | 56.7 | 66.7 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 69.2 | 37.5 | 48.6 | 100.0 | 100.0 | 100.0 |
| c_polarity | 66.7 | 100.0 | 80.0 | – | – | – |
| c_refer | 85.7 | 35.3 | 50.0 | 83.3 | 90.9 | 87.0 |
| d_core_args_abstract | 42.1 | 66.7 | 51.6 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 57.1 | 54.9 | 56.0 | 90.9 | 95.2 | 93.0 |
| d_peripheral_entity | 40.1 | 40.9 | 40.5 | 91.7 | 84.6 | 88.0 |
| d_peripheral_event | 31.4 | 23.9 | 27.1 | 75.0 | 85.7 | 80.0 |
| e_core_labels | 82.9 | 82.9 | 82.9 | 100.0 | 100.0 | 100.0 |
| e_peripheral_labels | 76.9 | 76.9 | 76.9 | 95.8 | 95.8 | 95.8 |
| f_name_tokens | 52.4 | 42.3 | 46.8 | 76.5 | 76.5 | 76.5 |
| f_wiki | – | – | – | 100.0 | 94.1 | 97.0 |
| g_reentrancy | 44.4 | 16.7 | 24.2 | 85.7 | 92.3 | 88.9 |
| h_temporal | 38.1 | 25.3 | 30.4 | 73.7 | 41.2 | 52.8 |
| i_modal | 54.9 | 46.5 | 50.3 | 88.6 | 54.2 | 67.2 |
| j_coref_chain | 45.0 | 7.0 | 12.1 | 100.0 | 64.7 | 78.6 |
| j_coref_subset | – | 0.0 | 0.0 | – | – | – |
| k_doc_format | 99.6 | 99.6 | 99.6 | 100.0 | 100.0 | 100.0 |
