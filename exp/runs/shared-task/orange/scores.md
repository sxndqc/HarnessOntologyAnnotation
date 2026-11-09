# runs/shared-task/orange

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0000 | 100 | 19.2 | 13.6 | 15.9 | 39.4 | yes | – | – | 42.3 |
| en-0005 | 29 | 38.9 | 17.7 | 24.3 | 50.2 | yes | 32.4 | 24.5 | 38.9 |
| en-0006 | 28 | 43.2 | 22.9 | 30.0 | 54.8 | yes | 37.7 | – | 42.4 |
| en-0007 | 29 | 38.6 | 17.6 | 24.2 | 50.1 | yes | 33.3 | 25.2 | 38.3 |
| en-0008 | 9 | 52.6 | 33.6 | 41.0 | 72.0 | yes | 59.0 | 50.7 | 57.6 |
| zh-0021 | 12 | 30.5 | 21.6 | 25.3 | 44.5 | yes | 24.8 | 25.8 | 54.7 |
| zh-0022 | 11 | 32.8 | 25.3 | 28.5 | 48.4 | yes | 24.4 | 23.3 | 40.9 |
| zh-0023 | 17 | 44.8 | 36.5 | 40.2 | 57.1 | yes | 42.8 | 42.2 | 56.8 |
| zh-0024 | 20 | 38.7 | 32.5 | 35.3 | 54.0 | yes | 37.1 | 34.9 | 51.4 |
| zh-0026 | 36 | 36.4 | 30.7 | 33.3 | 51.7 | yes | 36.2 | 35.8 | 52.2 |
| zh-0027 | 15 | 40.4 | 32.0 | 35.7 | 50.5 | yes | 32.6 | 29.5 | 47.1 |
| zh-0028 | 12 | 38.9 | 31.4 | 34.7 | 50.5 | yes | 29.5 | 26.0 | 48.0 |
| zh-0029 | 20 | 50.0 | 35.2 | 41.3 | 54.5 | yes | 33.2 | 27.5 | 49.3 |
| zh-0030 | 10 | 39.1 | 32.5 | 35.5 | 47.9 | yes | 30.2 | 25.9 | 47.9 |
| zh-0031 | 13 | 48.2 | 36.7 | 41.7 | 51.4 | yes | 34.4 | 32.4 | 52.1 |
| zh-0032 | 6 | 37.1 | 24.4 | 29.4 | 45.6 | yes | 28.2 | 24.8 | 47.3 |
| zh-0033 | 13 | 53.7 | 43.6 | 48.1 | 59.9 | yes | 41.7 | 35.5 | 54.0 |
| zh-0034 | 10 | 44.0 | 35.4 | 39.2 | 50.2 | yes | 32.3 | 30.7 | 53.8 |
| zh-0035 | 26 | 49.2 | 42.4 | 45.5 | 59.2 | yes | 44.1 | 42.7 | 59.0 |
| zh-0036 | 15 | 35.1 | 23.3 | 28.0 | 45.0 | yes | 28.2 | 23.1 | 41.8 |
| **zh** (15/15 files) | 236 | 41.2 | 32.5 | 36.3 | 52.1 | 15/15 | 33.3 | 30.7 | 47.7 |
| **en** (5/5 files) | 195 | 30.2 | 17.5 | 22.2 | 46.5 | 5/5 | 40.6 | 33.4 | 41.9 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 73.0 | 80.4 |
| a_entity_found | 87.9 | 86.2 |
| a_event_concept | 73.5 | 79.6 |
| a_event_found | 92.6 | 90.2 |
| a_granularity | 96.7 | 95.8 |
| b_event_sense | 80.9 | 67.5 |
| c_aspect | 35.9 | 1.9 |
| c_modstr | – | – |
| c_other_attributes | 37.7 | 46.8 |
| c_polarity | 42.4 | 39.7 |
| c_refer | 28.4 | 10.0 |
| d_core_args_abstract | 19.2 | 35.2 |
| d_core_args_event | 39.9 | 41.1 |
| d_peripheral_entity | 33.2 | 48.7 |
| d_peripheral_event | 25.8 | 42.9 |
| e_core_labels | 75.9 | 77.2 |
| e_peripheral_labels | 74.9 | 75.8 |
| f_name_tokens | 48.9 | 61.7 |
| f_wiki | – | 0.0 |
| g_reentrancy | 11.1 | 19.8 |
| h_temporal | 7.3 | 0.0 |
| i_modal | 30.8 | 1.8 |
| j_coref_chain | 0.0 | 0.6 |
| j_coref_subset | 0.0 | 0.0 |
| k_doc_format | 80.4 | 2.0 |
