# runs/harness/s1-abridged/claude-code

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 51.4 | 56.1 | 53.7 | 61.9 | yes | 45.9 | 47.2 |
| zh-0032 | 6 | 43.7 | 46.7 | 45.1 | 54.1 | yes | 40.5 | 35.3 |
| **zh** (2/15 files) | 18 | 47.3 | 3.7 | 6.9 | 7.7 | 2/2 | 43.2 | 41.2 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 79.0 | 79.0 | 79.0 |
| a_entity_found | 90.1 | 96.2 | 93.0 |
| a_event_concept | 80.7 | 80.7 | 80.7 |
| a_event_found | 94.3 | 100.0 | 97.1 |
| a_granularity | 97.2 | 98.6 | 97.9 |
| b_event_sense | 90.2 | 90.2 | 90.2 |
| c_aspect | 48.3 | 42.6 | 45.3 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 32.0 | 41.0 |
| c_polarity | 50.0 | 50.0 | 50.0 |
| c_refer | 100.0 | 42.9 | 60.0 |
| d_core_args_abstract | 38.0 | 75.9 | 50.6 |
| d_core_args_event | 58.5 | 56.4 | 57.4 |
| d_peripheral_entity | 42.8 | 42.8 | 42.8 |
| d_peripheral_event | 33.3 | 24.7 | 28.4 |
| e_core_labels | 79.3 | 79.3 | 79.3 |
| e_peripheral_labels | 80.8 | 80.8 | 80.8 |
| f_name_tokens | 57.1 | 46.2 | 51.1 |
| f_wiki | – | 0.0 | 0.0 |
| g_reentrancy | 50.0 | 31.0 | 38.3 |
| h_temporal | 35.6 | 25.0 | 29.4 |
| i_modal | 61.1 | 51.8 | 56.1 |
| j_coref_chain | 27.9 | 4.6 | 8.0 |
| j_coref_subset | – | – | – |
| k_doc_format | 99.2 | 99.2 | 99.2 |
