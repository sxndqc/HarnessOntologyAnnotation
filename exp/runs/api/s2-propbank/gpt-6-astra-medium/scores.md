# runs/api/s2-propbank/gpt-6-astra-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 48.1 | 50.0 | 49.1 | 76.2 | no (2) | 65.4 | 63.7 | 77.3 |
| zh-0028 | 12 | 46.9 | 57.5 | 51.6 | 62.1 | no (2) | 44.9 | 44.5 | 59.5 |
| zh-0032 | 6 | 42.1 | 47.3 | 44.6 | 54.7 | no (1) | 41.5 | 35.5 | 56.5 |
| **zh** (2/15 files) | 18 | 44.5 | 3.8 | 7.0 | 8.0 | 0/2 | 43.2 | 40.0 | 56.8 |
| **en** (1/5 files) | 9 | 48.1 | 1.9 | 3.6 | 5.3 | 0/1 | 65.4 | 63.7 | 77.3 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 80.1 | 94.0 |
| a_entity_found | 92.3 | 93.5 |
| a_event_concept | 73.9 | 87.1 |
| a_event_found | 98.1 | 98.4 |
| a_granularity | 97.3 | 96.4 |
| b_event_sense | 100.0 | 80.0 |
| c_aspect | 55.1 | 69.6 |
| c_modstr | – | – |
| c_other_attributes | 46.4 | 100.0 |
| c_polarity | 66.7 | – |
| c_refer | 25.0 | 91.7 |
| d_core_args_abstract | 27.6 | 83.3 |
| d_core_args_event | 62.6 | 67.1 |
| d_peripheral_entity | 38.4 | 60.4 |
| d_peripheral_event | 28.6 | 75.9 |
| e_core_labels | 84.9 | 90.9 |
| e_peripheral_labels | 71.2 | 90.9 |
| f_name_tokens | 45.4 | 71.0 |
| f_wiki | – | 0.0 |
| g_reentrancy | 19.6 | 58.3 |
| h_temporal | 28.4 | 40.8 |
| i_modal | 51.5 | 82.0 |
| j_coref_chain | 12.6 | 68.8 |
| j_coref_subset | 0.0 | – |
| k_doc_format | 100.0 | 100.0 |
