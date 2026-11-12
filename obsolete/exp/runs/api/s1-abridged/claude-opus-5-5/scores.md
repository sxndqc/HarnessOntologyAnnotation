# runs/api/s1-abridged/claude-opus-5-5

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 40.4 | 44.1 | 42.2 | 61.5 | yes | 44.0 | 44.9 |
| zh-0032 | 6 | 43.4 | 44.6 | 44.0 | 54.7 | yes | 40.7 | 36.8 |
| **zh** (2/15 files) | 18 | 42.0 | 3.2 | 6.0 | 7.7 | 2/2 | 42.3 | 40.9 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 78.7 | 78.7 | 78.7 |
| a_entity_found | 91.0 | 97.6 | 94.2 |
| a_event_concept | 78.3 | 78.3 | 78.3 |
| a_event_found | 94.3 | 100.0 | 97.1 |
| a_granularity | 94.1 | 94.1 | 94.1 |
| b_event_sense | 89.8 | 89.8 | 89.8 |
| c_aspect | 52.5 | 45.7 | 48.9 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 34.8 | 43.2 |
| c_polarity | 33.3 | 50.0 | 40.0 |
| c_refer | 85.7 | 40.0 | 54.5 |
| d_core_args_abstract | 38.9 | 70.0 | 50.0 |
| d_core_args_event | 52.8 | 50.0 | 51.4 |
| d_peripheral_entity | 36.5 | 35.0 | 35.8 |
| d_peripheral_event | 31.9 | 25.3 | 28.2 |
| e_core_labels | 75.3 | 75.3 | 75.3 |
| e_peripheral_labels | 76.5 | 76.5 | 76.5 |
| f_name_tokens | 59.1 | 46.4 | 52.0 |
| f_wiki | – | 0.0 | 0.0 |
| g_reentrancy | 38.9 | 26.9 | 31.8 |
| h_temporal | 36.4 | 31.6 | 33.9 |
| i_modal | 56.9 | 47.7 | 51.9 |
| j_coref_chain | 37.9 | 6.4 | 11.0 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
