# runs/harness/s1-full/claude-code

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 43.9 | 45.2 | 44.5 | 58.9 | yes | 39.5 | 41.0 | 56.7 |
| zh-0032 | 6 | 39.3 | 39.3 | 39.3 | 54.9 | yes | 40.2 | 36.2 | 54.8 |
| **zh** (2/15 files) | 18 | 41.5 | 3.0 | 5.7 | 7.4 | 2/2 | 39.9 | 38.6 | 55.8 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 78.0 |
| a_entity_found | 93.0 |
| a_event_concept | 73.4 |
| a_event_found | 94.6 |
| a_granularity | 96.8 |
| b_event_sense | 92.3 |
| c_aspect | 54.1 |
| c_modstr | – |
| c_other_attributes | 32.5 |
| c_polarity | 33.3 |
| c_refer | 29.4 |
| d_core_args_abstract | 24.2 |
| d_core_args_event | 53.6 |
| d_peripheral_entity | 36.7 |
| d_peripheral_event | 29.9 |
| e_core_labels | 72.1 |
| e_peripheral_labels | 74.2 |
| f_name_tokens | 42.5 |
| f_wiki | – |
| g_reentrancy | 30.0 |
| h_temporal | 27.4 |
| i_modal | 55.3 |
| j_coref_chain | 4.1 |
| j_coref_subset | – |
| k_doc_format | 100.0 |
