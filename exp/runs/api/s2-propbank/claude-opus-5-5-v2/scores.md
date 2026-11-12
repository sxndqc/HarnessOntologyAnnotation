# runs/api/s2-propbank/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 54.9 | 57.1 | 56.0 | 81.8 | no (2) | 73.6 | 71.1 |
| zh-0028 | 12 | 48.9 | 53.5 | 51.1 | 59.5 | yes | 44.0 | 45.7 |
| zh-0032 | 6 | 43.5 | 47.5 | 45.4 | 55.3 | no (1) | 39.1 | 34.7 |
| **zh** (2/15 files) | 18 | 46.0 | 3.6 | 6.8 | 7.7 | 1/2 | 41.5 | 40.2 |
| **en** (1/5 files) | 9 | 54.9 | 2.2 | 4.2 | 5.7 | 0/1 | 73.6 | 71.1 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 77.2 | 77.2 | 77.2 | 95.8 | 95.8 | 95.8 |
| a_entity_found | 88.7 | 98.0 | 93.1 | 92.3 | 90.6 | 91.4 |
| a_event_concept | 81.5 | 81.5 | 81.5 | 93.3 | 93.3 | 93.3 |
| a_event_found | 92.0 | 100.0 | 95.9 | 93.8 | 100.0 | 96.8 |
| a_granularity | 97.2 | 98.6 | 97.9 | 97.0 | 95.6 | 96.3 |
| b_event_sense | 98.3 | 98.3 | 98.3 | 88.5 | 88.5 | 88.5 |
| c_aspect | 47.5 | 42.0 | 44.6 | 66.7 | 53.8 | 59.6 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 61.5 | 33.3 | 43.2 | 100.0 | 100.0 | 100.0 |
| c_polarity | 33.3 | 50.0 | 40.0 | – | – | – |
| c_refer | 100.0 | 31.6 | 48.0 | 72.7 | 88.9 | 80.0 |
| d_core_args_abstract | 28.3 | 45.3 | 34.9 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 66.5 | 64.1 | 65.3 | 67.4 | 74.2 | 70.6 |
| d_peripheral_entity | 49.3 | 43.5 | 46.2 | 79.5 | 72.9 | 76.1 |
| d_peripheral_event | 23.9 | 26.2 | 25.0 | 87.5 | 70.0 | 77.8 |
| e_core_labels | 87.0 | 87.0 | 87.0 | 96.9 | 96.9 | 96.9 |
| e_peripheral_labels | 81.2 | 81.2 | 81.2 | 95.2 | 95.2 | 95.2 |
| f_name_tokens | 52.4 | 40.7 | 45.8 | 93.8 | 100.0 | 96.8 |
| f_wiki | – | 0.0 | 0.0 | 80.0 | 85.7 | 82.8 |
| g_reentrancy | 44.4 | 23.5 | 30.8 | 64.3 | 100.0 | 78.3 |
| h_temporal | 30.5 | 20.2 | 24.3 | 63.2 | 42.9 | 51.1 |
| i_modal | 59.7 | 48.9 | 53.8 | 84.1 | 63.8 | 72.5 |
| j_coref_chain | 33.3 | 5.8 | 9.9 | 100.0 | 57.9 | 73.3 |
| j_coref_subset | – | 0.0 | 0.0 | – | – | – |
| k_doc_format | 99.2 | 99.2 | 99.2 | 100.0 | 100.0 | 100.0 |
