# rsi/runs/examples-claude-opus-5-5/test/after-b1

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 51.7 | 56.4 | 53.9 | 62.7 | yes | 44.5 | 47.6 |
| zh-0032 | 6 | 48.2 | 48.3 | 48.2 | 57.6 | yes | 42.8 | 38.8 |
| **zh** (2/15 files) | 18 | 49.9 | 3.8 | 7.0 | 8.0 | 2/2 | 43.6 | 43.2 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 82.3 | 82.3 | 82.3 |
| a_entity_found | 91.4 | 95.3 | 93.3 |
| a_event_concept | 76.2 | 76.2 | 76.2 |
| a_event_found | 95.5 | 98.8 | 97.1 |
| a_granularity | 97.4 | 98.7 | 98.0 |
| b_event_sense | 95.1 | 95.1 | 95.1 |
| c_aspect | 54.1 | 49.3 | 51.6 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 32.0 | 41.0 |
| c_polarity | 33.3 | 50.0 | 40.0 |
| c_refer | 83.3 | 50.0 | 62.5 |
| d_core_args_abstract | 9.6 | 20.4 | 13.1 |
| d_core_args_event | 61.8 | 60.6 | 61.2 |
| d_peripheral_entity | 44.3 | 41.7 | 43.0 |
| d_peripheral_event | 31.5 | 25.0 | 27.9 |
| e_core_labels | 75.6 | 75.6 | 75.6 |
| e_peripheral_labels | 81.0 | 81.0 | 81.0 |
| f_name_tokens | 50.0 | 43.5 | 46.5 |
| f_wiki | – | – | – |
| g_reentrancy | 38.9 | 25.9 | 31.1 |
| h_temporal | 35.6 | 26.6 | 30.4 |
| i_modal | 61.8 | 54.3 | 57.8 |
| j_coref_chain | 9.1 | 2.1 | 3.4 |
| j_coref_subset | – | – | – |
| k_doc_format | 99.6 | 99.6 | 99.6 |
