# runs/api/s1-full/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 56.2 | 56.8 | 56.5 | 80.9 | no (2) | 71.4 | 70.7 |
| zh-0028 | 12 | 50.3 | 52.4 | 51.3 | 61.2 | yes | 42.6 | 44.4 |
| zh-0032 | 6 | 49.9 | 45.0 | 47.3 | 55.2 | yes | 38.7 | 36.2 |
| **zh** (2/15 files) | 18 | 50.1 | 3.5 | 6.6 | 7.6 | 2/2 | 40.7 | 40.3 |
| **en** (1/5 files) | 9 | 56.2 | 2.1 | 4.1 | 5.5 | 0/1 | 71.4 | 70.7 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 79.1 | 79.1 | 79.1 | 94.0 | 94.0 | 94.0 |
| a_entity_found | 90.5 | 96.2 | 93.3 | 96.2 | 90.9 | 93.5 |
| a_event_concept | 74.4 | 74.4 | 74.4 | 93.5 | 93.5 | 93.5 |
| a_event_found | 93.2 | 100.0 | 96.5 | 96.9 | 96.9 | 96.9 |
| a_granularity | 96.7 | 96.7 | 96.7 | 97.1 | 95.7 | 96.4 |
| b_event_sense | 87.7 | 87.7 | 87.7 | 92.3 | 92.3 | 92.3 |
| c_aspect | 47.5 | 43.8 | 45.5 | 76.2 | 76.2 | 76.2 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 69.2 | 37.5 | 48.6 | 100.0 | 100.0 | 100.0 |
| c_polarity | 33.3 | 33.3 | 33.3 | – | – | – |
| c_refer | 71.4 | 55.6 | 62.5 | 75.0 | 90.0 | 81.8 |
| d_core_args_abstract | 32.4 | 64.8 | 43.2 | 83.3 | 83.3 | 83.3 |
| d_core_args_event | 49.7 | 49.7 | 49.7 | 63.6 | 70.0 | 66.7 |
| d_peripheral_entity | 36.2 | 34.0 | 35.1 | 78.5 | 78.5 | 78.5 |
| d_peripheral_event | 37.1 | 28.2 | 32.0 | 62.5 | 62.5 | 62.5 |
| e_core_labels | 74.4 | 74.4 | 74.4 | 94.1 | 94.1 | 94.1 |
| e_peripheral_labels | 78.4 | 78.4 | 78.4 | 90.9 | 90.9 | 90.9 |
| f_name_tokens | 45.8 | 39.3 | 42.3 | 93.8 | 100.0 | 96.8 |
| f_wiki | – | – | – | 0.0 | – | 0.0 |
| g_reentrancy | 44.4 | 32.0 | 37.2 | 64.3 | 100.0 | 78.3 |
| h_temporal | 33.9 | 37.0 | 35.4 | 73.7 | 58.3 | 65.1 |
| i_modal | 50.0 | 66.7 | 57.1 | 86.4 | 73.1 | 79.2 |
| j_coref_chain | 3.8 | 0.8 | 1.4 | 81.8 | 52.9 | 64.3 |
| j_coref_subset | – | – | – | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 | 98.9 | 98.9 | 98.9 |
