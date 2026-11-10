# runs/api/s2-search/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 51.7 | 56.4 | 53.9 | 63.6 | yes | 47.5 | 48.1 | 58.7 |
| zh-0032 | 6 | 47.0 | 45.7 | 46.4 | 55.0 | no (20) | 40.7 | 37.2 | 56.1 |
| **zh** (2/15 files) | 18 | 49.4 | 3.7 | 6.8 | 7.8 | 1/2 | 44.1 | 42.7 | 56.2 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 78.8 |
| a_entity_found | 93.4 |
| a_event_concept | 78.6 |
| a_event_found | 96.1 |
| a_granularity | 97.3 |
| b_event_sense | 89.7 |
| c_aspect | 50.3 |
| c_modstr | – |
| c_other_attributes | 33.9 |
| c_polarity | 33.3 |
| c_refer | 35.3 |
| d_core_args_abstract | 40.2 |
| d_core_args_event | 55.2 |
| d_peripheral_entity | 39.3 |
| d_peripheral_event | 35.8 |
| e_core_labels | 78.8 |
| e_peripheral_labels | 78.2 |
| f_name_tokens | 42.8 |
| f_wiki | – |
| g_reentrancy | 33.9 |
| h_temporal | 36.1 |
| i_modal | 55.9 |
| j_coref_chain | 9.3 |
| j_coref_subset | 0.0 |
| k_doc_format | 99.6 |
