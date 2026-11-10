# runs/api/s2-gold/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 50.6 | 52.4 | 51.5 | 78.4 | no (2) | 70.4 | 66.3 | 82.1 |
| zh-0028 | 12 | 52.1 | 56.8 | 54.4 | 61.4 | yes | 45.0 | 46.5 | 57.9 |
| zh-0032 | 6 | 44.8 | 45.3 | 45.1 | 54.1 | yes | 40.3 | 34.6 | 57.6 |
| **zh** (2/15 files) | 18 | 48.4 | 3.7 | 6.8 | 7.6 | 2/2 | 42.7 | 40.5 | 58.0 |
| **en** (1/5 files) | 9 | 50.6 | 2.0 | 3.8 | 5.5 | 0/1 | 70.4 | 66.3 | 82.1 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 80.4 | 93.8 |
| a_entity_found | 93.4 | 92.3 |
| a_event_concept | 76.0 | 89.7 |
| a_event_found | 97.5 | 93.5 |
| a_granularity | 98.0 | 96.1 |
| b_event_sense | 88.5 | 83.3 |
| c_aspect | 44.8 | 56.5 |
| c_modstr | – | – |
| c_other_attributes | 37.5 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 70.6 | 84.2 |
| d_core_args_abstract | 19.3 | 100.0 |
| d_core_args_event | 52.6 | 74.8 |
| d_peripheral_entity | 41.5 | 78.6 |
| d_peripheral_event | 34.1 | 68.4 |
| e_core_labels | 67.1 | 90.9 |
| e_peripheral_labels | 80.6 | 95.5 |
| f_name_tokens | 48.0 | 96.8 |
| f_wiki | – | 60.0 |
| g_reentrancy | 20.7 | 75.0 |
| h_temporal | 29.4 | 44.4 |
| i_modal | 55.6 | 60.8 |
| j_coref_chain | 8.9 | 73.3 |
| j_coref_subset | – | – |
| k_doc_format | 99.3 | 97.8 |
