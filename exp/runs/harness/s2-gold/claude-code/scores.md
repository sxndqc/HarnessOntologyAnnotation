# runs/harness/s2-gold/claude-code

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0032 | 6 | 46.2 | 48.3 | 47.2 | 55.7 | yes | 42.7 | 37.1 | 57.1 |
| **zh** (1/1 files) | 6 | 46.2 | 48.3 | 47.2 | 55.7 | 1/1 | 42.7 | 37.1 | 57.1 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 81.2 |
| a_entity_found | 91.4 |
| a_event_concept | 91.7 |
| a_event_found | 99.0 |
| a_granularity | 96.0 |
| b_event_sense | 88.4 |
| c_aspect | 37.8 |
| c_modstr | – |
| c_other_attributes | 44.4 |
| c_polarity | 66.7 |
| c_refer | 0.0 |
| d_core_args_abstract | 20.0 |
| d_core_args_event | 60.4 |
| d_peripheral_entity | 33.3 |
| d_peripheral_event | 17.2 |
| e_core_labels | 90.5 |
| e_peripheral_labels | 68.4 |
| f_name_tokens | 60.6 |
| f_wiki | – |
| g_reentrancy | 46.7 |
| h_temporal | 12.9 |
| i_modal | 41.1 |
| j_coref_chain | 9.3 |
| j_coref_subset | – |
| k_doc_format | 99.3 |
