# runs/harness/s2-gold/claude-code

Shared-task scoring: juːmæʧ (main metric, compare_umr.pl) and Smatch, against the official test gold of UMR 2.2; per language F1 of the counts summed over the files. AnCast++ (mean over files) and umrjudge (mean of its checks) are extra. valid: validate.py --level 2.

| file | sents | juːmæʧ P | R | F | Smatch F | valid | AnCast F | Comp | judge |
|---|---|---|---|---|---|---|---|---|---|
| zh-0028 | 12 | 50.9 | 53.9 | 52.4 | 61.0 | no (3) | 46.4 | 47.7 | 61.6 |
| zh-0032 | 6 | 46.2 | 48.3 | 47.2 | 56.6 | yes | 42.7 | 37.1 | 57.1 |
| **zh** (2/15 files) | 18 | 48.4 | 3.7 | 6.9 | 7.7 | 1/2 | 44.5 | 42.4 | 59.5 |

## umrjudge per check

| check | zh |
|---|---|
| a_entity_concept | 81.8 |
| a_entity_found | 90.3 |
| a_event_concept | 84.1 |
| a_event_found | 95.4 |
| a_granularity | 98.0 |
| b_event_sense | 86.3 |
| c_aspect | 45.7 |
| c_modstr | – |
| c_other_attributes | 47.2 |
| c_polarity | 66.7 |
| c_refer | 35.7 |
| d_core_args_abstract | 32.5 |
| d_core_args_event | 53.9 |
| d_peripheral_entity | 44.2 |
| d_peripheral_event | 30.5 |
| e_core_labels | 73.3 |
| e_peripheral_labels | 77.5 |
| f_name_tokens | 48.5 |
| f_wiki | – |
| g_reentrancy | 29.6 |
| h_temporal | 27.9 |
| i_modal | 54.6 |
| j_coref_chain | 8.0 |
| j_coref_subset | – |
| k_doc_format | 96.9 |
