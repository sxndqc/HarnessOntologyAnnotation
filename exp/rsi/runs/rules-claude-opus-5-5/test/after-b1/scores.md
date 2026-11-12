# rsi/runs/rules-claude-opus-5-5/test/after-b1

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 53.5 | 59.4 | 56.3 | 64.0 | yes | 47.5 | 48.5 |
| zh-0032 | 6 | 46.0 | 46.7 | 46.3 | 56.2 | yes | 39.0 | 35.1 |
| **zh** (2/15 files) | 18 | 49.7 | 3.8 | 7.1 | 8.0 | 2/2 | 43.3 | 41.8 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 80.0 | 80.0 | 80.0 |
| a_entity_found | 92.3 | 93.6 | 93.0 |
| a_event_concept | 84.3 | 84.3 | 84.3 |
| a_event_found | 94.3 | 97.6 | 96.0 |
| a_granularity | 97.3 | 98.7 | 98.0 |
| b_event_sense | 95.1 | 95.1 | 95.1 |
| c_aspect | 50.0 | 42.9 | 46.2 |
| c_modstr | – | – | – |
| c_other_attributes | 64.3 | 36.0 | 46.2 |
| c_polarity | 50.0 | 100.0 | 66.7 |
| c_refer | 100.0 | 50.0 | 66.7 |
| d_core_args_abstract | 27.2 | 36.9 | 31.3 |
| d_core_args_event | 64.3 | 63.1 | 63.7 |
| d_peripheral_entity | 45.7 | 50.0 | 47.8 |
| d_peripheral_event | 21.7 | 19.2 | 20.4 |
| e_core_labels | 84.1 | 84.1 | 84.1 |
| e_peripheral_labels | 79.6 | 79.6 | 79.6 |
| f_name_tokens | 39.1 | 40.9 | 40.0 |
| f_wiki | – | – | – |
| g_reentrancy | 22.2 | 17.4 | 19.5 |
| h_temporal | 32.2 | 25.0 | 28.1 |
| i_modal | 61.1 | 50.0 | 55.0 |
| j_coref_chain | 27.3 | 6.8 | 10.9 |
| j_coref_subset | – | – | – |
| k_doc_format | 98.7 | 98.7 | 98.7 |
