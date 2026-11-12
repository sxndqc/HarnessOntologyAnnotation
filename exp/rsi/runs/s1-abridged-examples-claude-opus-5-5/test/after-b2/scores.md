# rsi/runs/s1-abridged-examples-claude-opus-5-5/test/after-b2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 49.9 | 55.3 | 52.4 | 61.0 | yes | 43.3 | 44.9 |
| zh-0032 | 6 | 49.2 | 48.1 | 48.6 | 57.1 | yes | 41.6 | 39.8 |
| **zh** (2/15 files) | 18 | 49.5 | 3.7 | 6.9 | 7.8 | 2/2 | 42.5 | 42.3 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 78.6 | 78.6 | 78.6 |
| a_entity_found | 92.8 | 93.6 | 93.2 |
| a_event_concept | 80.7 | 80.7 | 80.7 |
| a_event_found | 94.3 | 97.6 | 96.0 |
| a_granularity | 97.3 | 98.2 | 97.8 |
| b_event_sense | 90.0 | 90.0 | 90.0 |
| c_aspect | 46.7 | 43.1 | 44.8 |
| c_modstr | – | – | – |
| c_other_attributes | 64.3 | 37.5 | 47.4 |
| c_polarity | 50.0 | 100.0 | 66.7 |
| c_refer | 100.0 | 66.7 | 80.0 |
| d_core_args_abstract | 18.0 | 26.3 | 21.4 |
| d_core_args_event | 56.0 | 57.1 | 56.5 |
| d_peripheral_entity | 45.9 | 43.1 | 44.4 |
| d_peripheral_event | 27.7 | 22.0 | 24.5 |
| e_core_labels | 75.6 | 75.6 | 75.6 |
| e_peripheral_labels | 78.6 | 78.6 | 78.6 |
| f_name_tokens | 41.7 | 40.0 | 40.8 |
| f_wiki | – | – | – |
| g_reentrancy | 44.4 | 38.1 | 41.0 |
| h_temporal | 36.4 | 28.7 | 32.1 |
| i_modal | 57.6 | 52.5 | 55.0 |
| j_coref_chain | 4.5 | 1.5 | 2.2 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
