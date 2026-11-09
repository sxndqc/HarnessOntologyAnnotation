# runs/api/s1-abridged/claude-opus-5-5

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0032 | 6 | 43.4 | 44.6 | 44.0 | 54.4 | yes | 40.7 | 36.8 | 53.7 |
| **zh** (1/15 files) | 6 | 43.4 | 1.7 | 3.3 | 3.9 | 1/1 | 40.7 | 36.8 | 53.7 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 76.2 |
| a_entity_found | 90.8 |
| a_event_concept | 87.5 |
| a_event_found | 99.0 |
| a_granularity | 94.7 |
| b_event_sense | 90.2 |
| c_aspect | 45.3 |
| c_modstr | – |
| c_other_attributes | 25.0 |
| c_polarity | 66.7 |
| c_refer | 0.0 |
| d_core_args_abstract | 20.0 |
| d_core_args_event | 61.0 |
| d_peripheral_entity | 29.7 |
| d_peripheral_event | 12.5 |
| e_core_labels | 92.9 |
| e_peripheral_labels | 62.5 |
| f_name_tokens | 60.6 |
| f_wiki | 0.0 |
| g_reentrancy | 48.3 |
| h_temporal | 19.7 |
| i_modal | 41.5 |
| j_coref_chain | 10.0 |
| j_coref_subset | – |
| k_doc_format | 100.0 |
