# rsi/runs/s3-all-examples-claude-opus-5-5/test/after-b2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 53.1 | 59.6 | 56.2 | 63.8 | yes | 47.9 | 48.7 |
| zh-0032 | 6 | 47.7 | 48.1 | 47.9 | 57.4 | yes | 43.5 | 38.4 |
| **zh** (2/15 files) | 18 | 50.4 | 3.9 | 7.2 | 8.0 | 2/2 | 45.7 | 43.6 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 82.1 | 82.1 | 82.1 |
| a_entity_found | 90.5 | 94.4 | 92.4 |
| a_event_concept | 78.6 | 78.6 | 78.6 |
| a_event_found | 95.5 | 97.7 | 96.6 |
| a_granularity | 96.9 | 98.2 | 97.5 |
| b_event_sense | 95.0 | 95.0 | 95.0 |
| c_aspect | 49.2 | 44.8 | 46.9 |
| c_modstr | – | – | – |
| c_other_attributes | 69.2 | 37.5 | 48.6 |
| c_polarity | 33.3 | 33.3 | 33.3 |
| c_refer | 83.3 | 45.5 | 58.8 |
| d_core_args_abstract | 18.9 | 32.6 | 23.9 |
| d_core_args_event | 65.9 | 63.5 | 64.7 |
| d_peripheral_entity | 52.2 | 46.2 | 49.0 |
| d_peripheral_event | 27.5 | 26.4 | 27.0 |
| e_core_labels | 82.5 | 82.5 | 82.5 |
| e_peripheral_labels | 83.9 | 83.9 | 83.9 |
| f_name_tokens | 52.2 | 50.0 | 51.1 |
| f_wiki | – | – | – |
| g_reentrancy | 44.4 | 28.6 | 34.8 |
| h_temporal | 38.1 | 28.5 | 32.6 |
| i_modal | 55.6 | 47.6 | 51.3 |
| j_coref_chain | 28.5 | 5.3 | 9.0 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
