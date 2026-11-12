# runs/harness/s2-search/claude-code

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 51.6 | 55.7 | 53.6 | 62.2 | yes | 44.3 | 46.0 |
| zh-0032 | 6 | 44.0 | 46.9 | 45.4 | 54.2 | no (2) | 40.3 | 36.6 |
| **zh** (2/15 files) | 18 | 47.6 | 3.7 | 6.9 | 7.7 | 1/2 | 42.3 | 41.3 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 79.2 | 79.2 | 79.2 |
| a_entity_found | 91.0 | 97.1 | 94.0 |
| a_event_concept | 80.5 | 80.5 | 80.5 |
| a_event_found | 93.2 | 100.0 | 96.5 |
| a_granularity | 97.2 | 98.6 | 97.9 |
| b_event_sense | 91.8 | 91.8 | 91.8 |
| c_aspect | 54.1 | 47.1 | 50.4 |
| c_modstr | – | – | – |
| c_other_attributes | 53.8 | 30.4 | 38.9 |
| c_polarity | 33.3 | 100.0 | 50.0 |
| c_refer | 83.3 | 45.5 | 58.8 |
| d_core_args_abstract | 19.6 | 33.3 | 24.7 |
| d_core_args_event | 57.5 | 56.5 | 57.0 |
| d_peripheral_entity | 44.9 | 42.2 | 43.5 |
| d_peripheral_event | 30.1 | 25.6 | 27.7 |
| e_core_labels | 73.1 | 73.1 | 73.1 |
| e_peripheral_labels | 76.4 | 76.4 | 76.4 |
| f_name_tokens | 61.9 | 50.0 | 55.3 |
| f_wiki | – | 0.0 | 0.0 |
| g_reentrancy | 50.0 | 28.1 | 36.0 |
| h_temporal | 40.7 | 28.9 | 33.8 |
| i_modal | 59.0 | 52.5 | 55.6 |
| j_coref_chain | 31.8 | 5.5 | 9.3 |
| j_coref_subset | – | 0.0 | 0.0 |
| k_doc_format | 99.6 | 99.6 | 99.6 |
