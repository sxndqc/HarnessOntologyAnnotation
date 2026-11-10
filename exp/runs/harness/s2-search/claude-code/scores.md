# runs/harness/s2-search/claude-code

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 51.6 | 55.7 | 53.6 | 62.2 | yes | 44.3 | 46.0 | 54.4 |
| zh-0032 | 6 | 44.0 | 46.9 | 45.4 | 54.6 | no (2) | 40.3 | 36.6 | 54.1 |
| **zh** (2/15 files) | 18 | 47.6 | 3.7 | 6.9 | 7.8 | 1/2 | 42.3 | 41.3 | 53.1 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 78.6 |
| a_entity_found | 93.6 |
| a_event_concept | 78.2 |
| a_event_found | 96.1 |
| a_granularity | 97.9 |
| b_event_sense | 92.6 |
| c_aspect | 52.1 |
| c_modstr | – |
| c_other_attributes | 33.1 |
| c_polarity | 33.3 |
| c_refer | 33.3 |
| d_core_args_abstract | 22.9 |
| d_core_args_event | 55.6 |
| d_peripheral_entity | 42.4 |
| d_peripheral_event | 31.3 |
| e_core_labels | 72.0 |
| e_peripheral_labels | 74.8 |
| f_name_tokens | 51.2 |
| f_wiki | 0.0 |
| g_reentrancy | 33.0 |
| h_temporal | 36.5 |
| i_modal | 57.6 |
| j_coref_chain | 9.3 |
| j_coref_subset | 0.0 |
| k_doc_format | 99.6 |
