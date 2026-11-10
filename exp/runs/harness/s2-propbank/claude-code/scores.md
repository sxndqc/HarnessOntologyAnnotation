# runs/harness/s2-propbank/claude-code

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 53.4 | 57.5 | 55.3 | 63.7 | yes | 48.4 | 49.8 | 58.4 |
| zh-0032 | 6 | 46.0 | 47.7 | 46.8 | 55.4 | yes | 41.4 | 36.9 | 55.7 |
| **zh** (2/15 files) | 18 | 49.5 | 3.8 | 7.0 | 7.9 | 2/2 | 44.9 | 43.4 | 57.1 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 79.5 |
| a_entity_found | 92.6 |
| a_event_concept | 77.6 |
| a_event_found | 96.8 |
| a_granularity | 98.0 |
| b_event_sense | 96.2 |
| c_aspect | 54.2 |
| c_modstr | – |
| c_other_attributes | 50.9 |
| c_polarity | 33.3 |
| c_refer | 37.5 |
| d_core_args_abstract | 24.5 |
| d_core_args_event | 70.3 |
| d_peripheral_entity | 37.8 |
| d_peripheral_event | 31.3 |
| e_core_labels | 81.8 |
| e_peripheral_labels | 74.2 |
| f_name_tokens | 44.6 |
| f_wiki | 0.0 |
| g_reentrancy | 28.6 |
| h_temporal | 33.2 |
| i_modal | 61.1 |
| j_coref_chain | 8.3 |
| j_coref_subset | – |
| k_doc_format | 100.0 |
