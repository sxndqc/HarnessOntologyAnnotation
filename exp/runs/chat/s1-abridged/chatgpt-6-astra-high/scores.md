# runs/chat/s1-abridged/chatgpt-6-astra-high

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0032 | 6 | 46.5 | 45.9 | 46.2 | 54.9 | yes | 41.4 | 37.2 |
| **zh** (1/15 files) | 6 | 46.5 | 1.8 | 3.4 | 3.8 | 1/1 | 41.4 | 37.2 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 73.8 | 73.8 | 73.8 |
| a_entity_found | 79.2 | 100.0 | 88.4 |
| a_event_concept | 90.9 | 90.9 | 90.9 |
| a_event_found | 89.8 | 100.0 | 94.6 |
| a_granularity | 94.4 | 97.1 | 95.8 |
| b_event_sense | 84.6 | 84.6 | 84.6 |
| c_aspect | 45.5 | 37.5 | 41.1 |
| c_modstr | – | – | – |
| c_other_attributes | 50.0 | 50.0 | 50.0 |
| c_polarity | 50.0 | 100.0 | 66.7 |
| c_refer | – | 0.0 | 0.0 |
| d_core_args_abstract | 25.0 | 25.0 | 25.0 |
| d_core_args_event | 58.6 | 55.2 | 56.9 |
| d_peripheral_entity | 27.5 | 42.3 | 33.3 |
| d_peripheral_event | 20.0 | 15.0 | 17.1 |
| e_core_labels | 92.5 | 92.5 | 92.5 |
| e_peripheral_labels | 80.0 | 80.0 | 80.0 |
| f_name_tokens | 58.8 | 62.5 | 60.6 |
| f_wiki | – | – | – |
| g_reentrancy | 66.7 | 22.2 | 33.3 |
| h_temporal | 17.7 | 11.2 | 13.8 |
| i_modal | 50.0 | 40.8 | 44.9 |
| j_coref_chain | 0.0 | 0.0 | 0.0 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
