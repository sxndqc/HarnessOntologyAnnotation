# runs/api/a1-sentence-propbank/claude-opus-5-5-v2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 53.7 | 56.5 | 55.1 | 81.8 | no (4) | 75.5 | 74.3 |
| zh-0028 | 12 | 47.6 | 53.5 | 50.4 | 60.3 | yes | 42.7 | 44.8 |
| zh-0032 | 6 | 46.6 | 49.8 | 48.2 | 57.8 | no (3) | 42.9 | 37.6 |
| **zh** (2/15 files) | 18 | 47.1 | 3.7 | 6.9 | 7.9 | 1/2 | 42.8 | 41.2 |
| **en** (1/5 files) | 9 | 53.7 | 2.1 | 4.1 | 5.8 | 0/1 | 75.5 | 74.3 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F | en R | P | F |
|---|---|---|---|---|---|---|
| a_entity_concept | 80.9 | 80.9 | 80.9 | 96.0 | 96.0 | 96.0 |
| a_entity_found | 89.6 | 96.6 | 93.0 | 96.2 | 89.3 | 92.6 |
| a_event_concept | 78.6 | 78.6 | 78.6 | 93.5 | 93.5 | 93.5 |
| a_event_found | 95.5 | 100.0 | 97.7 | 96.9 | 100.0 | 98.4 |
| a_granularity | 97.2 | 98.6 | 97.9 | 97.0 | 95.6 | 96.3 |
| b_event_sense | 98.4 | 98.4 | 98.4 | 80.8 | 80.8 | 80.8 |
| c_aspect | 54.1 | 46.5 | 50.0 | 71.4 | 62.5 | 66.7 |
| c_modstr | – | – | – | – | – | – |
| c_other_attributes | 53.8 | 31.8 | 40.0 | 100.0 | 100.0 | 100.0 |
| c_polarity | 33.3 | 100.0 | 50.0 | – | – | – |
| c_refer | 85.7 | 54.5 | 66.7 | 75.0 | 90.0 | 81.8 |
| d_core_args_abstract | 22.2 | 36.4 | 27.6 | 83.3 | 83.3 | 83.3 |
| d_core_args_event | 68.1 | 63.3 | 65.6 | 65.2 | 79.6 | 71.7 |
| d_peripheral_entity | 43.8 | 41.2 | 42.5 | 81.2 | 81.2 | 81.2 |
| d_peripheral_event | 36.2 | 33.3 | 34.7 | 87.5 | 70.0 | 77.8 |
| e_core_labels | 84.0 | 84.0 | 84.0 | 93.9 | 93.9 | 93.9 |
| e_peripheral_labels | 80.8 | 80.8 | 80.8 | 95.8 | 95.8 | 95.8 |
| f_name_tokens | 54.5 | 52.2 | 53.3 | 93.8 | 100.0 | 96.8 |
| f_wiki | – | 0.0 | 0.0 | 60.0 | 81.8 | 69.2 |
| g_reentrancy | 38.9 | 19.4 | 25.9 | 64.3 | 81.8 | 72.0 |
| h_temporal | 39.8 | 26.7 | 32.0 | 63.2 | 44.4 | 52.2 |
| i_modal | 59.7 | 46.2 | 52.1 | 95.5 | 75.0 | 84.0 |
| j_coref_chain | 52.3 | 9.4 | 16.0 | 100.0 | 57.9 | 73.3 |
| j_coref_subset | – | 0.0 | 0.0 | – | – | – |
| k_doc_format | 98.5 | 98.5 | 98.5 | 98.9 | 98.9 | 98.9 |
