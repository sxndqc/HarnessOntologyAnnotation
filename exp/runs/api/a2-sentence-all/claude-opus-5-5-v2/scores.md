# runs/api/a2-sentence-all/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 53.4 | 55.7 | 54.5 | 82.3 | no (4) | 74.4 | 73.7 | 85.1 |
| zh-0028 | 12 | 51.2 | 56.6 | 53.7 | 63.7 | yes | 50.2 | 50.9 | 60.1 |
| zh-0032 | 6 | 46.8 | 49.6 | 48.2 | 58.2 | yes | 44.0 | 39.2 | 57.5 |
| **zh** (2/15 files) | 18 | 48.9 | 3.8 | 7.1 | 8.1 | 2/2 | 47.1 | 45.1 | 58.8 |
| **en** (1/5 files) | 9 | 53.4 | 2.1 | 4.0 | 5.8 | 0/1 | 74.4 | 73.7 | 85.1 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 81.3 | 95.9 |
| a_entity_found | 94.5 | 91.6 |
| a_event_concept | 76.6 | 90.0 |
| a_event_found | 96.8 | 96.8 |
| a_granularity | 98.0 | 98.5 |
| b_event_sense | 97.4 | 87.5 |
| c_aspect | 53.9 | 66.7 |
| c_modstr | – | – |
| c_other_attributes | 50.9 | 100.0 |
| c_polarity | 33.3 | – |
| c_refer | 37.5 | 76.2 |
| d_core_args_abstract | 37.4 | 100.0 |
| d_core_args_event | 68.8 | 75.8 |
| d_peripheral_entity | 47.3 | 67.4 |
| d_peripheral_event | 32.0 | 83.3 |
| e_core_labels | 89.7 | 97.1 |
| e_peripheral_labels | 79.5 | 95.0 |
| f_name_tokens | 49.3 | 100.0 |
| f_wiki | 0.0 | 64.3 |
| g_reentrancy | 20.7 | 72.0 |
| h_temporal | 30.9 | 54.5 |
| i_modal | 59.4 | 85.7 |
| j_coref_chain | 18.3 | 75.9 |
| j_coref_subset | – | – |
| k_doc_format | 99.6 | 97.6 |
