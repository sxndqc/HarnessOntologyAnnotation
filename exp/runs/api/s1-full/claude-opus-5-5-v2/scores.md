# runs/api/s1-full/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 56.2 | 56.8 | 56.5 | 80.9 | no (2) | 71.4 | 70.7 | 81.0 |
| zh-0028 | 12 | 50.3 | 52.4 | 51.3 | 61.2 | yes | 42.6 | 44.4 | 58.3 |
| zh-0032 | 6 | 49.9 | 45.0 | 47.3 | 55.2 | yes | 38.7 | 36.2 | 58.6 |
| **zh** (2/15 files) | 18 | 50.1 | 3.5 | 6.6 | 7.6 | 2/2 | 40.7 | 40.3 | 58.5 |
| **en** (1/5 files) | 9 | 56.2 | 2.1 | 4.1 | 5.5 | 0/1 | 71.4 | 70.7 | 81.1 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 79.0 | 94.0 |
| a_entity_found | 92.9 | 93.5 |
| a_event_concept | 72.6 | 93.5 |
| a_event_found | 96.3 | 96.9 |
| a_granularity | 96.7 | 96.4 |
| b_event_sense | 89.5 | 92.3 |
| c_aspect | 47.0 | 76.2 |
| c_modstr | – | – |
| c_other_attributes | 49.1 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 62.5 | 81.8 |
| d_core_args_abstract | 34.2 | 83.3 |
| d_core_args_event | 47.9 | 66.7 |
| d_peripheral_entity | 33.5 | 78.5 |
| d_peripheral_event | 36.4 | 62.5 |
| e_core_labels | 74.7 | 94.1 |
| e_peripheral_labels | 77.9 | 90.9 |
| f_name_tokens | 37.5 | 96.8 |
| f_wiki | – | 0.0 |
| g_reentrancy | 31.3 | 78.3 |
| h_temporal | 35.2 | 65.1 |
| i_modal | 57.7 | 79.2 |
| j_coref_chain | 1.8 | 64.3 |
| j_coref_subset | – | – |
| k_doc_format | 100.0 | 98.9 |
