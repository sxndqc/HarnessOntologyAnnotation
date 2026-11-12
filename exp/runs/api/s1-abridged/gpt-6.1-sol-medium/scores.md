# runs/api/s1-abridged/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 44.1 | 45.2 | 44.6 | 72.2 | no (2) | 60.1 | 59.8 |
| zh-0028 | 12 | 45.9 | 57.0 | 50.9 | 59.6 | yes | 42.4 | 42.2 |
| zh-0032 | 6 | 43.6 | 46.3 | 44.9 | 55.1 | no (1) | 40.4 | 35.3 |
| **zh** (2/15 files) | 18 | 44.8 | 3.7 | 6.9 | 7.8 | 1/2 | 41.4 | 38.8 |
| **en** (1/5 files) | 9 | 44.1 | 1.7 | 3.3 | 5.0 | 0/1 | 60.1 | 59.8 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 78.6 | 78.6 | 78.6 | 93.9 | 93.9 | 93.9 |
| a_entity_found | 92.8 | 92.8 | 92.8 | 94.2 | 90.7 | 92.5 |
| a_event_concept | 78.8 | 78.8 | 78.8 | 83.3 | 83.3 | 83.3 |
| a_event_found | 96.6 | 98.8 | 97.7 | 93.8 | 96.8 | 95.2 |
| a_granularity | 95.9 | 97.2 | 96.6 | 96.9 | 95.5 | 96.2 |
| b_event_sense | 86.7 | 86.7 | 86.7 | 78.3 | 78.3 | 78.3 |
| c_aspect | 54.1 | 46.5 | 50.0 | 66.7 | 58.3 | 62.2 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 53.8 | 28.0 | 36.8 | 100.0 | 100.0 | 100.0 |
| c_polarity | 33.3 | 33.3 | 33.3 | – | – | – |
| c_refer | 85.7 | 35.3 | 50.0 | 81.8 | 90.0 | 85.7 |
| d_core_args_abstract | 22.5 | 37.5 | 28.1 | 83.3 | 83.3 | 83.3 |
| d_core_args_event | 55.3 | 53.3 | 54.3 | 51.6 | 72.2 | 60.2 |
| d_peripheral_entity | 39.1 | 35.3 | 37.1 | 70.5 | 70.5 | 70.5 |
| d_peripheral_event | 29.0 | 23.0 | 25.6 | 79.2 | 52.8 | 63.3 |
| e_core_labels | 75.9 | 75.9 | 75.9 | 81.8 | 81.8 | 81.8 |
| e_peripheral_labels | 77.6 | 77.6 | 77.6 | 95.2 | 95.2 | 95.2 |
| f_name_tokens | 52.2 | 46.2 | 49.0 | 56.2 | 60.0 | 58.1 |
| f_wiki | – | – | – | 0.0 | – | 0.0 |
| g_reentrancy | 38.9 | 20.6 | 26.9 | 42.9 | 54.5 | 48.0 |
| h_temporal | 31.4 | 19.1 | 23.7 | 52.6 | 34.5 | 41.7 |
| i_modal | 57.6 | 46.6 | 51.6 | 84.1 | 66.1 | 74.0 |
| j_coref_chain | 17.0 | 3.0 | 5.1 | 100.0 | 57.9 | 73.3 |
| j_coref_subset | – | – | – | – | – | – |
| k_doc_format | 99.6 | 99.6 | 99.6 | 100.0 | 100.0 | 100.0 |
