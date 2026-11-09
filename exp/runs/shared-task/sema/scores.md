# runs/shared-task/sema

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0000 | 100 | 14.9 | 16.3 | 15.5 | 38.1 | yes | – | – | 48.4 |
| en-0005 | 29 | 19.8 | 15.6 | 17.5 | 41.1 | yes | – | – | 41.2 |
| en-0006 | 28 | 26.2 | 18.2 | 21.4 | 46.9 | yes | – | – | 44.4 |
| en-0007 | 29 | 26.4 | 19.4 | 22.4 | 44.3 | yes | – | – | 41.0 |
| en-0008 | 9 | 39.9 | 32.1 | 35.6 | 57.0 | yes | – | – | 53.9 |
| zh-0021 | 12 | 26.9 | 18.2 | 21.7 | 36.9 | yes | 19.6 | 22.5 | 46.4 |
| zh-0022 | 11 | 30.5 | 16.6 | 21.5 | 36.9 | yes | 20.3 | 22.2 | 43.8 |
| zh-0023 | 17 | 31.0 | 26.3 | 28.5 | 45.3 | yes | – | – | 47.3 |
| zh-0024 | 20 | 31.4 | 23.8 | 27.1 | 49.7 | yes | – | – | 53.6 |
| zh-0026 | 36 | 23.1 | 20.6 | 21.8 | 38.1 | yes | – | – | 46.3 |
| zh-0027 | 15 | 35.8 | 27.9 | 31.3 | 48.4 | yes | – | – | 52.1 |
| zh-0028 | 12 | 35.2 | 26.5 | 30.3 | 47.6 | yes | 26.8 | 27.0 | 44.8 |
| zh-0029 | 20 | 32.0 | 23.2 | 26.9 | 46.9 | yes | 29.0 | 26.9 | 48.9 |
| zh-0030 | 10 | 26.2 | 22.6 | 24.3 | 44.1 | yes | 23.9 | 21.5 | 50.8 |
| zh-0031 | 13 | 27.4 | 20.4 | 23.3 | 45.4 | yes | 27.4 | 28.5 | 51.2 |
| zh-0032 | 6 | 39.5 | 29.8 | 34.0 | 52.2 | yes | – | – | 48.7 |
| zh-0033 | 13 | 36.6 | 22.8 | 28.1 | 41.8 | yes | 28.3 | 28.1 | 49.7 |
| zh-0034 | 10 | 23.8 | 20.2 | 21.9 | 44.5 | yes | – | – | 47.0 |
| zh-0035 | 26 | 33.0 | 28.3 | 30.5 | 49.0 | yes | – | – | 51.8 |
| zh-0036 | 15 | 17.2 | 21.4 | 19.1 | 32.5 | yes | – | – | 44.5 |
| **zh** (15/15 files) | 236 | 29.0 | 23.2 | 25.8 | 43.6 | 15/15 | 25.0 | 25.3 | 45.9 |
| **en** (5/5 files) | 195 | 19.9 | 17.7 | 18.7 | 41.6 | 5/5 | – | – | 44.1 |

## umrjudge per check

| check | zh | en |
|---|---|---|
| a_entity_concept | 67.5 | 66.8 |
| a_entity_found | 82.9 | 87.3 |
| a_event_concept | 74.8 | 64.2 |
| a_event_found | 85.2 | 84.7 |
| a_granularity | 95.5 | 92.3 |
| b_event_sense | 81.2 | 59.5 |
| c_aspect | 59.3 | 59.7 |
| c_modstr | – | – |
| c_other_attributes | 28.5 | 36.6 |
| c_polarity | 42.0 | 46.9 |
| c_refer | 27.1 | 44.9 |
| d_core_args_abstract | 10.7 | 22.7 |
| d_core_args_event | 33.4 | 22.0 |
| d_peripheral_entity | 27.9 | 26.5 |
| d_peripheral_event | 16.1 | 19.4 |
| e_core_labels | 69.1 | 67.1 |
| e_peripheral_labels | 60.9 | 58.5 |
| f_name_tokens | 33.7 | 55.6 |
| f_wiki | – | 2.3 |
| g_reentrancy | 13.6 | 9.7 |
| h_temporal | 0.0 | 0.0 |
| i_modal | 46.3 | 31.5 |
| j_coref_chain | 0.0 | 4.6 |
| j_coref_subset | 0.0 | 0.0 |
| k_doc_format | 99.5 | 94.8 |
