# runs/api/s1-full/gpt-6-astra-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 50.7 | 60.4 | 55.2 | 83.7 | no (10) | 79.4 | 76.2 | 87.7 |
| zh-0028 | 12 | 42.7 | 51.8 | 46.8 | 60.2 | no (6) | 44.5 | 42.3 | 58.6 |
| zh-0032 | 6 | 41.2 | 44.6 | 42.8 | 50.7 | no (14) | 33.7 | 31.1 | 53.6 |
| **zh** (2/15 files) | 18 | 41.9 | 3.5 | 6.4 | 7.6 | 0/2 | 39.1 | 36.7 | 55.0 |
| **en** (1/5 files) | 9 | 50.8 | 2.3 | 4.4 | 6.3 | 0/1 | 79.4 | 76.2 | 87.7 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 80.4 | 94.1 |
| a_entity_found | 92.8 | 94.4 |
| a_event_concept | 67.6 | 96.8 |
| a_event_found | 95.3 | 95.4 |
| a_granularity | 96.6 | 98.5 |
| b_event_sense | 92.3 | 96.3 |
| c_aspect | 52.7 | 82.9 |
| c_modstr | – | – |
| c_other_attributes | 33.1 | 100.0 |
| c_polarity | 66.7 | – |
| c_refer | 31.3 | 71.4 |
| d_core_args_abstract | 43.8 | 100.0 |
| d_core_args_event | 46.3 | 78.3 |
| d_peripheral_entity | 44.4 | 80.0 |
| d_peripheral_event | 30.7 | 80.0 |
| e_core_labels | 80.3 | 100.0 |
| e_peripheral_labels | 88.7 | 91.7 |
| f_name_tokens | 32.7 | 76.5 |
| f_wiki | – | 97.0 |
| g_reentrancy | 8.7 | 90.3 |
| h_temporal | 20.7 | 60.9 |
| i_modal | 51.2 | 72.3 |
| j_coref_chain | 9.5 | 73.3 |
| j_coref_subset | 0.0 | – |
| k_doc_format | 98.6 | 99.0 |
