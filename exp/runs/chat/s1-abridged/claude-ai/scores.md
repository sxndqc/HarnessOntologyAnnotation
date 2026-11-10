# runs/chat/s1-abridged/claude-ai

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0032 | 6 | 43.9 | 46.7 | 45.3 | 53.4 | yes | 39.2 | 35.7 | 54.0 |
| **zh** (1/15 files) | 6 | 43.9 | 1.8 | 3.5 | 3.8 | 1/1 | 39.2 | 35.7 | 54.0 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 75.3 |
| a_entity_found | 91.4 |
| a_event_concept | 89.6 |
| a_event_found | 99.0 |
| a_granularity | 96.0 |
| b_event_sense | 88.1 |
| c_aspect | 40.5 |
| c_modstr | – |
| c_other_attributes | 25.0 |
| c_polarity | 66.7 |
| c_refer | 0.0 |
| d_core_args_abstract | 40.0 |
| d_core_args_event | 57.5 |
| d_peripheral_entity | 34.2 |
| d_peripheral_event | 14.6 |
| e_core_labels | 90.5 |
| e_peripheral_labels | 70.6 |
| f_name_tokens | 52.9 |
| f_wiki | 0.0 |
| g_reentrancy | 48.3 |
| h_temporal | 9.5 |
| i_modal | 43.0 |
| j_coref_chain | 10.0 |
| j_coref_subset | – |
| k_doc_format | 100.0 |
