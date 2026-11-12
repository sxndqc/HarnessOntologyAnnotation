# rsi/runs/s1-abridged-rules-claude-opus-5-5/test/v0

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 48.2 | 54.4 | 51.1 | 59.7 | yes | 43.0 | 44.7 |
| zh-0032 | 6 | 48.9 | 45.2 | 47.0 | 54.2 | yes | 38.9 | 36.4 |
| **zh** (2/15 files) | 18 | 48.6 | 3.6 | 6.7 | 7.5 | 2/2 | 40.9 | 40.5 |

## umrjudge per check (recall / precision / F1)

| check | zh R | P | F |
|---|---|---|---|
| a_entity_concept | 78.3 | 78.3 | 78.3 |
| a_entity_found | 91.4 | 97.1 | 94.2 |
| a_event_concept | 78.6 | 78.6 | 78.6 |
| a_event_found | 95.5 | 100.0 | 97.7 |
| a_granularity | 97.2 | 98.6 | 97.9 |
| b_event_sense | 90.0 | 90.0 | 90.0 |
| c_aspect | 49.2 | 42.9 | 45.8 |
| c_modstr | – | – | – |
| c_other_attributes | 57.1 | 33.3 | 42.1 |
| c_polarity | 33.3 | 50.0 | 40.0 |
| c_refer | 85.7 | 33.3 | 48.0 |
| d_core_args_abstract | 25.4 | 43.9 | 32.2 |
| d_core_args_event | 51.9 | 50.9 | 51.4 |
| d_peripheral_entity | 46.1 | 45.1 | 45.6 |
| d_peripheral_event | 27.2 | 21.6 | 24.0 |
| e_core_labels | 70.4 | 70.4 | 70.4 |
| e_peripheral_labels | 80.8 | 80.8 | 80.8 |
| f_name_tokens | 47.8 | 39.3 | 43.1 |
| f_wiki | – | 0.0 | 0.0 |
| g_reentrancy | 38.9 | 29.2 | 33.3 |
| h_temporal | 34.7 | 32.5 | 33.6 |
| i_modal | 56.2 | 65.3 | 60.4 |
| j_coref_chain | 7.7 | 1.5 | 2.6 |
| j_coref_subset | – | 0.0 | 0.0 |
| k_doc_format | 99.5 | 99.5 | 99.5 |
