# runs/chat/s1-abridged/chatgpt-6-astra-high

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0032 | 6 | 46.5 | 45.9 | 46.2 | 54.9 | yes | 41.4 | 37.2 | 56.5 |
| **zh** (1/15 files) | 6 | 46.5 | 1.8 | 3.4 | 3.8 | 1/1 | 41.4 | 37.2 | 56.5 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 73.8 |
| a_entity_found | 88.4 |
| a_event_concept | 90.9 |
| a_event_found | 94.6 |
| a_granularity | 95.8 |
| b_event_sense | 84.6 |
| c_aspect | 41.1 |
| c_modstr | – |
| c_other_attributes | 50.0 |
| c_polarity | 66.7 |
| c_refer | 0.0 |
| d_core_args_abstract | 25.0 |
| d_core_args_event | 56.9 |
| d_peripheral_entity | 33.3 |
| d_peripheral_event | 17.1 |
| e_core_labels | 92.5 |
| e_peripheral_labels | 80.0 |
| f_name_tokens | 60.6 |
| f_wiki | – |
| g_reentrancy | 33.3 |
| h_temporal | 13.7 |
| i_modal | 44.9 |
| j_coref_chain | 0.0 |
| j_coref_subset | – |
| k_doc_format | 100.0 |
