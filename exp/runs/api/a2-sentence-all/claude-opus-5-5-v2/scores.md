# runs/api/a2-sentence-all/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 53.4 | 55.7 | 54.5 | 82.3 | no (4) | 74.4 | 73.7 |
| zh-0028 | 12 | 51.2 | 56.6 | 53.7 | 63.7 | yes | 50.2 | 50.9 |
| zh-0032 | 6 | 46.8 | 49.6 | 48.2 | 58.2 | yes | 44.0 | 39.2 |
| **zh** (2/15 files) | 18 | 48.9 | 3.8 | 7.1 | 8.1 | 2/2 | 47.1 | 45.1 |
| **en** (1/5 files) | 9 | 53.4 | 2.1 | 4.0 | 5.8 | 0/1 | 74.4 | 73.7 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 81.6 | 81.6 | 81.6 | 95.9 | 95.9 | 95.9 |
| a_entity_found | 92.8 | 96.7 | 94.7 | 94.2 | 89.1 | 91.6 |
| a_event_concept | 78.3 | 78.3 | 78.3 | 90.0 | 90.0 | 90.0 |
| a_event_found | 94.3 | 100.0 | 97.1 | 93.8 | 100.0 | 96.8 |
| a_granularity | 97.3 | 98.6 | 97.9 | 98.5 | 98.5 | 98.5 |
| b_event_sense | 98.3 | 98.3 | 98.3 | 87.5 | 87.5 | 87.5 |
| c_aspect | 55.7 | 48.6 | 51.9 | 71.4 | 62.5 | 66.7 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 69.2 | 40.9 | 51.4 | 100.0 | 100.0 | 100.0 |
| c_polarity | 33.3 | 100.0 | 50.0 | – | – | – |
| c_refer | 85.7 | 60.0 | 70.6 | 66.7 | 88.9 | 76.2 |
| d_core_args_abstract | 27.8 | 50.0 | 35.7 | 100.0 | 100.0 | 100.0 |
| d_core_args_event | 69.0 | 64.2 | 66.5 | 72.2 | 79.8 | 75.8 |
| d_peripheral_entity | 50.4 | 48.3 | 49.3 | 70.5 | 64.6 | 67.4 |
| d_peripheral_event | 31.5 | 26.9 | 29.0 | 93.8 | 75.0 | 83.3 |
| e_core_labels | 90.0 | 90.0 | 90.0 | 97.1 | 97.1 | 97.1 |
| e_peripheral_labels | 82.1 | 82.1 | 82.1 | 95.0 | 95.0 | 95.0 |
| f_name_tokens | 64.0 | 55.2 | 59.3 | 100.0 | 100.0 | 100.0 |
| f_wiki | – | 0.0 | 0.0 | 60.0 | 69.2 | 64.3 |
| g_reentrancy | 33.3 | 22.2 | 26.7 | 64.3 | 81.8 | 72.0 |
| h_temporal | 34.7 | 25.9 | 29.7 | 63.2 | 48.0 | 54.5 |
| i_modal | 61.1 | 54.3 | 57.5 | 95.5 | 77.8 | 85.7 |
| j_coref_chain | 63.6 | 10.6 | 18.2 | 100.0 | 61.1 | 75.9 |
| j_coref_subset | – | – | – | – | – | – |
| k_doc_format | 99.6 | 99.6 | 99.6 | 97.6 | 97.6 | 97.6 |
