# runs/chat/s1-abridged/claude-ai

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 52.2 | 52.1 | 52.2 | 78.1 | no (2) | 69.5 | 68.0 |
| zh-0028 | 12 | 49.4 | 54.4 | 51.8 | 61.0 | yes | 43.6 | 45.3 |
| zh-0032 | 6 | 43.9 | 46.7 | 45.3 | 53.8 | yes | 39.2 | 35.7 |
| **zh** (2/15 files) | 18 | 46.5 | 3.6 | 6.8 | 7.6 | 2/2 | 41.4 | 40.5 |
| **en** (1/5 files) | 9 | 52.2 | 2.0 | 3.8 | 5.3 | 0/1 | 69.5 | 68.0 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 79.2 | 79.2 | 79.2 | 93.9 | 93.9 | 93.9 |
| a_entity_found | 91.0 | 97.1 | 94.0 | 94.2 | 90.7 | 92.5 |
| a_event_concept | 80.5 | 80.5 | 80.5 | 86.7 | 86.7 | 86.7 |
| a_event_found | 93.2 | 98.8 | 95.9 | 93.8 | 100.0 | 96.8 |
| a_granularity | 97.2 | 98.6 | 97.9 | 96.9 | 95.5 | 96.2 |
| b_event_sense | 88.3 | 88.3 | 88.3 | 82.6 | 82.6 | 82.6 |
| c_aspect | 50.8 | 44.9 | 47.7 | 71.4 | 60.0 | 65.2 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 61.5 | 33.3 | 43.2 | 100.0 | 100.0 | 100.0 |
| c_polarity | 33.3 | 100.0 | 50.0 | – | – | – |
| c_refer | 100.0 | 35.3 | 52.2 | 72.7 | 88.9 | 80.0 |
| d_core_args_abstract | 22.5 | 34.8 | 27.4 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 52.8 | 52.8 | 52.8 | 65.9 | 76.9 | 70.9 |
| d_peripheral_entity | 49.3 | 49.3 | 49.3 | 79.5 | 79.5 | 79.5 |
| d_peripheral_event | 29.1 | 23.1 | 25.8 | 93.8 | 75.0 | 83.3 |
| e_core_labels | 69.5 | 69.5 | 69.5 | 88.9 | 88.9 | 88.9 |
| e_peripheral_labels | 83.6 | 83.6 | 83.6 | 95.7 | 95.7 | 95.7 |
| f_name_tokens | 50.0 | 42.3 | 45.8 | 93.8 | 100.0 | 96.8 |
| f_wiki | – | 0.0 | 0.0 | 0.0 | – | 0.0 |
| g_reentrancy | 44.4 | 28.6 | 34.8 | 57.1 | 88.9 | 69.6 |
| h_temporal | 30.5 | 20.7 | 24.7 | 57.9 | 39.3 | 46.8 |
| i_modal | 60.4 | 50.6 | 55.1 | 95.5 | 75.0 | 84.0 |
| j_coref_chain | 44.5 | 7.9 | 13.4 | 100.0 | 57.9 | 73.3 |
| j_coref_subset | – | – | – | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
