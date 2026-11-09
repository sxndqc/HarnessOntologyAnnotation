# runs/api/s2-gold/claude-opus-5-5

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 41.1 | 44.7 | 42.9 | 61.6 | yes | 44.4 | 46.1 | 54.6 |
| zh-0032 | 6 | 41.8 | 44.0 | 42.9 | 54.0 | yes | 39.8 | 35.5 | 53.2 |
| **zh** (2/15 files) | 18 | 41.5 | 3.2 | 6.0 | 7.7 | 2/2 | 42.1 | 40.8 | 52.8 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 80.1 |
| a_entity_found | 92.9 |
| a_event_concept | 77.6 |
| a_event_found | 96.2 |
| a_granularity | 94.0 |
| b_event_sense | 91.3 |
| c_aspect | 47.0 |
| c_modstr | – |
| c_other_attributes | 35.1 |
| c_polarity | 33.3 |
| c_refer | 30.0 |
| d_core_args_abstract | 30.6 |
| d_core_args_event | 53.7 |
| d_peripheral_entity | 44.3 |
| d_peripheral_event | 32.1 |
| e_core_labels | 81.3 |
| e_peripheral_labels | 72.3 |
| f_name_tokens | 48.0 |
| f_wiki | 0.0 |
| g_reentrancy | 29.7 |
| h_temporal | 31.8 |
| i_modal | 57.1 |
| j_coref_chain | 8.6 |
| j_coref_subset | 0.0 |
| k_doc_format | 100.0 |
