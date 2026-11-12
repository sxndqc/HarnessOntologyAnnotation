# rsi/runs/s1-abridged-rules-claude-opus-5-5/test/after-b1

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 47.6 | 51.8 | 49.6 | 58.7 | yes | 40.8 | 42.7 |
| zh-0032 | 6 | 46.9 | 49.0 | 48.0 | 56.3 | yes | 42.9 | 38.6 |
| **zh** (2/15 files) | 18 | 47.2 | 3.6 | 6.8 | 7.6 | 2/2 | 41.9 | 40.7 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 80.0 | 80.0 | 80.0 |
| a_entity_found | 92.3 | 95.3 | 93.8 |
| a_event_concept | 77.6 | 77.6 | 77.6 |
| a_event_found | 96.6 | 98.8 | 97.7 |
| a_granularity | 97.4 | 98.7 | 98.0 |
| b_event_sense | 88.5 | 88.5 | 88.5 |
| c_aspect | 55.7 | 49.3 | 52.3 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 32.0 | 41.0 |
| c_polarity | 33.3 | 100.0 | 50.0 |
| c_refer | 83.3 | 50.0 | 62.5 |
| d_core_args_abstract | 19.2 | 31.9 | 24.0 |
| d_core_args_event | 55.7 | 56.7 | 56.2 |
| d_peripheral_entity | 39.0 | 43.7 | 41.2 |
| d_peripheral_event | 25.1 | 21.4 | 23.1 |
| e_core_labels | 69.9 | 69.9 | 69.9 |
| e_peripheral_labels | 78.2 | 78.2 | 78.2 |
| f_name_tokens | 47.6 | 43.5 | 45.5 |
| f_wiki | – | – | – |
| g_reentrancy | 44.4 | 30.8 | 36.4 |
| h_temporal | 35.6 | 25.6 | 29.8 |
| i_modal | 59.0 | 49.4 | 53.8 |
| j_coref_chain | 28.8 | 5.6 | 9.3 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
