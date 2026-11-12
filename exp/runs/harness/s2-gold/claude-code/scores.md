# runs/harness/s2-gold/claude-code

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 50.9 | 53.9 | 52.4 | 61.0 | no (3) | 46.4 | 47.7 |
| zh-0032 | 6 | 46.2 | 48.3 | 47.2 | 56.4 | yes | 42.7 | 37.1 |
| **zh** (2/15 files) | 18 | 48.4 | 3.7 | 6.9 | 7.7 | 1/2 | 44.5 | 42.4 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 81.9 | 81.9 | 81.9 |
| a_entity_found | 86.9 | 93.7 | 90.2 |
| a_event_concept | 85.4 | 85.4 | 85.4 |
| a_event_found | 93.2 | 98.8 | 95.9 |
| a_granularity | 97.3 | 98.6 | 97.9 |
| b_event_sense | 87.1 | 87.1 | 87.1 |
| c_aspect | 48.3 | 41.4 | 44.6 |
| c_modstr | – | – | – |
| c_other_attributes | 66.7 | 38.1 | 48.5 |
| c_polarity | 50.0 | 100.0 | 66.7 |
| c_refer | 100.0 | 50.0 | 66.7 |
| d_core_args_abstract | 33.3 | 51.5 | 40.5 |
| d_core_args_event | 56.3 | 55.2 | 55.8 |
| d_peripheral_entity | 46.0 | 46.0 | 46.0 |
| d_peripheral_event | 29.5 | 24.2 | 26.6 |
| e_core_labels | 73.5 | 73.5 | 73.5 |
| e_peripheral_labels | 80.4 | 80.4 | 80.4 |
| f_name_tokens | 57.1 | 52.2 | 54.5 |
| f_wiki | – | – | – |
| g_reentrancy | 44.4 | 28.6 | 34.8 |
| h_temporal | 31.9 | 21.6 | 25.8 |
| i_modal | 58.3 | 47.2 | 52.2 |
| j_coref_chain | 27.3 | 4.8 | 8.2 |
| j_coref_subset | – | – | – |
| k_doc_format | 97.2 | 97.2 | 97.2 |
