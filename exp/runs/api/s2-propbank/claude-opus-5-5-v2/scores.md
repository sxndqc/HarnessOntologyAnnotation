# runs/api/s2-propbank/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 54.9 | 57.1 | 56.0 | 81.8 | no (2) | 73.6 | 71.1 | 85.1 |
| zh-0028 | 12 | 48.9 | 53.5 | 51.1 | 59.5 | yes | 44.0 | 45.7 | 55.9 |
| zh-0032 | 6 | 43.5 | 47.5 | 45.4 | 55.3 | no (1) | 39.1 | 34.7 | 50.6 |
| **zh** (2/15 files) | 18 | 46.0 | 3.6 | 6.8 | 7.7 | 1/2 | 41.5 | 40.2 | 53.2 |
| **en** (1/5 files) | 9 | 54.9 | 2.2 | 4.2 | 5.7 | 0/1 | 73.6 | 71.1 | 85.1 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 77.3 | 95.8 |
| a_entity_found | 92.9 | 91.4 |
| a_event_concept | 79.6 | 93.3 |
| a_event_found | 95.3 | 96.8 |
| a_granularity | 98.0 | 96.3 |
| b_event_sense | 98.8 | 88.5 |
| c_aspect | 45.9 | 59.6 |
| c_modstr | – | – |
| c_other_attributes | 36.6 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 26.1 | 80.0 |
| d_core_args_abstract | 24.6 | 100.0 |
| d_core_args_event | 66.7 | 70.6 |
| d_peripheral_entity | 44.6 | 76.1 |
| d_peripheral_event | 33.4 | 77.8 |
| e_core_labels | 86.6 | 96.9 |
| e_peripheral_labels | 78.1 | 95.2 |
| f_name_tokens | 40.6 | 96.8 |
| f_wiki | 0.0 | 82.8 |
| g_reentrancy | 26.1 | 78.3 |
| h_temporal | 27.2 | 51.1 |
| i_modal | 56.9 | 72.5 |
| j_coref_chain | 9.9 | 73.3 |
| j_coref_subset | 0.0 | – |
| k_doc_format | 99.3 | 100.0 |
