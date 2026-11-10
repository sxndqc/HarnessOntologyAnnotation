# runs/harness/s1-abridged/claude-code

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 51.4 | 56.1 | 53.7 | 61.9 | yes | 45.9 | 47.2 | 58.2 |
| zh-0032 | 6 | 43.7 | 46.7 | 45.1 | 54.1 | yes | 40.5 | 35.3 | 53.5 |
| **zh** (2/15 files) | 18 | 47.3 | 3.7 | 6.9 | 7.7 | 2/2 | 43.2 | 41.2 | 55.9 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 78.8 |
| a_entity_found | 92.8 |
| a_event_concept | 79.1 |
| a_event_found | 96.8 |
| a_granularity | 98.0 |
| b_event_sense | 90.0 |
| c_aspect | 46.7 |
| c_modstr | – |
| c_other_attributes | 35.1 |
| c_polarity | 33.3 |
| c_refer | 33.3 |
| d_core_args_abstract | 38.8 |
| d_core_args_event | 55.9 |
| d_peripheral_entity | 40.7 |
| d_peripheral_event | 31.3 |
| e_core_labels | 79.3 |
| e_peripheral_labels | 76.6 |
| f_name_tokens | 44.6 |
| f_wiki | 0.0 |
| g_reentrancy | 35.1 |
| h_temporal | 32.3 |
| i_modal | 59.2 |
| j_coref_chain | 7.8 |
| j_coref_subset | – |
| k_doc_format | 99.3 |
