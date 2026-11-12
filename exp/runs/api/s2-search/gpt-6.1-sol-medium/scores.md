# runs/api/s2-search/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 51.0 | 61.0 | 55.6 | 86.0 | no (3) | 81.0 | 76.5 |
| zh-0028 | 12 | 50.9 | 57.7 | 54.1 | 64.1 | yes | 50.1 | 47.5 |
| zh-0032 | 6 | 40.7 | 46.5 | 43.4 | 53.9 | yes | 39.7 | 34.4 |
| **zh** (2/15 files) | 18 | 45.4 | 3.8 | 6.9 | 8.0 | 2/2 | 44.9 | 40.9 |
| **en** (1/5 files) | 9 | 51.0 | 2.3 | 4.4 | 6.3 | 0/1 | 81.0 | 76.5 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 79.2 | 79.2 | 79.2 | 94.1 | 94.1 | 94.1 |
| a_entity_found | 91.0 | 96.2 | 93.5 | 98.1 | 92.7 | 95.3 |
| a_event_concept | 81.7 | 81.7 | 81.7 | 96.8 | 96.8 | 96.8 |
| a_event_found | 93.2 | 100.0 | 96.5 | 96.9 | 93.9 | 95.4 |
| a_granularity | 96.2 | 98.1 | 97.1 | 98.5 | 98.5 | 98.5 |
| b_event_sense | 88.1 | 88.1 | 88.1 | 96.3 | 96.3 | 96.3 |
| c_aspect | 58.3 | 50.0 | 53.8 | 81.0 | 56.7 | 66.7 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 61.5 | 27.6 | 38.1 | 100.0 | 100.0 | 100.0 |
| c_polarity | 50.0 | 50.0 | 50.0 | – | – | – |
| c_refer | 100.0 | 41.2 | 58.3 | 83.3 | 90.9 | 87.0 |
| d_core_args_abstract | 55.9 | 79.2 | 65.5 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 57.9 | 59.0 | 58.4 | 90.9 | 95.2 | 93.0 |
| d_peripheral_entity | 43.3 | 47.3 | 45.2 | 91.7 | 84.6 | 88.0 |
| d_peripheral_event | 33.6 | 26.7 | 29.7 | 87.5 | 87.5 | 87.5 |
| e_core_labels | 87.7 | 87.7 | 87.7 | 100.0 | 100.0 | 100.0 |
| e_peripheral_labels | 76.8 | 76.8 | 76.8 | 96.0 | 96.0 | 96.0 |
| f_name_tokens | 44.0 | 40.7 | 42.3 | 76.5 | 76.5 | 76.5 |
| f_wiki | – | 0.0 | 0.0 | 100.0 | 94.1 | 97.0 |
| g_reentrancy | 50.0 | 20.9 | 29.5 | 85.7 | 92.3 | 88.9 |
| h_temporal | 28.8 | 17.9 | 22.1 | 73.7 | 41.2 | 52.8 |
| i_modal | 54.9 | 44.9 | 49.4 | 88.6 | 54.2 | 67.2 |
| j_coref_chain | 45.0 | 7.5 | 12.9 | 100.0 | 57.9 | 73.3 |
| j_coref_subset | – | – | – | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
