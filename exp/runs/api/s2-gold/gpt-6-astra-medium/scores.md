# runs/api/s2-gold/gpt-6-astra-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 46.1 | 47.3 | 46.7 | 73.4 | no (2) | 62.1 | 59.5 | 74.8 |
| zh-0028 | 12 | 49.7 | 57.9 | 53.5 | 62.3 | yes | 45.9 | 46.1 | 60.0 |
| zh-0032 | 6 | 43.7 | 44.8 | 44.2 | 54.2 | yes | 39.1 | 33.8 | 56.2 |
| **zh** (2/15 files) | 18 | 46.7 | 3.7 | 6.8 | 7.8 | 2/2 | 42.5 | 39.9 | 56.8 |
| **en** (1/5 files) | 9 | 46.1 | 1.8 | 3.5 | 5.1 | 0/1 | 62.1 | 59.5 | 74.8 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 82.7 | 92.0 |
| a_entity_found | 91.0 | 93.5 |
| a_event_concept | 77.1 | 86.7 |
| a_event_found | 95.8 | 95.2 |
| a_granularity | 96.9 | 96.4 |
| b_event_sense | 86.8 | 75.0 |
| c_aspect | 47.5 | 62.2 |
| c_modstr | – | – |
| c_other_attributes | 36.6 | 100.0 |
| c_polarity | 66.7 | – |
| c_refer | 35.3 | 90.9 |
| d_core_args_abstract | 35.7 | 83.3 |
| d_core_args_event | 56.8 | 65.0 |
| d_peripheral_entity | 39.6 | 76.1 |
| d_peripheral_event | 28.7 | 56.9 |
| e_core_labels | 81.2 | 87.5 |
| e_peripheral_labels | 81.2 | 90.9 |
| f_name_tokens | 42.4 | 71.0 |
| f_wiki | – | 0.0 |
| g_reentrancy | 27.9 | 52.2 |
| h_temporal | 28.9 | 32.7 |
| i_modal | 53.1 | 78.0 |
| j_coref_chain | 15.6 | 60.0 |
| j_coref_subset | 0.0 | – |
| k_doc_format | 100.0 | 100.0 |
