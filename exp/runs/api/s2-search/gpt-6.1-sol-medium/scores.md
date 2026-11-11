# runs/api/s2-search/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 51.0 | 61.0 | 55.6 | 86.0 | no (3) | 81.0 | 76.5 | 88.6 |
| zh-0028 | 12 | 50.9 | 57.7 | 54.1 | 64.1 | yes | 50.1 | 47.5 | 61.9 |
| zh-0032 | 6 | 40.7 | 46.5 | 43.4 | 53.9 | yes | 39.7 | 34.4 | 53.3 |
| **zh** (2/15 files) | 18 | 45.4 | 3.8 | 6.9 | 8.0 | 2/2 | 44.9 | 40.9 | 56.2 |
| **en** (1/5 files) | 9 | 51.0 | 2.3 | 4.4 | 6.3 | 0/1 | 81.0 | 76.5 | 88.6 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 78.5 | 94.1 |
| a_entity_found | 93.4 | 95.3 |
| a_event_concept | 80.5 | 96.8 |
| a_event_found | 96.1 | 95.4 |
| a_granularity | 97.2 | 98.5 |
| b_event_sense | 88.3 | 96.3 |
| c_aspect | 55.1 | 66.7 |
| c_modstr | – | – |
| c_other_attributes | 38.8 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 33.3 | 87.0 |
| d_core_args_abstract | 47.5 | 100.0 |
| d_core_args_event | 57.2 | 93.0 |
| d_peripheral_entity | 42.6 | 88.0 |
| d_peripheral_event | 33.0 | 87.5 |
| e_core_labels | 87.6 | 100.0 |
| e_peripheral_labels | 75.0 | 96.0 |
| f_name_tokens | 41.0 | 76.5 |
| f_wiki | 0.0 | 97.0 |
| g_reentrancy | 27.0 | 88.9 |
| h_temporal | 23.7 | 52.8 |
| i_modal | 51.5 | 67.2 |
| j_coref_chain | 13.0 | 73.3 |
| j_coref_subset | – | – |
| k_doc_format | 100.0 | 100.0 |
