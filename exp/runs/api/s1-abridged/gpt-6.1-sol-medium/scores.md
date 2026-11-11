# runs/api/s1-abridged/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 44.1 | 45.2 | 44.6 | 72.2 | no (2) | 60.1 | 59.8 | 74.4 |
| zh-0028 | 12 | 45.9 | 57.0 | 50.9 | 59.6 | yes | 42.4 | 42.2 | 56.2 |
| zh-0032 | 6 | 43.6 | 46.3 | 44.9 | 55.1 | no (1) | 40.4 | 35.3 | 54.5 |
| **zh** (2/15 files) | 18 | 44.8 | 3.7 | 6.9 | 7.8 | 1/2 | 41.4 | 38.8 | 55.3 |
| **en** (1/5 files) | 9 | 44.1 | 1.7 | 3.3 | 5.0 | 0/1 | 60.1 | 59.8 | 74.4 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 78.5 | 93.9 |
| a_entity_found | 92.6 | 92.5 |
| a_event_concept | 77.5 | 83.3 |
| a_event_found | 97.5 | 95.2 |
| a_granularity | 96.6 | 96.2 |
| b_event_sense | 86.0 | 78.3 |
| c_aspect | 50.9 | 62.2 |
| c_modstr | – | – |
| c_other_attributes | 33.6 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 27.3 | 85.7 |
| d_core_args_abstract | 24.8 | 83.3 |
| d_core_args_event | 53.3 | 60.2 |
| d_peripheral_entity | 35.5 | 70.5 |
| d_peripheral_event | 28.2 | 63.3 |
| e_core_labels | 76.2 | 81.8 |
| e_peripheral_labels | 73.7 | 95.2 |
| f_name_tokens | 42.7 | 58.1 |
| f_wiki | – | 0.0 |
| g_reentrancy | 25.8 | 48.0 |
| h_temporal | 25.2 | 41.7 |
| i_modal | 53.8 | 74.0 |
| j_coref_chain | 4.8 | 73.3 |
| j_coref_subset | – | – |
| k_doc_format | 99.7 | 100.0 |
