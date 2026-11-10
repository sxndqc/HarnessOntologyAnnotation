# runs/api/s1-abridged/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 55.3 | 54.2 | 54.7 | 79.1 | no (2) | 71.5 | 71.7 | 83.3 |
| zh-0028 | 12 | 48.2 | 54.4 | 51.1 | 59.7 | yes | 43.0 | 44.7 | 52.8 |
| zh-0032 | 6 | 48.9 | 45.2 | 47.0 | 53.9 | yes | 38.9 | 36.4 | 55.7 |
| **zh** (2/15 files) | 18 | 48.6 | 3.6 | 6.7 | 7.5 | 2/2 | 40.9 | 40.5 | 51.9 |
| **en** (1/5 files) | 9 | 55.3 | 2.0 | 4.0 | 5.4 | 0/1 | 71.5 | 71.7 | 83.3 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 78.2 | 95.9 |
| a_entity_found | 93.9 | 92.5 |
| a_event_concept | 77.1 | 82.8 |
| a_event_found | 97.5 | 95.1 |
| a_granularity | 98.0 | 96.2 |
| b_event_sense | 89.9 | 86.4 |
| c_aspect | 47.4 | 71.4 |
| c_modstr | – | – |
| c_other_attributes | 35.8 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 25.0 | 80.0 |
| d_core_args_abstract | 35.3 | 100.0 |
| d_core_args_event | 49.7 | 62.4 |
| d_peripheral_entity | 43.8 | 81.2 |
| d_peripheral_event | 28.4 | 68.4 |
| e_core_labels | 69.7 | 82.4 |
| e_peripheral_labels | 77.4 | 91.7 |
| f_name_tokens | 41.2 | 96.8 |
| f_wiki | 0.0 | 66.7 |
| g_reentrancy | 29.3 | 69.6 |
| h_temporal | 33.0 | 57.1 |
| i_modal | 60.6 | 82.6 |
| j_coref_chain | 2.6 | 73.3 |
| j_coref_subset | 0.0 | – |
| k_doc_format | 99.4 | 100.0 |
