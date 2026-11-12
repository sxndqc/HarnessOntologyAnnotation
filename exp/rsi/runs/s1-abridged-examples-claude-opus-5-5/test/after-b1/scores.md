# rsi/runs/s1-abridged-examples-claude-opus-5-5/test/after-b1

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 47.5 | 52.6 | 49.9 | 60.0 | yes | 41.1 | 43.5 |
| zh-0032 | 6 | 46.0 | 47.3 | 46.7 | 55.3 | yes | 41.1 | 37.8 |
| **zh** (2/15 files) | 18 | 46.8 | 3.6 | 6.7 | 7.7 | 2/2 | 41.1 | 40.7 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 79.9 | 79.9 | 79.9 |
| a_entity_found | 91.9 | 95.8 | 93.8 |
| a_event_concept | 77.6 | 77.6 | 77.6 |
| a_event_found | 96.6 | 96.6 | 96.6 |
| a_granularity | 97.3 | 98.6 | 98.0 |
| b_event_sense | 90.0 | 90.0 | 90.0 |
| c_aspect | 49.2 | 44.8 | 46.9 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 34.8 | 43.2 |
| c_polarity | 33.3 | 33.3 | 33.3 |
| c_refer | 100.0 | 50.0 | 66.7 |
| d_core_args_abstract | 14.2 | 23.6 | 17.7 |
| d_core_args_event | 53.8 | 55.9 | 54.8 |
| d_peripheral_entity | 44.2 | 44.2 | 44.2 |
| d_peripheral_event | 25.5 | 23.5 | 24.4 |
| e_core_labels | 69.6 | 69.6 | 69.6 |
| e_peripheral_labels | 80.4 | 80.4 | 80.4 |
| f_name_tokens | 57.1 | 48.0 | 52.2 |
| f_wiki | – | – | – |
| g_reentrancy | 44.4 | 27.6 | 34.0 |
| h_temporal | 35.6 | 26.2 | 30.2 |
| i_modal | 59.0 | 49.4 | 53.8 |
| j_coref_chain | 29.4 | 6.5 | 10.6 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
