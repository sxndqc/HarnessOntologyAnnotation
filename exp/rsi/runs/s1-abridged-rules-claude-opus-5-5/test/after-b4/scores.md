# rsi/runs/s1-abridged-rules-claude-opus-5-5/test/after-b4

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 48.8 | 52.0 | 50.3 | 59.6 | yes | 41.4 | 42.6 |
| zh-0032 | 6 | 45.5 | 51.0 | 48.1 | 58.0 | yes | 44.6 | 39.8 |
| **zh** (2/15 files) | 18 | 47.0 | 3.7 | 6.9 | 7.9 | 2/2 | 43.0 | 41.2 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 78.2 | 78.2 | 78.2 |
| a_entity_found | 95.0 | 96.3 | 95.7 |
| a_event_concept | 79.8 | 79.8 | 79.8 |
| a_event_found | 95.5 | 98.8 | 97.1 |
| a_granularity | 97.2 | 97.7 | 97.5 |
| b_event_sense | 90.0 | 90.0 | 90.0 |
| c_aspect | 43.3 | 39.4 | 41.3 |
| c_modstr | – | – | – |
| c_other_attributes | 50.0 | 30.4 | 37.8 |
| c_polarity | 50.0 | 100.0 | 66.7 |
| c_refer | 85.7 | 42.9 | 57.1 |
| d_core_args_abstract | 20.4 | 36.7 | 26.2 |
| d_core_args_event | 59.7 | 57.6 | 58.6 |
| d_peripheral_entity | 38.2 | 35.9 | 37.0 |
| d_peripheral_event | 21.0 | 22.0 | 21.5 |
| e_core_labels | 75.3 | 75.3 | 75.3 |
| e_peripheral_labels | 77.1 | 77.1 | 77.1 |
| f_name_tokens | 58.6 | 45.9 | 51.5 |
| f_wiki | – | – | – |
| g_reentrancy | 33.3 | 37.5 | 35.3 |
| h_temporal | 33.1 | 25.0 | 28.5 |
| i_modal | 56.9 | 49.4 | 52.9 |
| j_coref_chain | 52.2 | 8.8 | 15.1 |
| j_coref_subset | – | 0.0 | 0.0 |
| k_doc_format | 100.0 | 100.0 | 100.0 |
