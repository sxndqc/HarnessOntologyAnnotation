# runs/api/s2-propbank/claude-opus-5-5

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 38.0 | 43.9 | 40.7 | 59.4 | yes | 42.9 | 44.3 | 56.7 |
| zh-0032 | 6 | 42.4 | 44.2 | 43.3 | 54.9 | yes | 39.8 | 36.0 | 53.2 |
| **zh** (2/15 files) | 18 | 40.2 | 3.2 | 5.9 | 7.7 | 2/2 | 41.4 | 40.1 | 53.8 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 75.5 |
| a_entity_found | 94.1 |
| a_event_concept | 72.3 |
| a_event_found | 95.5 |
| a_granularity | 95.5 |
| b_event_sense | 94.8 |
| c_aspect | 50.2 |
| c_modstr | – |
| c_other_attributes | 36.6 |
| c_polarity | 83.3 |
| c_refer | 24.0 |
| d_core_args_abstract | 12.3 |
| d_core_args_event | 60.6 |
| d_peripheral_entity | 41.1 |
| d_peripheral_event | 37.2 |
| e_core_labels | 77.6 |
| e_peripheral_labels | 74.9 |
| f_name_tokens | 46.1 |
| f_wiki | 0.0 |
| g_reentrancy | 23.3 |
| h_temporal | 29.1 |
| i_modal | 55.8 |
| j_coref_chain | 12.3 |
| j_coref_subset | 0.0 |
| k_doc_format | 100.0 |
