# runs/api/s3-all/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 53.4 | 61.0 | 56.9 | 86.8 | no (3) | 82.5 | 79.2 |
| zh-0028 | 12 | 52.2 | 59.2 | 55.5 | 66.4 | no (2) | 50.0 | 48.5 |
| zh-0032 | 6 | 44.0 | 46.5 | 45.2 | 54.5 | yes | 36.1 | 32.9 |
| **zh** (2/15 files) | 18 | 48.0 | 3.8 | 7.0 | 8.0 | 1/2 | 43.0 | 40.7 |
| **en** (1/5 files) | 9 | 53.4 | 2.3 | 4.4 | 6.3 | 0/1 | 82.5 | 79.2 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 87.9 | 87.9 | 87.9 | 94.1 | 94.1 | 94.1 |
| a_entity_found | 89.2 | 95.7 | 92.3 | 98.1 | 92.7 | 95.3 |
| a_event_concept | 77.5 | 77.5 | 77.5 | 96.8 | 96.8 | 96.8 |
| a_event_found | 90.9 | 100.0 | 95.2 | 96.9 | 93.9 | 95.4 |
| a_granularity | 96.4 | 98.1 | 97.2 | 98.5 | 98.5 | 98.5 |
| b_event_sense | 98.2 | 98.2 | 98.2 | 92.6 | 92.6 | 92.6 |
| c_aspect | 52.5 | 44.3 | 48.1 | 85.7 | 75.0 | 80.0 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 58.3 | 43.8 | 50.0 | 100.0 | 100.0 | 100.0 |
| c_polarity | 66.7 | 100.0 | 80.0 | – | – | – |
| c_refer | 85.7 | 31.6 | 46.2 | 75.0 | 90.0 | 81.8 |
| d_core_args_abstract | 36.1 | 54.2 | 43.3 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 63.0 | 61.8 | 62.4 | 90.9 | 95.2 | 93.0 |
| d_peripheral_entity | 38.8 | 40.5 | 39.6 | 91.7 | 84.6 | 88.0 |
| d_peripheral_event | 28.9 | 22.7 | 25.5 | 75.0 | 85.7 | 80.0 |
| e_core_labels | 88.5 | 88.5 | 88.5 | 100.0 | 100.0 | 100.0 |
| e_peripheral_labels | 76.5 | 76.5 | 76.5 | 95.8 | 95.8 | 95.8 |
| f_name_tokens | 40.0 | 40.0 | 40.0 | 76.5 | 76.5 | 76.5 |
| f_wiki | – | – | – | 100.0 | 94.1 | 97.0 |
| g_reentrancy | 50.0 | 20.0 | 28.6 | 85.7 | 92.3 | 88.9 |
| h_temporal | 38.1 | 23.4 | 29.0 | 73.7 | 48.3 | 58.3 |
| i_modal | 56.2 | 46.0 | 50.6 | 87.9 | 64.4 | 74.4 |
| j_coref_chain | 45.0 | 7.4 | 12.7 | 100.0 | 64.7 | 78.6 |
| j_coref_subset | – | 0.0 | 0.0 | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
