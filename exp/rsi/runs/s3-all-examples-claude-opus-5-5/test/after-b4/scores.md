# rsi/runs/s3-all-examples-claude-opus-5-5/test/after-b4

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 51.8 | 57.2 | 54.4 | 62.5 | yes | 46.1 | 47.4 |
| zh-0032 | 6 | 47.8 | 53.3 | 50.4 | 61.3 | yes | 46.8 | 42.7 |
| **zh** (2/15 files) | 18 | 49.7 | 4.0 | 7.4 | 8.4 | 2/2 | 46.4 | 45.1 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 80.5 | 80.5 | 80.5 |
| a_entity_found | 94.6 | 95.9 | 95.2 |
| a_event_concept | 80.2 | 80.2 | 80.2 |
| a_event_found | 97.7 | 100.0 | 98.9 |
| a_granularity | 96.8 | 97.7 | 97.2 |
| b_event_sense | 95.1 | 95.1 | 95.1 |
| c_aspect | 48.3 | 42.6 | 45.3 |
| c_modstr | – | – | – |
| c_other_attributes | 64.3 | 36.0 | 46.2 |
| c_polarity | 50.0 | 100.0 | 66.7 |
| c_refer | 83.3 | 50.0 | 62.5 |
| d_core_args_abstract | 29.2 | 44.9 | 35.4 |
| d_core_args_event | 66.8 | 65.6 | 66.2 |
| d_peripheral_entity | 48.9 | 45.1 | 46.9 |
| d_peripheral_event | 23.2 | 26.7 | 24.8 |
| e_core_labels | 85.7 | 85.7 | 85.7 |
| e_peripheral_labels | 82.4 | 82.4 | 82.4 |
| f_name_tokens | 57.1 | 47.1 | 51.6 |
| f_wiki | – | – | – |
| g_reentrancy | 44.4 | 32.0 | 37.2 |
| h_temporal | 33.1 | 24.7 | 28.3 |
| i_modal | 71.5 | 59.9 | 65.2 |
| j_coref_chain | 31.8 | 5.0 | 8.6 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
