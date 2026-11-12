# runs/api/s2-gold/claude-opus-5-5

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 41.1 | 44.7 | 42.9 | 61.6 | yes | 44.4 | 46.1 |
| zh-0032 | 6 | 41.8 | 44.0 | 42.9 | 54.0 | yes | 39.8 | 35.5 |
| **zh** (2/15 files) | 18 | 41.5 | 3.2 | 6.0 | 7.7 | 2/2 | 42.1 | 40.8 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 80.2 | 80.2 | 80.2 |
| a_entity_found | 88.7 | 98.5 | 93.4 |
| a_event_concept | 79.5 | 79.5 | 79.5 |
| a_event_found | 94.3 | 98.8 | 96.5 |
| a_granularity | 94.0 | 94.0 | 94.0 |
| b_event_sense | 90.0 | 90.0 | 90.0 |
| c_aspect | 47.5 | 43.9 | 45.7 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 32.0 | 41.0 |
| c_polarity | 33.3 | 50.0 | 40.0 |
| c_refer | 100.0 | 40.0 | 57.1 |
| d_core_args_abstract | 26.9 | 60.4 | 37.2 |
| d_core_args_event | 54.7 | 54.7 | 54.7 |
| d_peripheral_entity | 47.0 | 47.0 | 47.0 |
| d_peripheral_event | 30.1 | 24.7 | 27.1 |
| e_core_labels | 82.2 | 82.2 | 82.2 |
| e_peripheral_labels | 76.9 | 76.9 | 76.9 |
| f_name_tokens | 65.0 | 43.3 | 52.0 |
| f_wiki | – | 0.0 | 0.0 |
| g_reentrancy | 44.4 | 27.6 | 34.0 |
| h_temporal | 35.6 | 24.7 | 29.2 |
| i_modal | 59.0 | 50.6 | 54.5 |
| j_coref_chain | 28.4 | 5.2 | 8.8 |
| j_coref_subset | – | 0.0 | 0.0 |
| k_doc_format | 100.0 | 100.0 | 100.0 |
