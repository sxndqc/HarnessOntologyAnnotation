# rsi/runs/rules-claude-opus-5-5/test/after-b4

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 53.5 | 56.6 | 55.0 | 64.2 | yes | 49.5 | 49.1 |
| zh-0032 | 6 | 49.3 | 54.3 | 51.7 | 61.5 | yes | 48.4 | 44.9 |
| **zh** (2/15 files) | 18 | 51.2 | 4.0 | 7.5 | 8.4 | 2/2 | 48.9 | 47.0 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 78.7 | 78.7 | 78.7 |
| a_entity_found | 95.0 | 96.3 | 95.7 |
| a_event_concept | 81.7 | 81.7 | 81.7 |
| a_event_found | 93.2 | 100.0 | 96.5 |
| a_granularity | 97.3 | 98.2 | 97.7 |
| b_event_sense | 95.0 | 95.0 | 95.0 |
| c_aspect | 51.7 | 47.0 | 49.2 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 33.3 | 42.1 |
| c_polarity | 50.0 | 100.0 | 66.7 |
| c_refer | 100.0 | 50.0 | 66.7 |
| d_core_args_abstract | 26.0 | 36.8 | 30.5 |
| d_core_args_event | 67.8 | 69.1 | 68.4 |
| d_peripheral_entity | 51.1 | 49.0 | 50.0 |
| d_peripheral_event | 31.9 | 28.2 | 29.9 |
| e_core_labels | 84.5 | 84.5 | 84.5 |
| e_peripheral_labels | 88.5 | 88.5 | 88.5 |
| f_name_tokens | 62.1 | 51.4 | 56.2 |
| f_wiki | – | – | – |
| g_reentrancy | 44.4 | 34.8 | 39.0 |
| h_temporal | 23.7 | 18.2 | 20.6 |
| i_modal | 71.5 | 62.0 | 66.5 |
| j_coref_chain | 29.1 | 6.7 | 10.9 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
