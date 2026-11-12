# rsi/runs/s1-abridged-examples-claude-opus-5-5/test/after-b4

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 46.3 | 52.2 | 49.1 | 60.8 | yes | 44.4 | 46.2 |
| zh-0032 | 6 | 47.1 | 48.3 | 47.7 | 55.5 | yes | 41.7 | 40.3 |
| **zh** (2/15 files) | 18 | 46.7 | 3.6 | 6.7 | 7.8 | 2/2 | 43.0 | 43.3 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 78.4 | 78.4 | 78.4 |
| a_entity_found | 91.9 | 95.8 | 93.8 |
| a_event_concept | 79.1 | 79.1 | 79.1 |
| a_event_found | 97.7 | 97.7 | 97.7 |
| a_granularity | 95.5 | 96.8 | 96.2 |
| b_event_sense | 88.3 | 88.3 | 88.3 |
| c_aspect | 50.8 | 44.9 | 47.7 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 40.0 | 47.1 |
| c_polarity | 33.3 | 100.0 | 50.0 |
| c_refer | 83.3 | 55.6 | 66.7 |
| d_core_args_abstract | 20.6 | 31.0 | 24.8 |
| d_core_args_event | 64.8 | 64.8 | 64.8 |
| d_peripheral_entity | 41.1 | 45.0 | 43.0 |
| d_peripheral_event | 25.4 | 24.3 | 24.8 |
| e_core_labels | 79.5 | 79.5 | 79.5 |
| e_peripheral_labels | 82.0 | 82.0 | 82.0 |
| f_name_tokens | 52.2 | 46.2 | 49.0 |
| f_wiki | – | – | – |
| g_reentrancy | 44.4 | 24.2 | 31.4 |
| h_temporal | 32.2 | 23.2 | 27.0 |
| i_modal | 70.8 | 58.6 | 64.2 |
| j_coref_chain | 15.2 | 3.3 | 5.4 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
