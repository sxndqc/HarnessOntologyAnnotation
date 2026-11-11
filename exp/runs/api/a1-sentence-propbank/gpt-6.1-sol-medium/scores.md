# runs/api/a1-sentence-propbank/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 45.1 | 48.2 | 46.6 | 75.8 | no (2) | 64.6 | 62.4 | 77.2 |
| zh-0028 | 12 | 47.7 | 55.3 | 51.2 | 61.4 | no (1) | 45.2 | 43.7 | 55.7 |
| zh-0032 | 6 | 41.8 | 45.7 | 43.7 | 54.1 | no (3) | 37.6 | 32.7 | 54.4 |
| **zh** (2/15 files) | 18 | 44.6 | 3.6 | 6.7 | 7.7 | 0/2 | 41.4 | 38.2 | 53.9 |
| **en** (1/5 files) | 9 | 45.1 | 1.8 | 3.5 | 5.3 | 0/1 | 64.6 | 62.4 | 77.2 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 79.9 | 93.9 |
| a_entity_found | 92.1 | 90.7 |
| a_event_concept | 77.1 | 90.3 |
| a_event_found | 97.5 | 95.4 |
| a_granularity | 97.3 | 96.3 |
| b_event_sense | 97.6 | 80.0 |
| c_aspect | 49.5 | 65.2 |
| c_modstr | – | – |
| c_other_attributes | 46.4 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 25.0 | 90.9 |
| d_core_args_abstract | 21.3 | 83.3 |
| d_core_args_event | 65.1 | 67.1 |
| d_peripheral_entity | 39.8 | 73.8 |
| d_peripheral_event | 28.6 | 70.6 |
| e_core_labels | 79.8 | 93.8 |
| e_peripheral_labels | 74.8 | 95.2 |
| f_name_tokens | 38.8 | 71.0 |
| f_wiki | – | 0.0 |
| g_reentrancy | 14.3 | 58.3 |
| h_temporal | 23.2 | 34.6 |
| i_modal | 50.8 | 75.0 |
| j_coref_chain | 8.1 | 73.3 |
| j_coref_subset | 0.0 | – |
| k_doc_format | 99.0 | 100.0 |
