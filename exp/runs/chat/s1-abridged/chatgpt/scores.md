# runs/chat/s1-abridged/chatgpt

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (per check: recall and precision of its units pooled over the files) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp |
|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 47.0 | 46.1 | 46.5 | 69.5 | no (1) | 58.0 | 58.4 |
| **en** (1/5 files) | 9 | 47.0 | 1.8 | 3.4 | 4.8 | 0/1 | 58.0 | 58.4 |

## umrjudge per check (recall / precision / F1)

| check | en R | P | F |
|---|---|---|---|
| a_entity_concept | 86.0 | 86.0 | 86.0 |
| a_entity_found | 96.2 | 90.9 | 93.5 |
| a_event_concept | 82.1 | 82.1 | 82.1 |
| a_event_found | 87.5 | 96.6 | 91.8 |
| a_granularity | 97.0 | 95.6 | 96.3 |
| b_event_sense | 68.2 | 68.2 | 68.2 |
| c_aspect | 61.9 | 59.1 | 60.5 |
| c_modstr | – | – | – |
| c_other_attributes | 100.0 | 100.0 | 100.0 |
| c_polarity | – | – | – |
| c_refer | 90.9 | 90.9 | 90.9 |
| d_core_args_abstract | 77.8 | 77.8 | 77.8 |
| d_core_args_event | 44.3 | 63.3 | 52.2 |
| d_peripheral_entity | 81.2 | 75.0 | 78.0 |
| d_peripheral_event | 75.0 | 50.0 | 60.0 |
| e_core_labels | 75.9 | 75.9 | 75.9 |
| e_peripheral_labels | 95.5 | 95.5 | 95.5 |
| f_name_tokens | 68.8 | 78.6 | 73.3 |
| f_wiki | 33.3 | 100.0 | 50.0 |
| g_reentrancy | 28.6 | 44.4 | 34.8 |
| h_temporal | 47.4 | 33.3 | 39.1 |
| i_modal | 81.8 | 69.2 | 75.0 |
| j_coref_chain | 100.0 | 84.6 | 91.7 |
| j_coref_subset | – | – | – |
| k_doc_format | 100.0 | 100.0 | 100.0 |
