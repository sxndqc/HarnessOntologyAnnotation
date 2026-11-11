# runs/api/s2-search/gpt-6-astra-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 51.4 | 61.3 | 55.9 | 86.3 | no (3) | 81.0 | 76.8 | 88.5 |
| zh-0028 | 12 | 48.4 | 58.3 | 52.9 | 64.7 | no (1) | 48.1 | 47.5 | 63.0 |
| zh-0032 | 6 | 43.4 | 45.7 | 44.5 | 54.2 | no (1) | 39.3 | 33.7 | 53.1 |
| **zh** (2/15 files) | 18 | 45.9 | 3.8 | 6.9 | 8.1 | 0/2 | 43.7 | 40.6 | 58.1 |
| **en** (1/5 files) | 9 | 51.4 | 2.3 | 4.4 | 6.3 | 0/1 | 81.0 | 76.8 | 88.5 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 83.8 | 94.1 |
| a_entity_found | 91.0 | 95.3 |
| a_event_concept | 72.6 | 96.8 |
| a_event_found | 96.9 | 95.4 |
| a_granularity | 97.2 | 98.5 |
| b_event_sense | 89.2 | 96.3 |
| c_aspect | 55.4 | 66.7 |
| c_modstr | – | – |
| c_other_attributes | 49.1 | 100.0 |
| c_polarity | 83.3 | – |
| c_refer | 27.3 | 87.0 |
| d_core_args_abstract | 44.7 | 100.0 |
| d_core_args_event | 56.6 | 93.0 |
| d_peripheral_entity | 37.4 | 88.0 |
| d_peripheral_event | 29.4 | 80.0 |
| e_core_labels | 82.9 | 100.0 |
| e_peripheral_labels | 73.9 | 95.8 |
| f_name_tokens | 45.0 | 76.5 |
| f_wiki | – | 97.0 |
| g_reentrancy | 22.7 | 88.9 |
| h_temporal | 32.8 | 52.8 |
| i_modal | 52.6 | 67.2 |
| j_coref_chain | 12.0 | 78.6 |
| j_coref_subset | 0.0 | – |
| k_doc_format | 99.7 | 100.0 |
