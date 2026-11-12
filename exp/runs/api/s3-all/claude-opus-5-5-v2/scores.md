# runs/api/s3-all/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 51.8 | 51.8 | 51.8 | 78.6 | no (2) | 70.3 | 69.7 |
| zh-0028 | 12 | 48.9 | 52.4 | 50.6 | 58.4 | yes | 40.7 | 43.0 |
| zh-0032 | 6 | 46.8 | 47.5 | 47.1 | 56.2 | yes | 42.0 | 36.3 |
| **zh** (2/15 files) | 18 | 47.8 | 3.6 | 6.7 | 7.6 | 2/2 | 41.3 | 39.6 |
| **en** (1/5 files) | 9 | 51.8 | 2.0 | 3.8 | 5.4 | 0/1 | 70.3 | 69.7 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 77.1 | 77.1 | 77.1 | 93.8 | 93.8 | 93.8 |
| a_entity_found | 90.5 | 97.1 | 93.7 | 92.3 | 92.3 | 92.3 |
| a_event_concept | 79.5 | 79.5 | 79.5 | 89.7 | 89.7 | 89.7 |
| a_event_found | 94.3 | 100.0 | 97.1 | 90.6 | 100.0 | 95.1 |
| a_granularity | 96.7 | 96.7 | 96.7 | 96.9 | 95.5 | 96.2 |
| b_event_sense | 91.9 | 91.9 | 91.9 | 87.5 | 87.5 | 87.5 |
| c_aspect | 48.3 | 43.3 | 45.7 | 66.7 | 56.0 | 60.9 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 57.1 | 30.8 | 40.0 | 100.0 | 100.0 | 100.0 |
| c_polarity | 50.0 | 50.0 | 50.0 | – | – | – |
| c_refer | 85.7 | 50.0 | 63.2 | 80.0 | 88.9 | 84.2 |
| d_core_args_abstract | 13.0 | 29.2 | 17.9 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 60.8 | 58.6 | 59.7 | 73.8 | 81.6 | 77.5 |
| d_peripheral_entity | 40.6 | 38.1 | 39.3 | 70.5 | 77.5 | 73.8 |
| d_peripheral_event | 34.1 | 30.1 | 32.0 | 93.8 | 75.0 | 83.3 |
| e_core_labels | 82.4 | 82.4 | 82.4 | 97.0 | 97.0 | 97.0 |
| e_peripheral_labels | 78.8 | 78.8 | 78.8 | 95.5 | 95.5 | 95.5 |
| f_name_tokens | 57.1 | 41.4 | 48.0 | 68.8 | 73.3 | 71.0 |
| f_wiki | – | 0.0 | 0.0 | 46.7 | 87.5 | 60.9 |
| g_reentrancy | 38.9 | 28.0 | 32.6 | 64.3 | 90.0 | 75.0 |
| h_temporal | 30.5 | 26.5 | 28.3 | 63.2 | 48.0 | 54.5 |
| i_modal | 54.2 | 52.7 | 53.4 | 84.1 | 66.1 | 74.0 |
| j_coref_chain | 27.0 | 5.0 | 8.4 | 100.0 | 57.9 | 73.3 |
| j_coref_subset | – | – | – | – | – | – |
| k_doc_format | 99.5 | 99.5 | 99.5 | 100.0 | 100.0 | 100.0 |
