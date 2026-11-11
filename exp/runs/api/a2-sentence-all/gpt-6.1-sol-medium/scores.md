# runs/api/a2-sentence-all/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 53.6 | 57.4 | 55.5 | 83.3 | no (3) | 77.9 | 74.7 | 86.3 |
| zh-0028 | 12 | 54.5 | 58.3 | 56.4 | 65.7 | no (1) | 50.7 | 50.1 | 60.9 |
| zh-0032 | 6 | 46.1 | 48.6 | 47.3 | 58.1 | no (1) | 40.8 | 36.1 | 57.0 |
| **zh** (2/15 files) | 18 | 50.0 | 3.9 | 7.2 | 8.1 | 0/2 | 45.8 | 43.1 | 57.7 |
| **en** (1/5 files) | 9 | 53.6 | 2.2 | 4.2 | 5.9 | 0/1 | 77.9 | 74.7 | 86.3 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 83.3 | 94.1 |
| a_entity_found | 92.8 | 94.4 |
| a_event_concept | 80.7 | 93.5 |
| a_event_found | 95.8 | 95.4 |
| a_granularity | 96.9 | 98.5 |
| b_event_sense | 96.1 | 80.8 |
| c_aspect | 53.2 | 77.3 |
| c_modstr | – | – |
| c_other_attributes | 49.0 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 35.7 | 76.2 |
| d_core_args_abstract | 43.0 | 100.0 |
| d_core_args_event | 69.4 | 85.0 |
| d_peripheral_entity | 40.8 | 79.3 |
| d_peripheral_event | 29.3 | 75.0 |
| e_core_labels | 85.4 | 97.3 |
| e_peripheral_labels | 79.9 | 95.7 |
| f_name_tokens | 43.7 | 82.4 |
| f_wiki | – | 75.9 |
| g_reentrancy | 25.8 | 92.3 |
| h_temporal | 28.8 | 43.5 |
| i_modal | 54.6 | 85.7 |
| j_coref_chain | 10.1 | 75.9 |
| j_coref_subset | 0.0 | – |
| k_doc_format | 99.2 | 100.0 |
