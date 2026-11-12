# runs/api/s1-abridged/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 55.3 | 54.2 | 54.7 | 79.1 | no (2) | 71.5 | 71.7 |
| zh-0028 | 12 | 48.2 | 54.4 | 51.1 | 59.7 | yes | 43.0 | 44.7 |
| zh-0032 | 6 | 48.9 | 45.2 | 47.0 | 53.9 | yes | 38.9 | 36.4 |
| **zh** (2/15 files) | 18 | 48.6 | 3.6 | 6.7 | 7.5 | 2/2 | 40.9 | 40.5 |
| **en** (1/5 files) | 9 | 55.3 | 2.0 | 4.0 | 5.4 | 0/1 | 71.5 | 71.7 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 78.3 | 78.3 | 78.3 | 95.9 | 95.9 | 95.9 |
| a_entity_found | 91.4 | 97.1 | 94.2 | 94.2 | 90.7 | 92.5 |
| a_event_concept | 78.6 | 78.6 | 78.6 | 82.8 | 82.8 | 82.8 |
| a_event_found | 95.5 | 100.0 | 97.7 | 90.6 | 100.0 | 95.1 |
| a_granularity | 97.2 | 98.6 | 97.9 | 96.9 | 95.5 | 96.2 |
| b_event_sense | 90.0 | 90.0 | 90.0 | 86.4 | 86.4 | 86.4 |
| c_aspect | 49.2 | 42.9 | 45.8 | 71.4 | 71.4 | 71.4 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 57.1 | 33.3 | 42.1 | 100.0 | 100.0 | 100.0 |
| c_polarity | 33.3 | 50.0 | 40.0 | – | – | – |
| c_refer | 85.7 | 33.3 | 48.0 | 72.7 | 88.9 | 80.0 |
| d_core_args_abstract | 25.4 | 43.9 | 32.2 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 51.9 | 50.9 | 51.4 | 57.9 | 67.6 | 62.4 |
| d_peripheral_entity | 46.1 | 45.1 | 45.6 | 81.2 | 81.2 | 81.2 |
| d_peripheral_event | 27.2 | 21.6 | 24.0 | 81.2 | 59.1 | 68.4 |
| e_core_labels | 70.4 | 70.4 | 70.4 | 82.4 | 82.4 | 82.4 |
| e_peripheral_labels | 80.8 | 80.8 | 80.8 | 91.7 | 91.7 | 91.7 |
| f_name_tokens | 47.8 | 39.3 | 43.1 | 93.8 | 100.0 | 96.8 |
| f_wiki | – | 0.0 | 0.0 | 53.3 | 88.9 | 66.7 |
| g_reentrancy | 38.9 | 29.2 | 33.3 | 57.1 | 88.9 | 69.6 |
| h_temporal | 34.7 | 32.5 | 33.6 | 63.2 | 52.2 | 57.1 |
| i_modal | 56.2 | 65.3 | 60.4 | 86.4 | 79.2 | 82.6 |
| j_coref_chain | 7.7 | 1.5 | 2.6 | 100.0 | 57.9 | 73.3 |
| j_coref_subset | – | 0.0 | 0.0 | – | – | – |
| k_doc_format | 99.5 | 99.5 | 99.5 | 100.0 | 100.0 | 100.0 |
