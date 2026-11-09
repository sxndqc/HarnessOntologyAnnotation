# runs/api/s1-abridged/claude-opus-5-5

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 40.4 | 44.1 | 42.2 | 61.5 | yes | 44.0 | 44.9 | 57.5 |
| zh-0032 | 6 | 43.4 | 44.6 | 44.0 | 54.7 | yes | 40.7 | 36.8 | 53.7 |
| **zh** (2/15 files) | 18 | 42.0 | 3.2 | 6.0 | 7.7 | 2/2 | 42.3 | 40.9 | 54.3 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 78.3 |
| a_entity_found | 93.8 |
| a_event_concept | 76.6 |
| a_event_found | 96.8 |
| a_granularity | 94.1 |
| b_event_sense | 89.6 |
| c_aspect | 49.5 |
| c_modstr | – |
| c_other_attributes | 36.6 |
| c_polarity | 33.3 |
| c_refer | 28.6 |
| d_core_args_abstract | 38.3 |
| d_core_args_event | 47.6 |
| d_peripheral_entity | 34.6 |
| d_peripheral_event | 32.9 |
| e_core_labels | 74.6 |
| e_peripheral_labels | 72.7 |
| f_name_tokens | 48.0 |
| f_wiki | 0.0 |
| g_reentrancy | 24.1 |
| h_temporal | 34.4 |
| i_modal | 54.3 |
| j_coref_chain | 11.0 |
| j_coref_subset | – |
| k_doc_format | 100.0 |
