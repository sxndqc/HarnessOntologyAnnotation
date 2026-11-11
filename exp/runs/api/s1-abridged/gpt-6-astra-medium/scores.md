# runs/api/s1-abridged/gpt-6-astra-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 47.0 | 49.1 | 48.0 | 75.5 | no (2) | 67.1 | 64.6 | 78.0 |
| zh-0028 | 12 | 45.4 | 52.6 | 48.7 | 60.4 | yes | 43.9 | 45.4 | 60.5 |
| zh-0032 | 6 | 42.8 | 46.7 | 44.7 | 54.2 | no (1) | 40.6 | 35.7 | 54.6 |
| **zh** (2/15 files) | 18 | 44.0 | 3.6 | 6.6 | 7.8 | 1/2 | 42.2 | 40.5 | 56.4 |
| **en** (1/5 files) | 9 | 47.0 | 1.9 | 3.6 | 5.3 | 0/1 | 67.1 | 64.6 | 78.0 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 78.5 | 94.0 |
| a_entity_found | 93.1 | 92.6 |
| a_event_concept | 75.7 | 86.7 |
| a_event_found | 97.3 | 95.2 |
| a_granularity | 97.8 | 96.3 |
| b_event_sense | 89.6 | 73.9 |
| c_aspect | 52.9 | 62.2 |
| c_modstr | – | – |
| c_other_attributes | 31.2 | 100.0 |
| c_polarity | 83.3 | – |
| c_refer | 24.0 | 91.7 |
| d_core_args_abstract | 30.1 | 100.0 |
| d_core_args_event | 58.1 | 69.4 |
| d_peripheral_entity | 39.4 | 81.2 |
| d_peripheral_event | 31.0 | 63.3 |
| e_core_labels | 76.9 | 88.6 |
| e_peripheral_labels | 73.1 | 95.7 |
| f_name_tokens | 43.8 | 71.0 |
| f_wiki | – | 0.0 |
| g_reentrancy | 26.3 | 66.7 |
| h_temporal | 32.7 | 36.7 |
| i_modal | 55.9 | 78.0 |
| j_coref_chain | 6.9 | 73.3 |
| j_coref_subset | 0.0 | – |
| k_doc_format | 99.4 | 100.0 |
