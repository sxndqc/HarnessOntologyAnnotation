# rsi/runs/rules-claude-opus-5-5/test/after-b3

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 51.6 | 56.4 | 53.9 | 65.3 | yes | 48.5 | 48.1 |
| zh-0032 | 6 | 51.5 | 55.8 | 53.6 | 64.0 | yes | 48.8 | 46.0 |
| **zh** (2/15 files) | 18 | 51.6 | 4.1 | 7.5 | 8.7 | 2/2 | 48.7 | 47.1 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 83.3 | 83.3 | 83.3 |
| a_entity_found | 94.1 | 94.1 | 94.1 |
| a_event_concept | 77.6 | 77.6 | 77.6 |
| a_event_found | 96.6 | 98.8 | 97.7 |
| a_granularity | 97.3 | 98.2 | 97.8 |
| b_event_sense | 94.9 | 94.9 | 94.9 |
| c_aspect | 50.8 | 45.6 | 48.1 |
| c_modstr | – | – | – |
| c_other_attributes | 66.7 | 36.4 | 47.1 |
| c_polarity | 66.7 | 100.0 | 80.0 |
| c_refer | 100.0 | 50.0 | 66.7 |
| d_core_args_abstract | 30.7 | 48.6 | 37.6 |
| d_core_args_event | 65.3 | 65.3 | 65.3 |
| d_peripheral_entity | 53.3 | 48.0 | 50.5 |
| d_peripheral_event | 38.8 | 35.7 | 37.2 |
| e_core_labels | 83.3 | 83.3 | 83.3 |
| e_peripheral_labels | 86.7 | 86.7 | 86.7 |
| f_name_tokens | 55.2 | 51.6 | 53.3 |
| f_wiki | – | – | – |
| g_reentrancy | 33.3 | 46.2 | 38.7 |
| h_temporal | 28.8 | 22.1 | 25.0 |
| i_modal | 69.0 | 59.1 | 63.7 |
| j_coref_chain | 36.0 | 7.5 | 12.4 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
