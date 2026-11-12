# rsi/runs/s3-all-examples-claude-opus-5-5/test/after-b1

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 50.6 | 57.2 | 53.7 | 61.8 | yes | 45.9 | 46.7 |
| zh-0032 | 6 | 47.9 | 48.4 | 48.2 | 56.0 | yes | 40.9 | 37.2 |
| **zh** (2/15 files) | 18 | 49.2 | 3.8 | 7.1 | 7.8 | 2/2 | 43.4 | 42.0 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 80.4 | 80.4 | 80.4 |
| a_entity_found | 91.9 | 94.4 | 93.2 |
| a_event_concept | 80.0 | 80.0 | 80.0 |
| a_event_found | 96.6 | 98.8 | 97.7 |
| a_granularity | 97.4 | 98.7 | 98.0 |
| b_event_sense | 91.9 | 91.9 | 91.9 |
| c_aspect | 45.9 | 40.0 | 42.7 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 32.0 | 41.0 |
| c_polarity | 33.3 | 50.0 | 40.0 |
| c_refer | 83.3 | 55.6 | 66.7 |
| d_core_args_abstract | 19.2 | 31.9 | 24.0 |
| d_core_args_event | 64.9 | 62.6 | 63.7 |
| d_peripheral_entity | 40.4 | 43.2 | 41.8 |
| d_peripheral_event | 26.8 | 23.7 | 25.2 |
| e_core_labels | 81.0 | 81.0 | 81.0 |
| e_peripheral_labels | 81.5 | 81.5 | 81.5 |
| f_name_tokens | 47.6 | 43.5 | 45.5 |
| f_wiki | – | – | – |
| g_reentrancy | 38.9 | 25.9 | 31.1 |
| h_temporal | 30.5 | 22.8 | 26.1 |
| i_modal | 61.1 | 53.7 | 57.1 |
| j_coref_chain | 27.7 | 5.1 | 8.6 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
