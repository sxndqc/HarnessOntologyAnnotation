# runs/api/s2-propbank/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 48.9 | 53.5 | 51.1 | 59.5 | yes | 44.0 | 45.7 | 55.9 |
| zh-0032 | 6 | 43.5 | 47.5 | 45.4 | 55.5 | no (1) | 39.1 | 34.7 | 50.6 |
| **zh** (2/15 files) | 18 | 46.0 | 3.6 | 6.8 | 7.7 | 1/2 | 41.5 | 40.2 | 53.2 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 77.3 |
| a_entity_found | 92.9 |
| a_event_concept | 79.6 |
| a_event_found | 95.3 |
| a_granularity | 98.0 |
| b_event_sense | 98.8 |
| c_aspect | 45.9 |
| c_modstr | – |
| c_other_attributes | 36.6 |
| c_polarity | 33.3 |
| c_refer | 26.1 |
| d_core_args_abstract | 24.6 |
| d_core_args_event | 66.7 |
| d_peripheral_entity | 44.6 |
| d_peripheral_event | 33.4 |
| e_core_labels | 86.6 |
| e_peripheral_labels | 78.1 |
| f_name_tokens | 40.6 |
| f_wiki | 0.0 |
| g_reentrancy | 26.1 |
| h_temporal | 27.2 |
| i_modal | 56.9 |
| j_coref_chain | 9.9 |
| j_coref_subset | 0.0 |
| k_doc_format | 99.3 |
