# rsi/runs/s1-abridged-examples-claude-opus-5-5/test/after-b3

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 47.6 | 51.1 | 49.3 | 58.8 | yes | 41.3 | 43.0 |
| zh-0032 | 6 | 48.5 | 51.9 | 50.1 | 58.7 | yes | 43.8 | 42.9 |
| **zh** (2/15 files) | 18 | 48.0 | 3.7 | 6.9 | 7.8 | 2/2 | 42.5 | 43.0 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 79.4 | 79.4 | 79.4 |
| a_entity_found | 94.1 | 93.7 | 93.9 |
| a_event_concept | 78.6 | 78.6 | 78.6 |
| a_event_found | 95.5 | 98.8 | 97.1 |
| a_granularity | 97.3 | 98.2 | 97.7 |
| b_event_sense | 90.0 | 90.0 | 90.0 |
| c_aspect | 49.2 | 45.5 | 47.2 |
| c_modstr | – | – | – |
| c_other_attributes | 53.8 | 29.2 | 37.8 |
| c_polarity | 33.3 | 50.0 | 40.0 |
| c_refer | 83.3 | 62.5 | 71.4 |
| d_core_args_abstract | 24.1 | 38.2 | 29.6 |
| d_core_args_event | 59.1 | 60.3 | 59.7 |
| d_peripheral_entity | 47.5 | 42.8 | 45.0 |
| d_peripheral_event | 22.6 | 20.0 | 21.2 |
| e_core_labels | 79.7 | 79.7 | 79.7 |
| e_peripheral_labels | 77.8 | 77.8 | 77.8 |
| f_name_tokens | 51.9 | 50.0 | 50.9 |
| f_wiki | – | – | – |
| g_reentrancy | 33.3 | 30.0 | 31.6 |
| h_temporal | 28.8 | 22.7 | 25.4 |
| i_modal | 66.9 | 60.2 | 63.4 |
| j_coref_chain | 50.6 | 16.4 | 24.7 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
