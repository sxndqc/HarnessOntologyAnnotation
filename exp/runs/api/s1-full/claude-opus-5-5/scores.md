# runs/api/s1-full/claude-opus-5-5

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 44.8 | 45.0 | 44.9 | 63.7 | yes | 41.8 | 41.0 | 57.0 |
| zh-0032 | 6 | 28.0 | 26.0 | 27.0 | 52.4 | yes | 38.7 | 37.3 | 58.2 |
| **zh** (2/15 files) | 18 | 36.2 | 2.5 | 4.7 | 7.5 | 2/2 | 40.2 | 39.1 | 57.4 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 84.0 |
| a_entity_found | 92.6 |
| a_event_concept | 76.9 |
| a_event_found | 95.0 |
| a_granularity | 95.6 |
| b_event_sense | 89.7 |
| c_aspect | 48.2 |
| c_modstr | – |
| c_other_attributes | 44.7 |
| c_polarity | 33.3 |
| c_refer | 50.0 |
| d_core_args_abstract | 28.3 |
| d_core_args_event | 45.0 |
| d_peripheral_entity | 37.5 |
| d_peripheral_event | 30.7 |
| e_core_labels | 71.7 |
| e_peripheral_labels | 73.0 |
| f_name_tokens | 48.5 |
| f_wiki | – |
| g_reentrancy | 33.6 |
| h_temporal | 19.5 |
| i_modal | 60.1 |
| j_coref_chain | 6.4 |
| j_coref_subset | – |
| k_doc_format | 99.5 |
