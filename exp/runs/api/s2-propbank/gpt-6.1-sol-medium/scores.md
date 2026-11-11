# runs/api/s2-propbank/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 47.1 | 50.0 | 48.5 | 75.9 | no (2) | 63.5 | 62.0 | 77.3 |
| zh-0028 | 12 | 47.1 | 56.1 | 51.3 | 61.4 | yes | 44.4 | 44.2 | 58.7 |
| zh-0032 | 6 | 41.9 | 46.1 | 43.9 | 54.8 | yes | 39.8 | 34.1 | 54.8 |
| **zh** (2/15 files) | 18 | 44.5 | 3.7 | 6.8 | 7.9 | 2/2 | 42.1 | 39.1 | 56.8 |
| **en** (1/5 files) | 9 | 47.1 | 1.9 | 3.6 | 5.3 | 0/1 | 63.5 | 62.0 | 77.3 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 76.5 | 92.0 |
| a_entity_found | 92.3 | 93.5 |
| a_event_concept | 78.5 | 90.0 |
| a_event_found | 97.5 | 96.8 |
| a_granularity | 97.3 | 96.4 |
| b_event_sense | 100.0 | 80.0 |
| c_aspect | 54.4 | 65.2 |
| c_modstr | – | – |
| c_other_attributes | 35.1 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 27.3 | 88.0 |
| d_core_args_abstract | 27.8 | 83.3 |
| d_core_args_event | 61.4 | 63.8 |
| d_peripheral_entity | 38.6 | 52.1 |
| d_peripheral_event | 25.5 | 80.4 |
| e_core_labels | 87.4 | 90.3 |
| e_peripheral_labels | 70.6 | 85.0 |
| f_name_tokens | 41.6 | 58.1 |
| f_wiki | – | 43.5 |
| g_reentrancy | 16.3 | 58.3 |
| h_temporal | 22.4 | 49.0 |
| i_modal | 53.0 | 78.0 |
| j_coref_chain | 12.5 | 56.2 |
| j_coref_subset | – | – |
| k_doc_format | 100.0 | 100.0 |
