# runs/api/s1-full/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 55.1 | 64.0 | 59.2 | 86.0 | no (10) | 83.9 | 79.8 | 90.0 |
| zh-0028 | 12 | 44.3 | 54.4 | 48.8 | 59.6 | no (7) | 43.3 | 41.8 | 59.9 |
| zh-0032 | 6 | 39.9 | 43.0 | 41.4 | 50.6 | no (6) | 33.8 | 32.6 | 52.0 |
| **zh** (2/15 files) | 18 | 42.1 | 3.5 | 6.5 | 7.6 | 0/2 | 38.5 | 37.2 | 55.9 |
| **en** (1/5 files) | 9 | 55.1 | 2.4 | 4.6 | 6.3 | 0/1 | 83.9 | 79.8 | 90.0 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 79.4 | 94.0 |
| a_entity_found | 92.1 | 94.3 |
| a_event_concept | 71.1 | 96.8 |
| a_event_found | 95.8 | 95.4 |
| a_granularity | 96.8 | 98.5 |
| b_event_sense | 91.6 | 96.3 |
| c_aspect | 54.4 | 82.9 |
| c_modstr | – | – |
| c_other_attributes | 32.6 | 100.0 |
| c_polarity | 66.7 | – |
| c_refer | 18.2 | 87.0 |
| d_core_args_abstract | 28.3 | 100.0 |
| d_core_args_event | 43.8 | 85.3 |
| d_peripheral_entity | 34.8 | 83.3 |
| d_peripheral_event | 28.0 | 80.0 |
| e_core_labels | 78.1 | 100.0 |
| e_peripheral_labels | 76.0 | 95.7 |
| f_name_tokens | 45.7 | 100.0 |
| f_wiki | – | 97.0 |
| g_reentrancy | 15.5 | 90.3 |
| h_temporal | 23.8 | 60.9 |
| i_modal | 55.9 | 74.5 |
| j_coref_chain | 1.7 | 69.0 |
| j_coref_subset | – | – |
| k_doc_format | 100.0 | 99.0 |
