# rsi/runs/s1-abridged-rules-claude-opus-5-5/test/after-b2

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 48.0 | 53.9 | 50.8 | 61.9 | yes | 44.0 | 47.5 |
| zh-0032 | 6 | 48.3 | 49.2 | 48.8 | 56.9 | yes | 41.1 | 38.0 |
| **zh** (2/15 files) | 18 | 48.2 | 3.7 | 6.9 | 7.9 | 2/2 | 42.6 | 42.7 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 80.7 | 80.7 | 80.7 |
| a_entity_found | 93.2 | 95.4 | 94.3 |
| a_event_concept | 75.3 | 75.3 | 75.3 |
| a_event_found | 96.6 | 97.7 | 97.1 |
| a_granularity | 97.3 | 98.6 | 98.0 |
| b_event_sense | 88.3 | 88.3 | 88.3 |
| c_aspect | 50.8 | 44.9 | 47.7 |
| c_modstr | – | – | – |
| c_other_attributes | 64.3 | 36.0 | 46.2 |
| c_polarity | 33.3 | 100.0 | 50.0 |
| c_refer | 71.4 | 55.6 | 62.5 |
| d_core_args_abstract | 10.0 | 16.7 | 12.5 |
| d_core_args_event | 61.3 | 61.3 | 61.3 |
| d_peripheral_entity | 49.3 | 49.3 | 49.3 |
| d_peripheral_event | 35.3 | 28.0 | 31.2 |
| e_core_labels | 73.8 | 73.8 | 73.8 |
| e_peripheral_labels | 84.7 | 84.7 | 84.7 |
| f_name_tokens | 40.9 | 36.0 | 38.3 |
| f_wiki | – | – | – |
| g_reentrancy | 33.3 | 27.3 | 30.0 |
| h_temporal | 40.7 | 28.6 | 33.6 |
| i_modal | 62.5 | 52.9 | 57.3 |
| j_coref_chain | 54.5 | 10.9 | 18.2 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
