# runs/api/s3-all/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 53.4 | 61.0 | 56.9 | 86.8 | no (3) | 82.5 | 79.2 | 89.3 |
| zh-0028 | 12 | 52.2 | 59.2 | 55.5 | 66.4 | no (2) | 50.0 | 48.5 | 64.9 |
| zh-0032 | 6 | 44.0 | 46.5 | 45.2 | 54.5 | yes | 36.1 | 32.9 | 53.8 |
| **zh** (2/15 files) | 18 | 48.0 | 3.8 | 7.0 | 8.0 | 1/2 | 43.0 | 40.7 | 58.2 |
| **en** (1/5 files) | 9 | 53.4 | 2.3 | 4.4 | 6.3 | 0/1 | 82.5 | 79.2 | 89.3 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 87.1 | 94.1 |
| a_entity_found | 92.1 | 95.3 |
| a_event_concept | 76.2 | 96.8 |
| a_event_found | 95.2 | 95.4 |
| a_granularity | 97.2 | 98.5 |
| b_event_sense | 97.4 | 92.6 |
| c_aspect | 49.6 | 80.0 |
| c_modstr | – | – |
| c_other_attributes | 42.5 | 100.0 |
| c_polarity | 83.3 | – |
| c_refer | 25.0 | 81.8 |
| d_core_args_abstract | 33.3 | 100.0 |
| d_core_args_event | 64.5 | 93.0 |
| d_peripheral_entity | 38.0 | 88.0 |
| d_peripheral_event | 28.5 | 80.0 |
| e_core_labels | 88.5 | 100.0 |
| e_peripheral_labels | 71.7 | 95.8 |
| f_name_tokens | 43.8 | 76.5 |
| f_wiki | – | 97.0 |
| g_reentrancy | 27.8 | 88.9 |
| h_temporal | 31.2 | 58.3 |
| i_modal | 53.1 | 74.4 |
| j_coref_chain | 12.9 | 78.6 |
| j_coref_subset | 0.0 | – |
| k_doc_format | 100.0 | 100.0 |
