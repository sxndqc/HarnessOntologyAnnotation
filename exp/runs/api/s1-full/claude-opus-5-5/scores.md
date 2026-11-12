# runs/api/s1-full/claude-opus-5-5

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 44.8 | 45.0 | 44.9 | 63.7 | yes | 41.8 | 41.0 |
| zh-0032 | 6 | 28.0 | 26.0 | 27.0 | 52.4 | yes | 38.7 | 37.3 |
| **zh** (2/15 files) | 18 | 36.2 | 2.5 | 4.7 | 7.5 | 2/2 | 40.2 | 39.1 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 84.7 | 84.7 | 84.7 |
| a_entity_found | 88.3 | 98.0 | 92.9 |
| a_event_concept | 78.8 | 78.8 | 78.8 |
| a_event_found | 90.9 | 100.0 | 95.2 |
| a_granularity | 95.4 | 95.8 | 95.6 |
| b_event_sense | 87.9 | 87.9 | 87.9 |
| c_aspect | 47.5 | 45.2 | 46.3 |
| c_modstr | – | – | – |
| c_other_attributes | 66.7 | 44.4 | 53.3 |
| c_polarity | 33.3 | 33.3 | 33.3 |
| c_refer | 71.4 | 38.5 | 50.0 |
| d_core_args_abstract | 25.5 | 48.1 | 33.3 |
| d_core_args_event | 48.0 | 47.1 | 47.6 |
| d_peripheral_entity | 38.7 | 39.5 | 39.1 |
| d_peripheral_event | 29.5 | 24.1 | 26.5 |
| e_core_labels | 73.2 | 73.2 | 73.2 |
| e_peripheral_labels | 75.5 | 75.5 | 75.5 |
| f_name_tokens | 54.5 | 54.5 | 54.5 |
| f_wiki | – | – | – |
| g_reentrancy | 44.4 | 36.4 | 40.0 |
| h_temporal | 19.5 | 19.5 | 19.5 |
| i_modal | 53.7 | 67.8 | 59.9 |
| j_coref_chain | 21.2 | 4.5 | 7.4 |
| j_coref_subset | – | – | – |
| k_doc_format | 99.5 | 99.5 | 99.5 |
