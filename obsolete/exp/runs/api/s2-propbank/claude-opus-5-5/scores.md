# runs/api/s2-propbank/claude-opus-5-5

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 38.0 | 43.9 | 40.7 | 59.4 | yes | 42.9 | 44.3 |
| zh-0032 | 6 | 42.4 | 44.2 | 43.3 | 54.9 | yes | 39.8 | 36.0 |
| **zh** (2/15 files) | 18 | 40.2 | 3.2 | 5.9 | 7.7 | 2/2 | 41.4 | 40.1 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 75.9 | 75.9 | 75.9 |
| a_entity_found | 91.4 | 98.1 | 94.6 |
| a_event_concept | 74.7 | 74.7 | 74.7 |
| a_event_found | 94.3 | 97.6 | 96.0 |
| a_granularity | 94.9 | 95.8 | 95.4 |
| b_event_sense | 94.9 | 94.9 | 94.9 |
| c_aspect | 52.5 | 46.4 | 49.2 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 34.8 | 43.2 |
| c_polarity | 66.7 | 100.0 | 80.0 |
| c_refer | 85.7 | 31.6 | 46.2 |
| d_core_args_abstract | 12.2 | 20.0 | 15.2 |
| d_core_args_event | 60.2 | 60.2 | 60.2 |
| d_peripheral_entity | 42.9 | 42.9 | 42.9 |
| d_peripheral_event | 33.3 | 29.5 | 31.3 |
| e_core_labels | 77.6 | 77.6 | 77.6 |
| e_peripheral_labels | 77.4 | 77.4 | 77.4 |
| f_name_tokens | 56.5 | 44.8 | 50.0 |
| f_wiki | – | 0.0 | 0.0 |
| g_reentrancy | 38.9 | 23.3 | 29.2 |
| h_temporal | 33.9 | 22.7 | 27.2 |
| i_modal | 59.0 | 49.4 | 53.8 |
| j_coref_chain | 38.6 | 7.3 | 12.3 |
| j_coref_subset | – | 0.0 | 0.0 |
| k_doc_format | 100.0 | 100.0 | 100.0 |
