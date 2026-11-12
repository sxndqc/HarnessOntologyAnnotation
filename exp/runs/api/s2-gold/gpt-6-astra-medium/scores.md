# runs/api/s2-gold/gpt-6-astra-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 46.1 | 47.3 | 46.7 | 73.4 | no (2) | 62.1 | 59.5 |
| zh-0028 | 12 | 49.7 | 57.9 | 53.5 | 62.3 | yes | 45.9 | 46.1 |
| zh-0032 | 6 | 43.7 | 44.8 | 44.2 | 54.2 | yes | 39.1 | 33.8 |
| **zh** (2/15 files) | 18 | 46.7 | 3.7 | 6.8 | 7.8 | 2/2 | 42.5 | 39.9 |
| **en** (1/5 files) | 9 | 46.1 | 1.8 | 3.5 | 5.1 | 0/1 | 62.1 | 59.5 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 82.7 | 82.7 | 82.7 | 92.0 | 92.0 | 92.0 |
| a_entity_found | 88.7 | 94.3 | 91.4 | 96.2 | 90.9 | 93.5 |
| a_event_concept | 78.0 | 78.0 | 78.0 | 86.7 | 86.7 | 86.7 |
| a_event_found | 93.2 | 98.8 | 95.9 | 93.8 | 96.8 | 95.2 |
| a_granularity | 96.3 | 97.6 | 97.0 | 97.1 | 95.7 | 96.4 |
| b_event_sense | 87.7 | 87.7 | 87.7 | 75.0 | 75.0 | 75.0 |
| c_aspect | 50.0 | 43.3 | 46.4 | 66.7 | 58.3 | 62.2 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 61.5 | 33.3 | 43.2 | 100.0 | 100.0 | 100.0 |
| c_polarity | 66.7 | 66.7 | 66.7 | – | – | – |
| c_refer | 100.0 | 46.2 | 63.2 | 90.9 | 90.9 | 90.9 |
| d_core_args_abstract | 38.6 | 61.1 | 47.3 | 83.3 | 83.3 | 83.3 |
| d_core_args_event | 58.0 | 58.0 | 58.0 | 57.3 | 75.2 | 65.0 |
| d_peripheral_entity | 40.4 | 41.3 | 40.8 | 79.5 | 72.9 | 76.1 |
| d_peripheral_event | 32.5 | 22.8 | 26.8 | 60.4 | 53.7 | 56.9 |
| e_core_labels | 81.0 | 81.0 | 81.0 | 87.5 | 87.5 | 87.5 |
| e_peripheral_labels | 82.4 | 82.4 | 82.4 | 90.9 | 90.9 | 90.9 |
| f_name_tokens | 55.0 | 42.3 | 47.8 | 68.8 | 73.3 | 71.0 |
| f_wiki | – | – | – | 0.0 | – | 0.0 |
| g_reentrancy | 44.4 | 23.5 | 30.8 | 42.9 | 66.7 | 52.2 |
| h_temporal | 34.7 | 21.1 | 26.3 | 42.1 | 26.7 | 32.7 |
| i_modal | 54.9 | 46.5 | 50.3 | 88.6 | 69.6 | 78.0 |
| j_coref_chain | 49.6 | 9.2 | 15.6 | 81.8 | 47.4 | 60.0 |
| j_coref_subset | – | 0.0 | 0.0 | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
