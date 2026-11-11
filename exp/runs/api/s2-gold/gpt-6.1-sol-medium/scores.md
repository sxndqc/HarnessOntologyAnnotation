# runs/api/s2-gold/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 45.0 | 51.8 | 48.1 | 78.7 | no (3) | 71.2 | 66.9 | 80.5 |
| zh-0028 | 12 | 49.1 | 58.3 | 53.3 | 62.7 | no (1) | 46.1 | 45.8 | 58.2 |
| zh-0032 | 6 | 43.1 | 46.7 | 44.8 | 54.1 | no (2) | 40.6 | 35.4 | 55.4 |
| **zh** (2/15 files) | 18 | 46.0 | 3.8 | 7.0 | 7.9 | 0/2 | 43.3 | 40.6 | 56.8 |
| **en** (1/5 files) | 9 | 45.0 | 2.0 | 3.8 | 5.8 | 0/1 | 71.2 | 66.9 | 80.5 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 80.9 | 96.2 |
| a_entity_found | 93.0 | 95.4 |
| a_event_concept | 76.0 | 81.2 |
| a_event_found | 97.0 | 97.0 |
| a_granularity | 96.9 | 98.5 |
| b_event_sense | 87.1 | 73.9 |
| c_aspect | 48.6 | 59.6 |
| c_modstr | – | – |
| c_other_attributes | 36.6 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 33.3 | 91.7 |
| d_core_args_abstract | 22.8 | 86.7 |
| d_core_args_event | 58.9 | 70.9 |
| d_peripheral_entity | 38.5 | 76.1 |
| d_peripheral_event | 29.4 | 66.7 |
| e_core_labels | 74.8 | 91.7 |
| e_peripheral_labels | 73.4 | 90.9 |
| f_name_tokens | 46.5 | 76.5 |
| f_wiki | – | 81.2 |
| g_reentrancy | 27.7 | 56.0 |
| h_temporal | 30.1 | 34.6 |
| i_modal | 52.5 | 73.6 |
| j_coref_chain | 12.6 | 73.3 |
| j_coref_subset | – | – |
| k_doc_format | 99.3 | 100.0 |
