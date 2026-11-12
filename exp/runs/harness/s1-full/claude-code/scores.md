# runs/harness/s1-full/claude-code

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 43.9 | 45.2 | 44.5 | 58.6 | yes | 39.5 | 41.0 |
| zh-0032 | 6 | 39.3 | 39.3 | 39.3 | 56.1 | yes | 40.2 | 36.2 |
| **zh** (2/15 files) | 18 | 41.5 | 3.0 | 5.7 | 7.5 | 2/2 | 39.9 | 38.6 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 78.0 | 78.0 | 78.0 |
| a_entity_found | 90.1 | 97.1 | 93.5 |
| a_event_concept | 76.2 | 76.2 | 76.2 |
| a_event_found | 90.9 | 100.0 | 95.2 |
| a_granularity | 96.2 | 97.1 | 96.7 |
| b_event_sense | 91.5 | 91.5 | 91.5 |
| c_aspect | 54.2 | 49.2 | 51.6 |
| c_modstr | – | – | – |
| c_other_attributes | 58.3 | 25.0 | 35.0 |
| c_polarity | 50.0 | 50.0 | 50.0 |
| c_refer | 71.4 | 45.5 | 55.6 |
| d_core_args_abstract | 20.8 | 37.0 | 26.7 |
| d_core_args_event | 56.1 | 55.0 | 55.6 |
| d_peripheral_entity | 37.4 | 38.3 | 37.8 |
| d_peripheral_event | 30.8 | 23.6 | 26.7 |
| e_core_labels | 73.7 | 73.7 | 73.7 |
| e_peripheral_labels | 74.5 | 74.5 | 74.5 |
| f_name_tokens | 57.9 | 36.7 | 44.9 |
| f_wiki | – | – | – |
| g_reentrancy | 38.9 | 25.9 | 31.1 |
| h_temporal | 28.8 | 22.1 | 25.0 |
| i_modal | 55.6 | 50.6 | 53.0 |
| j_coref_chain | 11.2 | 2.2 | 3.6 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
