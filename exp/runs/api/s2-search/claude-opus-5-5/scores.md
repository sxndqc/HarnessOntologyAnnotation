# runs/api/s2-search/claude-opus-5-5

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 38.8 | 42.8 | 40.7 | 60.3 | yes | 43.6 | 44.4 | 58.6 |
| **zh** (1/15 files) | 12 | 38.8 | 1.5 | 2.8 | 4.0 | 1/1 | 43.6 | 44.4 | 58.6 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 79.7 |
| a_entity_found | 96.3 |
| a_event_concept | 67.6 |
| a_event_found | 91.9 |
| a_granularity | 91.9 |
| b_event_sense | 94.4 |
| c_aspect | 51.9 |
| c_modstr | – |
| c_other_attributes | 50.0 |
| c_polarity | 0.0 |
| c_refer | 66.7 |
| d_core_args_abstract | 53.0 |
| d_core_args_event | 37.8 |
| d_peripheral_entity | 50.6 |
| d_peripheral_event | 44.2 |
| e_core_labels | 60.5 |
| e_peripheral_labels | 85.7 |
| f_name_tokens | 37.5 |
| f_wiki | – |
| g_reentrancy | 11.8 |
| h_temporal | 45.2 |
| i_modal | 66.2 |
| j_coref_chain | 6.0 |
| j_coref_subset | – |
| k_doc_format | 100.0 |
