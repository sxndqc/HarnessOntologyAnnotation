# runs/chat/s2-propbank/claude-ai

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0032 | 6 | 43.3 | 46.7 | 44.9 | 54.7 | no (2) | 39.0 | 35.8 | 54.8 |
| **zh** (1/15 files) | 6 | 43.3 | 1.8 | 3.5 | 3.9 | 0/1 | 39.0 | 35.8 | 54.8 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 77.6 |
| a_entity_found | 91.4 |
| a_event_concept | 87.5 |
| a_event_found | 99.0 |
| a_granularity | 94.6 |
| b_event_sense | 92.7 |
| c_aspect | 34.7 |
| c_modstr | – |
| c_other_attributes | 50.0 |
| c_polarity | 66.7 |
| c_refer | 0.0 |
| d_core_args_abstract | 20.0 |
| d_core_args_event | 62.8 |
| d_peripheral_entity | 34.2 |
| d_peripheral_event | 25.0 |
| e_core_labels | 95.1 |
| e_peripheral_labels | 73.7 |
| f_name_tokens | 48.5 |
| f_wiki | 0.0 |
| g_reentrancy | 37.5 |
| h_temporal | 17.4 |
| i_modal | 42.1 |
| j_coref_chain | 10.5 |
| j_coref_subset | – |
| k_doc_format | 100.0 |
