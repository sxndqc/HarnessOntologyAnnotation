# rsi/runs/s3-all-examples-claude-opus-5-5/test/after-b3

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 51.0 | 56.4 | 53.5 | 62.0 | yes | 43.9 | 44.3 |
| zh-0032 | 6 | 49.5 | 50.0 | 49.8 | 57.1 | yes | 41.5 | 37.9 |
| **zh** (2/15 files) | 18 | 50.2 | 3.8 | 7.1 | 7.9 | 2/2 | 42.7 | 41.1 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 81.3 | 81.3 | 81.3 |
| a_entity_found | 91.4 | 94.9 | 93.1 |
| a_event_concept | 78.3 | 78.3 | 78.3 |
| a_event_found | 94.3 | 100.0 | 97.1 |
| a_granularity | 98.2 | 99.1 | 98.6 |
| b_event_sense | 96.6 | 96.6 | 96.6 |
| c_aspect | 46.7 | 41.8 | 44.1 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 32.0 | 41.0 |
| c_polarity | 50.0 | 100.0 | 66.7 |
| c_refer | 66.7 | 50.0 | 57.1 |
| d_core_args_abstract | 14.4 | 21.5 | 17.2 |
| d_core_args_event | 59.9 | 59.9 | 59.9 |
| d_peripheral_entity | 47.8 | 48.9 | 48.4 |
| d_peripheral_event | 27.5 | 25.3 | 26.4 |
| e_core_labels | 81.1 | 81.1 | 81.1 |
| e_peripheral_labels | 81.5 | 81.5 | 81.5 |
| f_name_tokens | 45.5 | 41.7 | 43.5 |
| f_wiki | – | – | – |
| g_reentrancy | 38.9 | 21.2 | 27.5 |
| h_temporal | 34.7 | 26.3 | 29.9 |
| i_modal | 56.9 | 49.4 | 52.9 |
| j_coref_chain | 21.2 | 4.5 | 7.4 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
