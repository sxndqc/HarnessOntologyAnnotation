# runs/api/a2-sentence-all/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 53.6 | 57.4 | 55.5 | 83.3 | no (3) | 77.9 | 74.7 |
| zh-0028 | 12 | 54.5 | 58.3 | 56.4 | 65.7 | no (1) | 50.7 | 50.1 |
| zh-0032 | 6 | 46.1 | 48.6 | 47.3 | 58.1 | no (1) | 40.8 | 36.1 |
| **zh** (2/15 files) | 18 | 50.0 | 3.9 | 7.2 | 8.1 | 0/2 | 45.8 | 43.1 |
| **en** (1/5 files) | 9 | 53.6 | 2.2 | 4.2 | 5.9 | 0/1 | 77.9 | 74.7 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 83.8 | 83.8 | 83.8 | 94.1 | 94.1 | 94.1 |
| a_entity_found | 88.7 | 97.5 | 92.9 | 98.1 | 91.1 | 94.4 |
| a_event_concept | 81.7 | 81.7 | 81.7 | 93.5 | 93.5 | 93.5 |
| a_event_found | 93.2 | 100.0 | 96.5 | 96.9 | 93.9 | 95.4 |
| a_granularity | 96.3 | 97.2 | 96.8 | 98.5 | 98.5 | 98.5 |
| b_event_sense | 96.7 | 96.7 | 96.7 | 80.8 | 80.8 | 80.8 |
| c_aspect | 55.7 | 47.9 | 51.5 | 81.0 | 73.9 | 77.3 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 66.7 | 38.1 | 48.5 | 100.0 | 100.0 | 100.0 |
| c_polarity | 33.3 | 100.0 | 50.0 | – | – | – |
| c_refer | 100.0 | 50.0 | 66.7 | 66.7 | 88.9 | 76.2 |
| d_core_args_abstract | 36.5 | 58.3 | 44.9 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 67.0 | 68.3 | 67.6 | 77.3 | 94.4 | 85.0 |
| d_peripheral_entity | 41.9 | 43.8 | 42.8 | 82.6 | 76.3 | 79.3 |
| d_peripheral_event | 29.9 | 23.7 | 26.4 | 75.0 | 75.0 | 75.0 |
| e_core_labels | 85.7 | 85.7 | 85.7 | 97.3 | 97.3 | 97.3 |
| e_peripheral_labels | 82.7 | 82.7 | 82.7 | 95.7 | 95.7 | 95.7 |
| f_name_tokens | 45.5 | 40.0 | 42.6 | 82.4 | 82.4 | 82.4 |
| f_wiki | – | – | – | 68.8 | 84.6 | 75.9 |
| g_reentrancy | 44.4 | 20.0 | 27.6 | 85.7 | 100.0 | 92.3 |
| h_temporal | 34.7 | 21.8 | 26.8 | 52.6 | 37.0 | 43.5 |
| i_modal | 57.6 | 47.2 | 51.9 | 95.5 | 77.8 | 85.7 |
| j_coref_chain | 31.8 | 6.0 | 10.1 | 100.0 | 61.1 | 75.9 |
| j_coref_subset | – | 0.0 | 0.0 | – | – | – |
| k_doc_format | 99.2 | 99.2 | 99.2 | 100.0 | 100.0 | 100.0 |
