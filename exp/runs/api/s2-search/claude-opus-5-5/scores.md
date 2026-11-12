# runs/api/s2-search/claude-opus-5-5

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 38.8 | 42.8 | 40.7 | 60.3 | yes | 43.6 | 44.4 |
| zh-0032 | 6 | 42.5 | 43.2 | 42.8 | 54.1 | yes | 39.8 | 36.8 |
| **zh** (2/15 files) | 18 | 40.7 | 3.1 | 5.8 | 7.6 | 2/2 | 41.7 | 40.6 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 79.1 | 79.1 | 79.1 |
| a_entity_found | 90.5 | 97.1 | 93.7 |
| a_event_concept | 78.3 | 78.3 | 78.3 |
| a_event_found | 94.3 | 98.8 | 96.5 |
| a_granularity | 92.2 | 93.1 | 92.7 |
| b_event_sense | 88.1 | 88.1 | 88.1 |
| c_aspect | 50.0 | 44.8 | 47.2 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 36.4 | 44.4 |
| c_polarity | 50.0 | 50.0 | 50.0 |
| c_refer | 100.0 | 42.9 | 60.0 |
| d_core_args_abstract | 37.3 | 63.3 | 46.9 |
| d_core_args_event | 50.6 | 50.6 | 50.6 |
| d_peripheral_entity | 41.5 | 40.6 | 41.0 |
| d_peripheral_event | 27.9 | 21.4 | 24.2 |
| e_core_labels | 75.0 | 75.0 | 75.0 |
| e_peripheral_labels | 78.0 | 78.0 | 78.0 |
| f_name_tokens | 71.4 | 55.6 | 62.5 |
| f_wiki | – | 0.0 | 0.0 |
| g_reentrancy | 44.4 | 27.6 | 34.0 |
| h_temporal | 32.2 | 25.0 | 28.1 |
| i_modal | 56.9 | 55.4 | 56.2 |
| j_coref_chain | 26.8 | 5.0 | 8.4 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
