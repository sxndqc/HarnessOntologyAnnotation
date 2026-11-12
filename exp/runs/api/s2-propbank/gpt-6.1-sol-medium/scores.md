# runs/api/s2-propbank/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 47.1 | 50.0 | 48.5 | 75.9 | no (2) | 63.5 | 62.0 |
| zh-0028 | 12 | 47.1 | 56.1 | 51.3 | 61.4 | yes | 44.4 | 44.2 |
| zh-0032 | 6 | 41.9 | 46.1 | 43.9 | 54.8 | yes | 39.8 | 34.1 |
| **zh** (2/15 files) | 18 | 44.5 | 3.7 | 6.8 | 7.9 | 2/2 | 42.1 | 39.1 |
| **en** (1/5 files) | 9 | 47.1 | 1.9 | 3.6 | 5.3 | 0/1 | 63.5 | 62.0 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 76.6 | 76.6 | 76.6 | 92.0 | 92.0 | 92.0 |
| a_entity_found | 90.5 | 94.8 | 92.6 | 96.2 | 90.9 | 93.5 |
| a_event_concept | 79.8 | 79.8 | 79.8 | 90.0 | 90.0 | 90.0 |
| a_event_found | 95.5 | 100.0 | 97.7 | 93.8 | 100.0 | 96.8 |
| a_granularity | 96.3 | 98.1 | 97.2 | 97.1 | 95.7 | 96.4 |
| b_event_sense | 100.0 | 100.0 | 100.0 | 80.0 | 80.0 | 80.0 |
| c_aspect | 57.4 | 48.6 | 52.6 | 71.4 | 60.0 | 65.2 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 61.5 | 30.8 | 41.0 | 100.0 | 100.0 | 100.0 |
| c_polarity | 33.3 | 50.0 | 40.0 | – | – | – |
| c_refer | 85.7 | 35.3 | 50.0 | 91.7 | 84.6 | 88.0 |
| d_core_args_abstract | 24.1 | 39.4 | 29.9 | 83.3 | 83.3 | 83.3 |
| d_core_args_event | 63.7 | 60.3 | 61.9 | 57.7 | 71.3 | 63.8 |
| d_peripheral_entity | 40.3 | 41.1 | 40.7 | 56.8 | 48.1 | 52.1 |
| d_peripheral_event | 26.2 | 20.1 | 22.8 | 85.4 | 75.9 | 80.4 |
| e_core_labels | 88.3 | 88.3 | 88.3 | 90.3 | 90.3 | 90.3 |
| e_peripheral_labels | 74.5 | 74.5 | 74.5 | 85.0 | 85.0 | 85.0 |
| f_name_tokens | 55.0 | 36.7 | 44.0 | 56.2 | 60.0 | 58.1 |
| f_wiki | – | – | – | 33.3 | 62.5 | 43.5 |
| g_reentrancy | 38.9 | 15.2 | 21.9 | 50.0 | 70.0 | 58.3 |
| h_temporal | 28.0 | 16.8 | 21.0 | 63.2 | 40.0 | 49.0 |
| i_modal | 56.2 | 45.0 | 50.0 | 88.6 | 69.6 | 78.0 |
| j_coref_chain | 45.0 | 7.2 | 12.4 | 81.8 | 42.9 | 56.2 |
| j_coref_subset | – | – | – | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
