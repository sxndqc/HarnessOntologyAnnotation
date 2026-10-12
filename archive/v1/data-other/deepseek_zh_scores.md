# experiment/rsi-zh-deepseek: scores

DeepSeek. AnCast++ against gold after Chun & Xue's cleanup; P / R / F are the sentence graphs.
Round Rxy = training document x, iteration y; order R11 R12 R41 R42.

## Training documents (sentence F / comprehensive)

| doc | the seed R0 (vanilla) | before Rx1 | before Rx2 (last reflection) | after Rx2 |
|---|---|---|---|---|
| chinese_umr-0001 | - | 41.7 / 37.6 | 49.2 / 43.9 | - |
| chinese_umr-0004 | - | 35.3 / 32.9 | 40.4 / 37.6 | - |

### chinese_umr-0001

| | P | R | F | Modal | Temporal | Coref | Comprehensive |
|---|---|---|---|---|---|---|---|
| before R11 | 43.8 | 39.7 | 41.7 | 41.7 | 10.1 | 23.6 | 37.6 |
| before R12 (last reflection) | 49.6 | 48.8 | 49.2 | 35.9 | 20.0 | 34.4 | 43.9 |

umrjudge (F per check):

| check | iter1 | iter2 |
|---|---|---|
| a_event_found | 0.944 | 0.952 |
| a_event_concept | 0.736 | 0.817 |
| a_entity_found | 0.931 | 0.942 |
| a_entity_concept | 0.719 | 0.765 |
| a_granularity | 0.801 | 0.782 |
| b_event_sense | 0.812 | 0.888 |
| c_aspect | 0.595 | 0.599 |
| c_modstr | - | - |
| c_polarity | 0.545 | 0.600 |
| c_refer | 0.444 | 0.432 |
| c_other_attributes | 0.537 | 0.595 |
| d_core_args_event | 0.513 | 0.586 |
| d_core_args_abstract | 0.119 | 0.302 |
| d_peripheral_event | 0.287 | 0.338 |
| d_peripheral_entity | 0.410 | 0.489 |
| e_core_labels | 0.846 | 0.870 |
| e_peripheral_labels | 0.804 | 0.825 |
| f_name_tokens | 0.408 | 0.556 |
| f_wiki | - | - |
| g_reentrancy | 0.174 | 0.203 |
| h_temporal | 0.150 | 0.261 |
| i_modal | 0.402 | 0.379 |
| j_coref_chain | 0.289 | 0.324 |
| j_coref_subset | 0.000 | 0.000 |
| k_doc_format | 0.998 | 0.996 |

points lost per skill (sum of 1 - credit over all judge units):

| skill | iter1 | iter2 |
|---|---|---|
| predicate | 490.6 | 600.6 |
| document | 470.2 | 461.4 |
| np_phrase | 449.0 | 469.1 |
| sent_type | 287.0 | 175.0 |
| (no predicted node) | 269.0 | 241.0 |
| special_entity | 152.0 | 123.0 |
| discourse | 21.7 | 12.0 |

### chinese_umr-0004

| | P | R | F | Modal | Temporal | Coref | Comprehensive |
|---|---|---|---|---|---|---|---|
| before R41 | 33.0 | 37.8 | 35.3 | 51.1 | 13.2 | 5.4 | 32.9 |
| before R42 (last reflection) | 38.3 | 42.7 | 40.4 | 55.9 | 15.5 | 8.7 | 37.6 |

umrjudge (F per check):

| check | iter1 | iter2 |
|---|---|---|
| a_event_found | 0.911 | 0.938 |
| a_event_concept | 0.706 | 0.747 |
| a_entity_found | 0.869 | 0.880 |
| a_entity_concept | 0.623 | 0.711 |
| a_granularity | 0.694 | 0.711 |
| b_event_sense | 0.894 | 0.883 |
| c_aspect | 0.603 | 0.613 |
| c_modstr | - | - |
| c_polarity | 0.636 | 0.400 |
| c_refer | 0.622 | 0.494 |
| c_other_attributes | 0.283 | 0.387 |
| d_core_args_event | 0.414 | 0.461 |
| d_core_args_abstract | 0.178 | 0.215 |
| d_peripheral_event | 0.213 | 0.215 |
| d_peripheral_entity | 0.312 | 0.386 |
| e_core_labels | 0.795 | 0.815 |
| e_peripheral_labels | 0.739 | 0.812 |
| f_name_tokens | 0.339 | 0.408 |
| f_wiki | - | - |
| g_reentrancy | 0.168 | 0.178 |
| h_temporal | 0.120 | 0.109 |
| i_modal | 0.513 | 0.558 |
| j_coref_chain | 0.034 | 0.074 |
| j_coref_subset | 0.000 | 0.000 |
| k_doc_format | 0.959 | 0.934 |

points lost per skill (sum of 1 - credit over all judge units):

| skill | iter1 | iter2 |
|---|---|---|
| predicate | 813.4 | 757.5 |
| document | 613.5 | 618.4 |
| np_phrase | 586.5 | 568.3 |
| (no predicted node) | 332.0 | 324.0 |
| sent_type | 301.0 | 269.0 |
| special_entity | 161.0 | 91.2 |
| discourse | 45.7 | 40.7 |

## RSI rounds

| round | problems | of them document level | edits | applied | applied per skill |
|---|---|---|---|---|---|
| R11 | 887 | 263 | 38 | 38 | discourse 8, document 2, np_phrase 10, predicate 11, sent_type 3, special_entity 4 |
| R12 | 877 | 287 | 43 | 42 | discourse 3, document 3, np_phrase 11, predicate 17, sent_type 3, special_entity 5 |
| R41 | 1364 | 290 | 20 | 16 | discourse 3, document 3, np_phrase 2, predicate 2, sent_type 2, special_entity 4 |
| R42 | 1323 | 282 | 17 | 17 | discourse 4, document 1, np_phrase 3, predicate 7, special_entity 2 |

## Test documents 0002+0003+0005+0006+0007, macro average

| | P | R | F | Modal | Temporal | Coref | Comprehensive |
|---|---|---|---|---|---|---|---|
| umr-tree seed, before RSI (R0) | 32.2 | 32.9 | 32.5 | 50.2 | 5.5 | 7.4 | 30.4 |
| umr-tree after R42 | 34.8 | 41.1 | 37.6 | 53.6 | 16.7 | 7.8 | 35.8 |

## Test documents 0005+0006+0007, macro average

| | P | R | F | Modal | Temporal | Coref | Comprehensive |
|---|---|---|---|---|---|---|---|
| umr-tree seed, before RSI (R0) | 29.5 | 32.5 | 30.9 | 47.6 | 6.5 | 8.2 | 29.0 |
| umr-tree after R42 | 32.9 | 40.2 | 36.1 | 50.8 | 12.7 | 8.4 | 34.0 |

### chinese_umr-0002

| | P | R | F | Modal | Temporal | Coref | Comprehensive |
|---|---|---|---|---|---|---|---|
| umr-tree seed, before RSI (R0) | 37.0 | 34.9 | 35.9 | 49.5 | 4.9 | 3.0 | 32.8 |
| umr-tree seed (R0), thinking on | 51.2 | 47.2 | 49.1 | 55.5 | 18.3 | 10.6 | 44.4 |
| umr-tree after R42 | 37.6 | 43.5 | 40.4 | 51.9 | 12.2 | 3.8 | 37.3 |

### chinese_umr-0003

| | P | R | F | Modal | Temporal | Coref | Comprehensive |
|---|---|---|---|---|---|---|---|
| umr-tree seed, before RSI (R0) | 35.5 | 31.9 | 33.6 | 58.5 | 3.3 | 9.6 | 32.0 |
| umr-tree after R42 | 37.6 | 41.4 | 39.4 | 63.8 | 33.1 | 10.0 | 39.6 |

### chinese_umr-0005

| | P | R | F | Modal | Temporal | Coref | Comprehensive |
|---|---|---|---|---|---|---|---|
| umr-tree seed, before RSI (R0) | 30.6 | 33.8 | 32.1 | 57.4 | 9.6 | 7.8 | 31.4 |
| umr-tree after R42 | 33.8 | 41.5 | 37.3 | 65.0 | 14.1 | 8.6 | 37.1 |

### chinese_umr-0006

| | P | R | F | Modal | Temporal | Coref | Comprehensive |
|---|---|---|---|---|---|---|---|
| umr-tree seed, before RSI (R0) | 23.2 | 27.5 | 25.2 | 33.4 | 3.3 | 10.1 | 23.4 |
| umr-tree after R42 | 26.0 | 36.1 | 30.3 | 34.5 | 16.0 | 8.0 | 28.4 |

### chinese_umr-0007

| | P | R | F | Modal | Temporal | Coref | Comprehensive |
|---|---|---|---|---|---|---|---|
| umr-tree seed, before RSI (R0) | 34.7 | 36.2 | 35.4 | 52.0 | 6.7 | 6.6 | 32.3 |
| umr-tree after R42 | 38.8 | 43.1 | 40.9 | 52.9 | 8.1 | 8.7 | 36.6 |

## umrjudge on chinese_umr-0002 (F per check; h-k are document level)

| check | R0 | R0-thinking | R42 |
|---|---|---|---|
| a_event_found | 0.959 | 0.970 | 0.912 |
| a_event_concept | 0.702 | 0.772 | 0.757 |
| a_entity_found | 0.904 | 0.935 | 0.905 |
| a_entity_concept | 0.574 | 0.691 | 0.669 |
| a_granularity | 0.729 | 0.830 | 0.715 |
| b_event_sense | 0.749 | 0.738 | 0.842 |
| c_aspect | 0.546 | 0.614 | 0.628 |
| c_modstr | - | - | - |
| c_polarity | 0.667 | 0.588 | 0.706 |
| c_refer | 0.448 | 0.571 | 0.500 |
| c_other_attributes | 0.472 | 0.591 | 0.403 |
| d_core_args_event | 0.401 | 0.535 | 0.426 |
| d_core_args_abstract | 0.097 | 0.153 | 0.118 |
| d_peripheral_event | 0.232 | 0.402 | 0.231 |
| d_peripheral_entity | 0.266 | 0.457 | 0.330 |
| e_core_labels | 0.815 | 0.843 | 0.846 |
| e_peripheral_labels | 0.731 | 0.839 | 0.812 |
| f_name_tokens | 0.533 | 0.562 | 0.502 |
| f_wiki | - | - | - |
| g_reentrancy | 0.201 | 0.275 | 0.216 |
| h_temporal | 0.068 | 0.145 | 0.130 |
| i_modal | 0.499 | 0.554 | 0.523 |
| j_coref_chain | 0.048 | 0.108 | 0.045 |
| j_coref_subset | 0.000 | 0.000 | 0.000 |
| k_doc_format | 0.917 | 1.000 | 0.940 |

## umrjudge on chinese_umr-0003 (F per check; h-k are document level)

| check | R0 | R42 |
|---|---|---|
| a_event_found | 0.931 | 0.960 |
| a_event_concept | 0.674 | 0.735 |
| a_entity_found | 0.893 | 0.918 |
| a_entity_concept | 0.620 | 0.669 |
| a_granularity | 0.702 | 0.707 |
| b_event_sense | 0.914 | 0.944 |
| c_aspect | 0.586 | 0.643 |
| c_modstr | - | - |
| c_polarity | 0.571 | 0.750 |
| c_refer | 0.444 | 0.667 |
| c_other_attributes | 0.608 | 0.500 |
| d_core_args_event | 0.362 | 0.404 |
| d_core_args_abstract | 0.083 | 0.346 |
| d_peripheral_event | 0.250 | 0.418 |
| d_peripheral_entity | 0.296 | 0.279 |
| e_core_labels | 0.714 | 0.778 |
| e_peripheral_labels | 0.685 | 0.764 |
| f_name_tokens | 0.426 | 0.317 |
| f_wiki | - | - |
| g_reentrancy | 0.171 | 0.173 |
| h_temporal | 0.061 | 0.320 |
| i_modal | 0.596 | 0.633 |
| j_coref_chain | 0.100 | 0.061 |
| j_coref_subset | 0.000 | 0.000 |
| k_doc_format | 0.949 | 0.907 |

## umrjudge on chinese_umr-0005 (F per check; h-k are document level)

| check | R0 | R42 |
|---|---|---|
| a_event_found | 0.939 | 0.919 |
| a_event_concept | 0.714 | 0.799 |
| a_entity_found | 0.863 | 0.861 |
| a_entity_concept | 0.593 | 0.676 |
| a_granularity | 0.657 | 0.685 |
| b_event_sense | 0.827 | 0.864 |
| c_aspect | 0.582 | 0.562 |
| c_modstr | - | - |
| c_polarity | 0.556 | 0.706 |
| c_refer | 0.821 | 0.872 |
| c_other_attributes | 0.569 | 0.580 |
| d_core_args_event | 0.407 | 0.470 |
| d_core_args_abstract | 0.078 | 0.111 |
| d_peripheral_event | 0.202 | 0.291 |
| d_peripheral_entity | 0.189 | 0.237 |
| e_core_labels | 0.752 | 0.842 |
| e_peripheral_labels | 0.611 | 0.784 |
| f_name_tokens | 0.244 | 0.115 |
| f_wiki | - | - |
| g_reentrancy | 0.227 | 0.329 |
| h_temporal | 0.076 | 0.162 |
| i_modal | 0.581 | 0.653 |
| j_coref_chain | 0.051 | 0.051 |
| j_coref_subset | - | - |
| k_doc_format | 0.937 | 0.923 |

## umrjudge on chinese_umr-0006 (F per check; h-k are document level)

| check | R0 | R42 |
|---|---|---|
| a_event_found | 0.844 | 0.869 |
| a_event_concept | 0.684 | 0.717 |
| a_entity_found | 0.879 | 0.831 |
| a_entity_concept | 0.579 | 0.634 |
| a_granularity | 0.645 | 0.631 |
| b_event_sense | 0.775 | 0.870 |
| c_aspect | 0.412 | 0.563 |
| c_modstr | - | - |
| c_polarity | 0.000 | 0.500 |
| c_refer | 0.143 | 0.235 |
| c_other_attributes | 0.457 | 0.452 |
| d_core_args_event | 0.319 | 0.313 |
| d_core_args_abstract | 0.068 | 0.111 |
| d_peripheral_event | 0.158 | 0.119 |
| d_peripheral_entity | 0.212 | 0.216 |
| e_core_labels | 0.706 | 0.778 |
| e_peripheral_labels | 0.727 | 0.764 |
| f_name_tokens | 0.381 | 0.356 |
| f_wiki | - | - |
| g_reentrancy | 0.191 | 0.110 |
| h_temporal | 0.077 | 0.107 |
| i_modal | 0.338 | 0.349 |
| j_coref_chain | 0.058 | 0.075 |
| j_coref_subset | - | - |
| k_doc_format | 0.937 | 0.918 |

## umrjudge on chinese_umr-0007 (F per check; h-k are document level)

| check | R0 | R42 |
|---|---|---|
| a_event_found | 0.921 | 0.939 |
| a_event_concept | 0.673 | 0.738 |
| a_entity_found | 0.874 | 0.895 |
| a_entity_concept | 0.608 | 0.801 |
| a_granularity | 0.752 | 0.730 |
| b_event_sense | 0.878 | 0.886 |
| c_aspect | 0.494 | 0.568 |
| c_modstr | - | - |
| c_polarity | - | - |
| c_refer | 0.545 | 0.643 |
| c_other_attributes | 0.607 | 0.530 |
| d_core_args_event | 0.398 | 0.512 |
| d_core_args_abstract | 0.118 | 0.248 |
| d_peripheral_event | 0.249 | 0.292 |
| d_peripheral_entity | 0.330 | 0.298 |
| e_core_labels | 0.743 | 0.805 |
| e_peripheral_labels | 0.722 | 0.711 |
| f_name_tokens | 0.428 | 0.185 |
| f_wiki | - | - |
| g_reentrancy | 0.130 | 0.204 |
| h_temporal | 0.107 | 0.107 |
| i_modal | 0.524 | 0.537 |
| j_coref_chain | 0.050 | 0.070 |
| j_coref_subset | 0.000 | 0.000 |
| k_doc_format | 0.945 | 0.928 |
