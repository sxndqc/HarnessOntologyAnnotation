# runs/chat/s1-abridged/claude-ai

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 52.2 | 52.1 | 52.2 | 78.1 | no (2) | 69.5 | 68.0 | 81.0 |
| zh-0028 | 12 | 49.4 | 54.4 | 51.8 | 61.0 | yes | 43.6 | 45.3 | 55.4 |
| zh-0032 | 6 | 43.9 | 46.7 | 45.3 | 54.3 | yes | 39.2 | 35.7 | 54.0 |
| **zh** (2/15 files) | 18 | 46.5 | 3.6 | 6.8 | 7.7 | 2/2 | 41.4 | 40.5 | 54.7 |
| **en** (1/5 files) | 9 | 52.2 | 2.0 | 3.8 | 5.3 | 0/1 | 69.5 | 68.0 | 81.0 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 78.7 | 93.9 |
| a_entity_found | 93.6 | 92.5 |
| a_event_concept | 78.6 | 86.7 |
| a_event_found | 95.4 | 96.8 |
| a_granularity | 98.0 | 96.2 |
| b_event_sense | 88.5 | 82.6 |
| c_aspect | 48.8 | 65.2 |
| c_modstr | – | – |
| c_other_attributes | 36.6 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 28.6 | 80.0 |
| d_core_args_abstract | 32.3 | 100.0 |
| d_core_args_event | 50.8 | 70.9 |
| d_peripheral_entity | 47.2 | 79.5 |
| d_peripheral_event | 29.1 | 83.3 |
| e_core_labels | 69.0 | 88.9 |
| e_peripheral_labels | 80.0 | 95.7 |
| f_name_tokens | 40.8 | 96.8 |
| f_wiki | 0.0 | 0.0 |
| g_reentrancy | 30.0 | 69.6 |
| h_temporal | 27.3 | 46.8 |
| i_modal | 57.7 | 84.0 |
| j_coref_chain | 13.8 | 73.3 |
| j_coref_subset | – | – |
| k_doc_format | 100.0 | 100.0 |
