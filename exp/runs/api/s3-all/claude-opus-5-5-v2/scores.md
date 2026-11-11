# runs/api/s3-all/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 51.8 | 51.8 | 51.8 | 78.6 | no (2) | 70.3 | 69.7 | 83.4 |
| zh-0028 | 12 | 48.9 | 52.4 | 50.6 | 58.4 | yes | 40.7 | 43.0 | 56.2 |
| zh-0032 | 6 | 46.8 | 47.5 | 47.1 | 56.2 | yes | 42.0 | 36.3 | 54.9 |
| **zh** (2/15 files) | 18 | 47.8 | 3.6 | 6.7 | 7.6 | 2/2 | 41.3 | 39.6 | 54.3 |
| **en** (1/5 files) | 9 | 51.8 | 2.0 | 3.8 | 5.4 | 0/1 | 70.3 | 69.7 | 83.4 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 76.9 | 93.8 |
| a_entity_found | 93.4 | 92.3 |
| a_event_concept | 77.3 | 89.7 |
| a_event_found | 96.8 | 95.1 |
| a_granularity | 96.8 | 96.2 |
| b_event_sense | 89.8 | 87.5 |
| c_aspect | 46.7 | 60.9 |
| c_modstr | – | – |
| c_other_attributes | 34.4 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 33.3 | 84.2 |
| d_core_args_abstract | 18.7 | 100.0 |
| d_core_args_event | 59.1 | 77.5 |
| d_peripheral_entity | 39.2 | 73.8 |
| d_peripheral_event | 37.3 | 83.3 |
| e_core_labels | 81.6 | 97.0 |
| e_peripheral_labels | 77.8 | 95.5 |
| f_name_tokens | 39.2 | 71.0 |
| f_wiki | 0.0 | 60.9 |
| g_reentrancy | 24.1 | 75.0 |
| h_temporal | 29.6 | 54.5 |
| i_modal | 56.1 | 74.0 |
| j_coref_chain | 8.2 | 73.3 |
| j_coref_subset | – | – |
| k_doc_format | 99.6 | 100.0 |
