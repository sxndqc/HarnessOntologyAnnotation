# runs/api/s2-search/claude-opus-5-5

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 38.8 | 42.8 | 40.7 | 60.3 | yes | 43.6 | 44.4 | 58.6 |
| zh-0032 | 6 | 42.5 | 43.2 | 42.8 | 54.1 | yes | 39.8 | 36.8 | 53.4 |
| **zh** (2/15 files) | 18 | 40.7 | 3.1 | 5.8 | 7.6 | 2/2 | 41.7 | 40.6 | 54.7 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 79.0 |
| a_entity_found | 93.3 |
| a_event_concept | 76.7 |
| a_event_found | 95.9 |
| a_granularity | 92.6 |
| b_event_sense | 89.9 |
| c_aspect | 47.8 |
| c_modstr | – |
| c_other_attributes | 37.5 |
| c_polarity | 33.3 |
| c_refer | 33.3 |
| d_core_args_abstract | 36.5 |
| d_core_args_event | 47.7 |
| d_peripheral_entity | 38.8 |
| d_peripheral_event | 28.1 |
| e_core_labels | 74.3 |
| e_peripheral_labels | 72.9 |
| f_name_tokens | 56.2 |
| f_wiki | 0.0 |
| g_reentrancy | 29.2 |
| h_temporal | 29.4 |
| i_modal | 57.2 |
| j_coref_chain | 8.2 |
| j_coref_subset | – |
| k_doc_format | 100.0 |
