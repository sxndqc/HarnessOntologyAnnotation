# rsi/runs/examples-claude-opus-5-5/test/v0

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 48.9 | 52.4 | 50.6 | 58.4 | yes | 40.7 | 43.0 |
| zh-0032 | 6 | 46.8 | 47.5 | 47.1 | 56.4 | yes | 42.0 | 36.3 |
| **zh** (2/15 files) | 18 | 47.8 | 3.6 | 6.7 | 7.6 | 2/2 | 41.3 | 39.6 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 77.1 | 77.1 | 77.1 |
| a_entity_found | 90.5 | 97.1 | 93.7 |
| a_event_concept | 79.5 | 79.5 | 79.5 |
| a_event_found | 94.3 | 100.0 | 97.1 |
| a_granularity | 96.7 | 96.7 | 96.7 |
| b_event_sense | 91.9 | 91.9 | 91.9 |
| c_aspect | 48.3 | 43.3 | 45.7 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 30.8 | 40.0 |
| c_polarity | 50.0 | 50.0 | 50.0 |
| c_refer | 85.7 | 50.0 | 63.2 |
| d_core_args_abstract | 13.0 | 29.2 | 17.9 |
| d_core_args_event | 60.8 | 58.6 | 59.7 |
| d_peripheral_entity | 40.6 | 38.1 | 39.3 |
| d_peripheral_event | 34.1 | 30.1 | 32.0 |
| e_core_labels | 82.4 | 82.4 | 82.4 |
| e_peripheral_labels | 78.8 | 78.8 | 78.8 |
| f_name_tokens | 57.1 | 41.4 | 48.0 |
| f_wiki | – | 0.0 | 0.0 |
| g_reentrancy | 38.9 | 28.0 | 32.6 |
| h_temporal | 30.5 | 26.5 | 28.3 |
| i_modal | 54.2 | 52.7 | 53.4 |
| j_coref_chain | 27.0 | 5.0 | 8.4 |
| j_coref_subset | – | – | – |
| k_doc_format | 99.5 | 99.5 | 99.5 |
