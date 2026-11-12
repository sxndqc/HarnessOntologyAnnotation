# runs/api/s2-gold/gpt-6.1-sol-medium

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 45.0 | 51.8 | 48.1 | 78.7 | no (3) | 71.2 | 66.9 |
| zh-0028 | 12 | 49.1 | 58.3 | 53.3 | 62.7 | no (1) | 46.1 | 45.8 |
| zh-0032 | 6 | 43.1 | 46.7 | 44.8 | 54.1 | no (2) | 40.6 | 35.4 |
| **zh** (2/15 files) | 18 | 46.0 | 3.8 | 7.0 | 7.9 | 0/2 | 43.3 | 40.6 |
| **en** (1/5 files) | 9 | 45.0 | 2.0 | 3.8 | 5.8 | 0/1 | 71.2 | 66.9 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 81.4 | 81.4 | 81.4 | 96.2 | 96.2 | 96.2 |
| a_entity_found | 91.9 | 94.0 | 92.9 | 100.0 | 91.2 | 95.4 |
| a_event_concept | 77.4 | 77.4 | 77.4 | 81.2 | 81.2 | 81.2 |
| a_event_found | 95.5 | 98.8 | 97.1 | 100.0 | 94.1 | 97.0 |
| a_granularity | 96.4 | 97.3 | 96.8 | 98.5 | 98.5 | 98.5 |
| b_event_sense | 88.1 | 88.1 | 88.1 | 73.9 | 73.9 | 73.9 |
| c_aspect | 51.7 | 43.1 | 47.0 | 66.7 | 53.8 | 59.6 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 57.1 | 34.8 | 43.2 | 100.0 | 100.0 | 100.0 |
| c_polarity | 33.3 | 100.0 | 50.0 | – | – | – |
| c_refer | 100.0 | 46.2 | 63.2 | 84.6 | 100.0 | 91.7 |
| d_core_args_abstract | 19.2 | 34.8 | 24.7 | 86.7 | 86.7 | 86.7 |
| d_core_args_event | 60.1 | 60.1 | 60.1 | 62.9 | 81.4 | 70.9 |
| d_peripheral_entity | 40.4 | 40.4 | 40.4 | 72.9 | 79.5 | 76.1 |
| d_peripheral_event | 31.9 | 23.7 | 27.2 | 66.7 | 66.7 | 66.7 |
| e_core_labels | 75.9 | 75.9 | 75.9 | 91.7 | 91.7 | 91.7 |
| e_peripheral_labels | 76.8 | 76.8 | 76.8 | 90.9 | 90.9 | 90.9 |
| f_name_tokens | 52.2 | 46.2 | 49.0 | 76.5 | 76.5 | 76.5 |
| f_wiki | – | – | – | 81.2 | 81.2 | 81.2 |
| g_reentrancy | 50.0 | 20.9 | 29.5 | 50.0 | 63.6 | 56.0 |
| h_temporal | 36.4 | 22.6 | 27.9 | 47.4 | 27.3 | 34.6 |
| i_modal | 55.6 | 45.5 | 50.0 | 88.6 | 62.9 | 73.6 |
| j_coref_chain | 45.9 | 7.5 | 12.9 | 100.0 | 57.9 | 73.3 |
| j_coref_subset | – | – | – | – | – | – |
| k_doc_format | 99.3 | 99.3 | 99.3 | 100.0 | 100.0 | 100.0 |
