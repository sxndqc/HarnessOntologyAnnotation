# runs/harness/s2-propbank/claude-code

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 53.4 | 57.5 | 55.3 | 63.7 | yes | 48.4 | 49.8 |
| zh-0032 | 6 | 46.0 | 47.7 | 46.8 | 55.4 | yes | 41.4 | 36.9 |
| **zh** (2/15 files) | 18 | 49.5 | 3.8 | 7.0 | 7.9 | 2/2 | 44.9 | 43.4 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 79.9 | 79.9 | 79.9 |
| a_entity_found | 89.6 | 96.6 | 93.0 |
| a_event_concept | 79.5 | 79.5 | 79.5 |
| a_event_found | 94.3 | 100.0 | 97.1 |
| a_granularity | 97.3 | 98.6 | 97.9 |
| b_event_sense | 96.7 | 96.7 | 96.7 |
| c_aspect | 55.7 | 49.3 | 52.3 |
| c_modstr | – | – | – |
| c_other_attributes | 69.2 | 40.9 | 51.4 |
| c_polarity | 33.3 | 100.0 | 50.0 |
| c_refer | 100.0 | 50.0 | 66.7 |
| d_core_args_abstract | 21.3 | 38.3 | 27.4 |
| d_core_args_event | 69.7 | 67.1 | 68.4 |
| d_peripheral_entity | 38.4 | 38.4 | 38.4 |
| d_peripheral_event | 30.1 | 25.6 | 27.7 |
| e_core_labels | 81.9 | 81.9 | 81.9 |
| e_peripheral_labels | 75.5 | 75.5 | 75.5 |
| f_name_tokens | 57.1 | 46.2 | 51.1 |
| f_wiki | – | 0.0 | 0.0 |
| g_reentrancy | 44.4 | 25.8 | 32.7 |
| h_temporal | 36.4 | 27.9 | 31.6 |
| i_modal | 61.8 | 55.6 | 58.6 |
| j_coref_chain | 27.3 | 5.1 | 8.6 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
