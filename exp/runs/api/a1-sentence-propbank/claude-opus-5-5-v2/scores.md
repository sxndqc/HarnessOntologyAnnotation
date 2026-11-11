# runs/api/a1-sentence-propbank/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 53.7 | 56.5 | 55.1 | 81.8 | no (4) | 75.5 | 74.3 | 84.4 |
| zh-0028 | 12 | 47.6 | 53.5 | 50.4 | 60.3 | yes | 42.7 | 44.8 | 55.5 |
| zh-0032 | 6 | 46.6 | 49.8 | 48.2 | 57.8 | no (3) | 42.9 | 37.6 | 57.2 |
| **zh** (2/15 files) | 18 | 47.1 | 3.7 | 6.9 | 7.9 | 1/2 | 42.8 | 41.2 | 55.2 |
| **en** (1/5 files) | 9 | 53.7 | 2.1 | 4.1 | 5.8 | 0/1 | 75.5 | 74.3 | 84.4 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 80.6 | 96.0 |
| a_entity_found | 92.7 | 92.6 |
| a_event_concept | 76.3 | 93.5 |
| a_event_found | 97.3 | 98.4 |
| a_granularity | 98.0 | 96.3 |
| b_event_sense | 97.4 | 80.8 |
| c_aspect | 50.9 | 66.7 |
| c_modstr | – | – |
| c_other_attributes | 43.5 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 35.3 | 81.8 |
| d_core_args_abstract | 29.7 | 83.3 |
| d_core_args_event | 66.5 | 71.7 |
| d_peripheral_entity | 41.5 | 81.2 |
| d_peripheral_event | 39.7 | 77.8 |
| e_core_labels | 83.4 | 93.9 |
| e_peripheral_labels | 79.3 | 95.8 |
| f_name_tokens | 53.7 | 96.8 |
| f_wiki | 0.0 | 69.2 |
| g_reentrancy | 22.6 | 72.0 |
| h_temporal | 33.5 | 52.2 |
| i_modal | 54.8 | 84.0 |
| j_coref_chain | 15.4 | 73.3 |
| j_coref_subset | 0.0 | – |
| k_doc_format | 98.4 | 98.9 |
