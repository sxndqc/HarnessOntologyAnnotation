# runs/api/s2-gold/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 50.6 | 52.4 | 51.5 | 78.4 | no (2) | 70.4 | 66.3 |
| zh-0028 | 12 | 52.1 | 56.8 | 54.4 | 61.4 | yes | 45.0 | 46.5 |
| zh-0032 | 6 | 44.8 | 45.3 | 45.1 | 54.1 | yes | 40.3 | 34.6 |
| **zh** (2/15 files) | 18 | 48.4 | 3.7 | 6.8 | 7.6 | 2/2 | 42.7 | 40.5 |
| **en** (1/5 files) | 9 | 50.6 | 2.0 | 3.8 | 5.5 | 0/1 | 70.4 | 66.3 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 80.7 | 80.7 | 80.7 | 93.8 | 93.8 | 93.8 |
| a_entity_found | 91.0 | 96.7 | 93.7 | 92.3 | 92.3 | 92.3 |
| a_event_concept | 77.4 | 77.4 | 77.4 | 89.7 | 89.7 | 89.7 |
| a_event_found | 95.5 | 100.0 | 97.7 | 90.6 | 96.7 | 93.5 |
| a_granularity | 97.3 | 98.6 | 97.9 | 96.9 | 95.4 | 96.1 |
| b_event_sense | 88.1 | 88.1 | 88.1 | 83.3 | 83.3 | 83.3 |
| c_aspect | 46.7 | 41.2 | 43.8 | 61.9 | 52.0 | 56.5 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 57.1 | 36.4 | 44.4 | 100.0 | 100.0 | 100.0 |
| c_polarity | 50.0 | 50.0 | 50.0 | – | – | – |
| c_refer | 100.0 | 54.5 | 70.6 | 80.0 | 88.9 | 84.2 |
| d_core_args_abstract | 14.9 | 25.8 | 18.9 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 53.5 | 53.5 | 53.5 | 69.4 | 81.0 | 74.8 |
| d_peripheral_entity | 42.8 | 42.8 | 42.8 | 75.0 | 82.5 | 78.6 |
| d_peripheral_event | 32.6 | 25.0 | 28.3 | 81.2 | 59.1 | 68.4 |
| e_core_labels | 67.1 | 67.1 | 67.1 | 90.9 | 90.9 | 90.9 |
| e_peripheral_labels | 82.7 | 82.7 | 82.7 | 95.5 | 95.5 | 95.5 |
| f_name_tokens | 59.1 | 46.4 | 52.0 | 93.8 | 100.0 | 96.8 |
| f_wiki | – | – | – | 60.0 | 60.0 | 60.0 |
| g_reentrancy | 33.3 | 24.0 | 27.9 | 64.3 | 90.0 | 75.0 |
| h_temporal | 31.4 | 23.4 | 26.8 | 49.1 | 40.6 | 44.4 |
| i_modal | 55.6 | 50.0 | 52.6 | 70.5 | 53.4 | 60.8 |
| j_coref_chain | 29.9 | 5.3 | 9.0 | 100.0 | 57.9 | 73.3 |
| j_coref_subset | – | – | – | – | – | – |
| k_doc_format | 99.2 | 99.2 | 99.2 | 97.8 | 97.8 | 97.8 |
