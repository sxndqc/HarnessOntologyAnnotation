# runs/api/s2-gold/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 52.1 | 56.8 | 54.4 | 61.4 | yes | 45.0 | 46.5 | 57.9 |
| zh-0032 | 6 | 44.8 | 45.3 | 45.1 | 53.3 | yes | 40.3 | 34.6 | 57.6 |
| **zh** (2/15 files) | 18 | 48.4 | 3.7 | 6.8 | 7.5 | 2/2 | 42.7 | 40.5 | 58.0 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 80.4 |
| a_entity_found | 93.4 |
| a_event_concept | 76.0 |
| a_event_found | 97.5 |
| a_granularity | 98.0 |
| b_event_sense | 88.5 |
| c_aspect | 44.8 |
| c_modstr | – |
| c_other_attributes | 37.5 |
| c_polarity | 33.3 |
| c_refer | 70.6 |
| d_core_args_abstract | 19.3 |
| d_core_args_event | 52.6 |
| d_peripheral_entity | 41.5 |
| d_peripheral_event | 34.1 |
| e_core_labels | 67.1 |
| e_peripheral_labels | 80.6 |
| f_name_tokens | 48.0 |
| f_wiki | – |
| g_reentrancy | 20.7 |
| h_temporal | 29.4 |
| i_modal | 55.6 |
| j_coref_chain | 8.9 |
| j_coref_subset | – |
| k_doc_format | 99.3 |
