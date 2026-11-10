# runs/api/s2-search/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 53.3 | 54.8 | 54.0 | 79.5 | no (2) | 69.7 | 68.5 | 82.1 |
| zh-0028 | 12 | 51.7 | 56.4 | 53.9 | 63.6 | yes | 47.5 | 48.1 | 58.7 |
| zh-0032 | 6 | 47.0 | 45.7 | 46.4 | 54.3 | no (20) | 40.7 | 37.2 | 56.1 |
| **zh** (2/15 files) | 18 | 49.4 | 3.7 | 6.8 | 7.8 | 1/2 | 44.1 | 42.7 | 56.2 |
| **en** (1/5 files) | 9 | 53.3 | 2.1 | 4.0 | 5.5 | 0/1 | 69.7 | 68.5 | 82.1 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 78.8 | 95.9 |
| a_entity_found | 93.4 | 93.3 |
| a_event_concept | 78.6 | 82.8 |
| a_event_found | 96.1 | 95.1 |
| a_granularity | 97.3 | 96.2 |
| b_event_sense | 89.7 | 90.9 |
| c_aspect | 50.3 | 60.9 |
| c_modstr | – | – |
| c_other_attributes | 33.9 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 35.3 | 81.8 |
| d_core_args_abstract | 40.2 | 100.0 |
| d_core_args_event | 55.2 | 62.5 |
| d_peripheral_entity | 39.3 | 84.8 |
| d_peripheral_event | 35.8 | 68.4 |
| e_core_labels | 78.8 | 84.8 |
| e_peripheral_labels | 78.2 | 91.7 |
| f_name_tokens | 42.8 | 93.3 |
| f_wiki | – | 64.3 |
| g_reentrancy | 33.9 | 75.0 |
| h_temporal | 36.1 | 54.5 |
| i_modal | 55.9 | 76.0 |
| j_coref_chain | 9.3 | 54.8 |
| j_coref_subset | 0.0 | – |
| k_doc_format | 99.6 | 100.0 |
