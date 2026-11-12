# runs/api/s1-full/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 55.1 | 64.0 | 59.2 | 86.0 | no (10) | 83.9 | 79.8 |
| zh-0028 | 12 | 44.3 | 54.4 | 48.8 | 59.6 | no (7) | 43.3 | 41.8 |
| zh-0032 | 6 | 39.9 | 43.0 | 41.4 | 50.6 | no (6) | 33.8 | 32.6 |
| **zh** (2/15 files) | 18 | 42.1 | 3.5 | 6.5 | 7.6 | 0/2 | 38.5 | 37.2 |
| **en** (1/5 files) | 9 | 55.1 | 2.4 | 4.6 | 6.3 | 0/1 | 83.9 | 79.8 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 79.2 | 79.2 | 79.2 | 94.0 | 94.0 | 94.0 |
| a_entity_found | 91.0 | 94.0 | 92.4 | 96.2 | 92.6 | 94.3 |
| a_event_concept | 72.0 | 72.0 | 72.0 | 96.8 | 96.8 | 96.8 |
| a_event_found | 93.2 | 98.8 | 95.9 | 96.9 | 93.9 | 95.4 |
| a_granularity | 96.2 | 97.6 | 96.9 | 98.5 | 98.5 | 98.5 |
| b_event_sense | 92.5 | 92.5 | 92.5 | 96.3 | 96.3 | 96.3 |
| c_aspect | 55.0 | 52.4 | 53.7 | 81.0 | 85.0 | 82.9 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 61.5 | 28.6 | 39.0 | 100.0 | 100.0 | 100.0 |
| c_polarity | 66.7 | 66.7 | 66.7 | – | – | – |
| c_refer | 57.1 | 25.0 | 34.8 | 83.3 | 90.9 | 87.0 |
| d_core_args_abstract | 28.9 | 45.8 | 35.5 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 43.3 | 43.3 | 43.3 | 83.3 | 87.3 | 85.3 |
| d_peripheral_entity | 37.2 | 36.4 | 36.8 | 83.3 | 83.3 | 83.3 |
| d_peripheral_event | 28.0 | 22.8 | 25.2 | 75.0 | 85.7 | 80.0 |
| e_core_labels | 77.5 | 77.5 | 77.5 | 100.0 | 100.0 | 100.0 |
| e_peripheral_labels | 79.2 | 79.2 | 79.2 | 95.7 | 95.7 | 95.7 |
| f_name_tokens | 55.0 | 36.7 | 44.0 | 100.0 | 100.0 | 100.0 |
| f_wiki | – | – | – | 100.0 | 94.1 | 97.0 |
| g_reentrancy | 33.3 | 12.0 | 17.6 | 100.0 | 82.4 | 90.3 |
| h_temporal | 28.0 | 20.4 | 23.6 | 73.7 | 51.9 | 60.9 |
| i_modal | 56.0 | 52.4 | 54.1 | 79.5 | 70.0 | 74.5 |
| j_coref_chain | 6.1 | 1.1 | 1.8 | 90.9 | 55.6 | 69.0 |
| j_coref_subset | – | – | – | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 | 99.0 | 99.0 | 99.0 |
