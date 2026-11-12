# runs/api/a1-sentence-propbank/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 45.1 | 48.2 | 46.6 | 75.8 | no (2) | 64.6 | 62.4 |
| zh-0028 | 12 | 47.7 | 55.3 | 51.2 | 61.4 | no (1) | 45.2 | 43.7 |
| zh-0032 | 6 | 41.8 | 45.7 | 43.7 | 54.1 | no (3) | 37.6 | 32.7 |
| **zh** (2/15 files) | 18 | 44.6 | 3.6 | 6.7 | 7.7 | 0/2 | 41.4 | 38.2 |
| **en** (1/5 files) | 9 | 45.1 | 1.8 | 3.5 | 5.3 | 0/1 | 64.6 | 62.4 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 80.3 | 80.3 | 80.3 | 93.9 | 93.9 | 93.9 |
| a_entity_found | 89.2 | 95.7 | 92.3 | 94.2 | 87.5 | 90.7 |
| a_event_concept | 78.6 | 78.6 | 78.6 | 90.3 | 90.3 | 90.3 |
| a_event_found | 95.5 | 100.0 | 97.7 | 96.9 | 93.9 | 95.4 |
| a_granularity | 96.3 | 98.1 | 97.2 | 97.0 | 95.6 | 96.3 |
| b_event_sense | 96.7 | 96.7 | 96.7 | 80.0 | 80.0 | 80.0 |
| c_aspect | 52.5 | 43.8 | 47.8 | 71.4 | 60.0 | 65.2 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 66.7 | 33.3 | 44.4 | 100.0 | 100.0 | 100.0 |
| c_polarity | 33.3 | 50.0 | 40.0 | – | – | – |
| c_refer | 83.3 | 33.3 | 47.6 | 90.9 | 90.9 | 90.9 |
| d_core_args_abstract | 17.5 | 30.3 | 22.2 | 83.3 | 83.3 | 83.3 |
| d_core_args_event | 64.8 | 62.4 | 63.6 | 59.5 | 77.0 | 67.1 |
| d_peripheral_entity | 41.8 | 42.8 | 42.3 | 70.5 | 77.5 | 73.8 |
| d_peripheral_event | 27.5 | 23.5 | 25.3 | 75.0 | 66.7 | 70.6 |
| e_core_labels | 80.5 | 80.5 | 80.5 | 93.8 | 93.8 | 93.8 |
| e_peripheral_labels | 78.0 | 78.0 | 78.0 | 95.2 | 95.2 | 95.2 |
| f_name_tokens | 42.9 | 34.6 | 38.3 | 68.8 | 73.3 | 71.0 |
| f_wiki | – | – | – | 0.0 | – | 0.0 |
| g_reentrancy | 27.8 | 13.2 | 17.9 | 50.0 | 70.0 | 58.3 |
| h_temporal | 29.7 | 17.2 | 21.7 | 47.4 | 27.3 | 34.6 |
| i_modal | 56.2 | 42.2 | 48.2 | 88.6 | 65.0 | 75.0 |
| j_coref_chain | 28.1 | 4.8 | 8.2 | 100.0 | 57.9 | 73.3 |
| j_coref_subset | – | 0.0 | 0.0 | – | – | – |
| k_doc_format | 99.0 | 99.0 | 99.0 | 100.0 | 100.0 | 100.0 |
