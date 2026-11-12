# rsi/runs/s1-abridged-rules-claude-opus-5-5/test/after-b3

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 50.4 | 53.5 | 51.9 | 62.5 | yes | 44.1 | 47.8 |
| zh-0032 | 6 | 46.9 | 50.6 | 48.7 | 60.7 | yes | 45.1 | 40.6 |
| **zh** (2/15 files) | 18 | 48.6 | 3.8 | 7.0 | 8.2 | 2/2 | 44.6 | 44.2 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 80.0 | 80.0 | 80.0 |
| a_entity_found | 94.6 | 95.0 | 94.8 |
| a_event_concept | 76.5 | 76.5 | 76.5 |
| a_event_found | 96.6 | 100.0 | 98.3 |
| a_granularity | 97.3 | 97.7 | 97.5 |
| b_event_sense | 88.1 | 88.1 | 88.1 |
| c_aspect | 50.8 | 46.3 | 48.4 |
| c_modstr | – | – | – |
| c_other_attributes | 50.0 | 28.0 | 35.9 |
| c_polarity | 33.3 | 100.0 | 50.0 |
| c_refer | 83.3 | 62.5 | 71.4 |
| d_core_args_abstract | 21.5 | 37.1 | 27.2 |
| d_core_args_event | 57.2 | 55.2 | 56.2 |
| d_peripheral_entity | 46.5 | 44.6 | 45.5 |
| d_peripheral_event | 31.7 | 28.0 | 29.7 |
| e_core_labels | 75.0 | 75.0 | 75.0 |
| e_peripheral_labels | 77.6 | 77.6 | 77.6 |
| f_name_tokens | 64.3 | 56.2 | 60.0 |
| f_wiki | – | – | – |
| g_reentrancy | 22.2 | 40.0 | 28.6 |
| h_temporal | 33.1 | 25.3 | 28.7 |
| i_modal | 61.1 | 53.7 | 57.1 |
| j_coref_chain | 17.9 | 4.4 | 7.0 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
