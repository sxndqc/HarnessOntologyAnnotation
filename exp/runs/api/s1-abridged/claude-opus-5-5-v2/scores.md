# runs/api/s1-abridged/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 48.2 | 54.4 | 51.1 | 59.7 | yes | 43.0 | 44.7 | 52.8 |
| zh-0032 | 6 | 48.9 | 45.2 | 47.0 | 54.4 | yes | 38.9 | 36.4 | 55.7 |
| **zh** (2/15 files) | 18 | 48.6 | 3.6 | 6.7 | 7.5 | 2/2 | 40.9 | 40.5 | 51.9 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 78.2 |
| a_entity_found | 93.9 |
| a_event_concept | 77.1 |
| a_event_found | 97.5 |
| a_granularity | 98.0 |
| b_event_sense | 89.9 |
| c_aspect | 47.4 |
| c_modstr | – |
| c_other_attributes | 35.8 |
| c_polarity | 33.3 |
| c_refer | 25.0 |
| d_core_args_abstract | 35.3 |
| d_core_args_event | 49.7 |
| d_peripheral_entity | 43.8 |
| d_peripheral_event | 28.4 |
| e_core_labels | 69.7 |
| e_peripheral_labels | 77.4 |
| f_name_tokens | 41.2 |
| f_wiki | 0.0 |
| g_reentrancy | 29.3 |
| h_temporal | 33.0 |
| i_modal | 60.6 |
| j_coref_chain | 2.6 |
| j_coref_subset | 0.0 |
| k_doc_format | 99.4 |
