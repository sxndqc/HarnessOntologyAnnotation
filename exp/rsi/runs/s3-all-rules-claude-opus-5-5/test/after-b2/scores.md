# rsi/runs/rules-claude-opus-5-5/test/after-b2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 48.4 | 52.2 | 50.2 | 59.6 | yes | 40.1 | 42.8 |
| zh-0032 | 6 | 49.1 | 49.0 | 49.1 | 57.0 | yes | 41.2 | 39.0 |
| **zh** (2/15 files) | 18 | 48.8 | 3.7 | 6.8 | 7.7 | 2/2 | 40.7 | 40.9 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 76.7 | 76.7 | 76.7 |
| a_entity_found | 92.8 | 95.4 | 94.1 |
| a_event_concept | 77.1 | 77.1 | 77.1 |
| a_event_found | 94.3 | 98.8 | 96.5 |
| a_granularity | 97.3 | 98.6 | 98.0 |
| b_event_sense | 96.7 | 96.7 | 96.7 |
| c_aspect | 51.7 | 46.3 | 48.8 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 33.3 | 42.1 |
| c_polarity | 50.0 | 100.0 | 66.7 |
| c_refer | 83.3 | 38.5 | 52.6 |
| d_core_args_abstract | 13.0 | 19.4 | 15.6 |
| d_core_args_event | 64.0 | 61.7 | 62.8 |
| d_peripheral_entity | 40.7 | 39.9 | 40.3 |
| d_peripheral_event | 32.2 | 28.5 | 30.3 |
| e_core_labels | 78.5 | 78.5 | 78.5 |
| e_peripheral_labels | 79.2 | 79.2 | 79.2 |
| f_name_tokens | 36.0 | 39.1 | 37.5 |
| f_wiki | – | – | – |
| g_reentrancy | 16.7 | 18.8 | 17.6 |
| h_temporal | 35.6 | 27.3 | 30.9 |
| i_modal | 61.1 | 54.3 | 57.5 |
| j_coref_chain | 34.8 | 7.4 | 12.2 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
