# runs/chat/s1-abridged/chatgpt

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| en-0008 | 9 | 47.0 | 46.1 | 46.5 | 69.5 | no (1) | 58.0 | 58.4 | 76.0 |
| **en** (1/5 files) | 9 | 47.0 | 1.8 | 3.4 | 4.8 | 0/1 | 58.0 | 58.4 | 76.0 |

## umrjudge per check

| check | en |
|---|---|
| a_entity_concept | 86.0 |
| a_entity_found | 93.5 |
| a_event_concept | 82.1 |
| a_event_found | 91.8 |
| a_granularity | 96.3 |
| b_event_sense | 68.2 |
| c_aspect | 60.5 |
| c_modstr | – |
| c_other_attributes | 100.0 |
| c_polarity | – |
| c_refer | 90.9 |
| d_core_args_abstract | 77.8 |
| d_core_args_event | 52.2 |
| d_peripheral_entity | 78.0 |
| d_peripheral_event | 60.0 |
| e_core_labels | 75.9 |
| e_peripheral_labels | 95.5 |
| f_name_tokens | 73.3 |
| f_wiki | 50.0 |
| g_reentrancy | 34.8 |
| h_temporal | 39.1 |
| i_modal | 75.0 |
| j_coref_chain | 91.7 |
| j_coref_subset | – |
| k_doc_format | 100.0 |
