# runs/chat/s2-propbank/claude-chat

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0032 | 6 | 43.3 | 46.7 | 44.9 | 54.7 | no (2) | 39.0 | 35.8 |
| **zh** (1/15 files) | 6 | 43.3 | 1.8 | 3.5 | 3.9 | 0/1 | 39.0 | 35.8 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 77.6 | 77.6 | 77.6 |
| a_entity_found | 84.2 | 100.0 | 91.4 |
| a_event_concept | 87.5 | 87.5 | 87.5 |
| a_event_found | 98.0 | 100.0 | 99.0 |
| a_granularity | 92.9 | 96.3 | 94.6 |
| b_event_sense | 92.7 | 92.7 | 92.7 |
| c_aspect | 38.2 | 31.7 | 34.7 |
| c_modstr | – | – | – |
| c_other_attributes | 50.0 | 50.0 | 50.0 |
| c_polarity | 50.0 | 100.0 | 66.7 |
| c_refer | – | 0.0 | 0.0 |
| d_core_args_abstract | 12.5 | 50.0 | 20.0 |
| d_core_args_event | 63.7 | 61.9 | 62.8 |
| d_peripheral_entity | 32.5 | 36.1 | 34.2 |
| d_peripheral_event | 26.7 | 23.5 | 25.0 |
| e_core_labels | 95.1 | 95.1 | 95.1 |
| e_peripheral_labels | 73.7 | 73.7 | 73.7 |
| f_name_tokens | 47.1 | 50.0 | 48.5 |
| f_wiki | – | 0.0 | 0.0 |
| g_reentrancy | 66.7 | 26.1 | 37.5 |
| h_temporal | 24.2 | 13.6 | 17.4 |
| i_modal | 50.0 | 36.4 | 42.1 |
| j_coref_chain | 50.0 | 5.9 | 10.5 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
