# runs/api/s1-abridged/gpt-6-astra-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 47.0 | 49.1 | 48.0 | 75.5 | no (2) | 67.1 | 64.6 |
| zh-0028 | 12 | 45.4 | 52.6 | 48.7 | 60.4 | yes | 43.9 | 45.4 |
| zh-0032 | 6 | 42.8 | 46.7 | 44.7 | 54.2 | no (1) | 40.6 | 35.7 |
| **zh** (2/15 files) | 18 | 44.0 | 3.6 | 6.6 | 7.8 | 1/2 | 42.2 | 40.5 |
| **en** (1/5 files) | 9 | 47.0 | 1.9 | 3.6 | 5.3 | 0/1 | 67.1 | 64.6 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 78.8 | 78.8 | 78.8 | 94.0 | 94.0 | 94.0 |
| a_entity_found | 91.4 | 95.3 | 93.3 | 96.2 | 89.3 | 92.6 |
| a_event_concept | 77.4 | 77.4 | 77.4 | 86.7 | 86.7 | 86.7 |
| a_event_found | 95.5 | 100.0 | 97.7 | 93.8 | 96.8 | 95.2 |
| a_granularity | 97.2 | 98.1 | 97.7 | 97.0 | 95.6 | 96.3 |
| b_event_sense | 89.8 | 89.8 | 89.8 | 73.9 | 73.9 | 73.9 |
| c_aspect | 55.7 | 47.9 | 51.5 | 66.7 | 58.3 | 62.2 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 53.8 | 25.9 | 35.0 | 100.0 | 100.0 | 100.0 |
| c_polarity | 66.7 | 100.0 | 80.0 | – | – | – |
| c_refer | 85.7 | 30.0 | 44.4 | 91.7 | 91.7 | 91.7 |
| d_core_args_abstract | 29.6 | 48.5 | 36.8 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 59.1 | 58.0 | 58.6 | 61.1 | 80.2 | 69.4 |
| d_peripheral_entity | 40.1 | 44.8 | 42.3 | 81.2 | 81.2 | 81.2 |
| d_peripheral_event | 33.3 | 24.7 | 28.4 | 79.2 | 52.8 | 63.3 |
| e_core_labels | 77.1 | 77.1 | 77.1 | 88.6 | 88.6 | 88.6 |
| e_peripheral_labels | 75.9 | 75.9 | 75.9 | 95.7 | 95.7 | 95.7 |
| f_name_tokens | 60.0 | 42.9 | 50.0 | 68.8 | 73.3 | 71.0 |
| f_wiki | – | – | – | 0.0 | – | 0.0 |
| g_reentrancy | 44.4 | 20.5 | 28.1 | 57.1 | 80.0 | 66.7 |
| h_temporal | 38.1 | 23.7 | 29.2 | 47.4 | 30.0 | 36.7 |
| i_modal | 59.0 | 47.8 | 52.8 | 88.6 | 69.6 | 78.0 |
| j_coref_chain | 20.8 | 3.9 | 6.5 | 100.0 | 57.9 | 73.3 |
| j_coref_subset | – | 0.0 | 0.0 | – | – | – |
| k_doc_format | 99.3 | 99.3 | 99.3 | 100.0 | 100.0 | 100.0 |
