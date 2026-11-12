# runs/api/s2-search/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 53.3 | 54.8 | 54.0 | 79.5 | no (2) | 69.7 | 68.5 |
| zh-0028 | 12 | 51.7 | 56.4 | 53.9 | 63.6 | yes | 47.5 | 48.1 |
| zh-0032 | 6 | 47.0 | 45.7 | 46.4 | 54.3 | no (20) | 40.7 | 37.2 |
| **zh** (2/15 files) | 18 | 49.4 | 3.7 | 6.8 | 7.8 | 1/2 | 44.1 | 42.7 |
| **en** (1/5 files) | 9 | 53.3 | 2.1 | 4.0 | 5.5 | 0/1 | 69.7 | 68.5 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 79.2 | 79.2 | 79.2 | 95.9 | 95.9 | 95.9 |
| a_entity_found | 91.0 | 96.7 | 93.7 | 94.2 | 92.5 | 93.3 |
| a_event_concept | 80.5 | 80.5 | 80.5 | 82.8 | 82.8 | 82.8 |
| a_event_found | 93.2 | 100.0 | 96.5 | 90.6 | 100.0 | 95.1 |
| a_granularity | 96.8 | 97.7 | 97.2 | 96.9 | 95.5 | 96.2 |
| b_event_sense | 90.0 | 90.0 | 90.0 | 90.9 | 90.9 | 90.9 |
| c_aspect | 50.8 | 45.6 | 48.1 | 66.7 | 56.0 | 60.9 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 53.8 | 30.4 | 38.9 | 100.0 | 100.0 | 100.0 |
| c_polarity | 33.3 | 50.0 | 40.0 | – | – | – |
| c_refer | 85.7 | 50.0 | 63.2 | 75.0 | 90.0 | 81.8 |
| d_core_args_abstract | 40.2 | 75.9 | 52.6 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 57.5 | 55.5 | 56.5 | 59.5 | 65.8 | 62.5 |
| d_peripheral_entity | 41.8 | 41.0 | 41.4 | 81.2 | 88.6 | 84.8 |
| d_peripheral_event | 36.2 | 27.8 | 31.4 | 81.2 | 59.1 | 68.4 |
| e_core_labels | 79.0 | 79.0 | 79.0 | 84.8 | 84.8 | 84.8 |
| e_peripheral_labels | 83.0 | 83.0 | 83.0 | 91.7 | 91.7 | 91.7 |
| f_name_tokens | 54.5 | 44.4 | 49.0 | 93.3 | 93.3 | 93.3 |
| f_wiki | – | – | – | 64.3 | 64.3 | 64.3 |
| g_reentrancy | 50.0 | 29.0 | 36.7 | 64.3 | 90.0 | 75.0 |
| h_temporal | 39.0 | 31.5 | 34.8 | 63.2 | 48.0 | 54.5 |
| i_modal | 55.6 | 53.3 | 54.4 | 86.4 | 67.9 | 76.0 |
| j_coref_chain | 32.1 | 5.4 | 9.3 | 74.7 | 43.3 | 54.8 |
| j_coref_subset | – | 0.0 | 0.0 | – | – | – |
| k_doc_format | 99.6 | 99.6 | 99.6 | 100.0 | 100.0 | 100.0 |
