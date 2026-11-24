# Comparison points: agreement, accuracy, voting

Four groups: (A) the 30 test files with all 8 systems; (B) the test files by language; (C) all 48 documents with the 6 systems that ran on all of them; (D) the 31 Chinese documents with those 6 (the group of the first round).


# A. Test set, 8 systems

Systems: s0/r1, s0/r2, s1f/r1, s1f/r2, s3/r1, s3/r2, a2/r1, a2/r2. 8364 points in 30 documents (arp-0003, arp-0005, cs-0000, cs-0001, cs-0002, cs-0003, cs-0004, en-0000, en-0005, en-0006, en-0007, en-0008, it-0000, la-0001, nv-0004, zh-0021, zh-0022, zh-0023, zh-0024, zh-0026, zh-0027, zh-0028, zh-0029, zh-0030, zh-0031, zh-0032, zh-0033, zh-0034, zh-0035, zh-0036); 2407 where the gold should change.

## 1. Agreement between systems (6894 points where the systems differ)

| | s0/r1 | s0/r2 | s1f/r1 | s1f/r2 | s3/r1 | s3/r2 | a2/r1 | a2/r2 | gold |
|---|---|---|---|---|---|---|---|---|---|
| **s0/r1** | – | 69 | 40 | 38 | 31 | 31 | 23 | 21 | 20 |
| **s0/r2** | 69 | – | 40 | 39 | 32 | 31 | 22 | 21 | 21 |
| **s1f/r1** | 40 | 40 | – | 68 | 49 | 48 | 38 | 36 | 25 |
| **s1f/r2** | 38 | 39 | 68 | – | 49 | 48 | 38 | 36 | 23 |
| **s3/r1** | 31 | 32 | 49 | 49 | – | 69 | 56 | 54 | 30 |
| **s3/r2** | 31 | 31 | 48 | 48 | 69 | – | 56 | 55 | 30 |
| **a2/r1** | 23 | 22 | 38 | 38 | 56 | 56 | – | 78 | 30 |
| **a2/r2** | 21 | 21 | 36 | 36 | 54 | 55 | 78 | – | 30 |

Pairs from closest to farthest: a2/r1 ~ a2/r2 78; s3/r1 ~ s3/r2 69; s0/r1 ~ s0/r2 69; s1f/r1 ~ s1f/r2 68; s3/r2 ~ a2/r1 56; s3/r1 ~ a2/r1 56; s3/r2 ~ a2/r2 55; s3/r1 ~ a2/r2 54; s1f/r2 ~ s3/r1 49; s1f/r1 ~ s3/r1 49; s1f/r1 ~ s3/r2 48; s1f/r2 ~ s3/r2 48; s0/r2 ~ s1f/r1 40; s0/r1 ~ s1f/r1 40; s0/r2 ~ s1f/r2 39; s0/r1 ~ s1f/r2 38; s1f/r2 ~ a2/r1 38; s1f/r1 ~ a2/r1 38; s1f/r2 ~ a2/r2 36; s1f/r1 ~ a2/r2 36; s0/r2 ~ s3/r1 32; s0/r2 ~ s3/r2 31; s0/r1 ~ s3/r1 31; s0/r1 ~ s3/r2 31; s0/r1 ~ a2/r1 23; s0/r2 ~ a2/r1 22; s0/r1 ~ a2/r2 21; s0/r2 ~ a2/r2 21

| pairs | mean agreement |
|---|---|
| same condition, the two runs | 71.0 |
| different conditions, same run | 38.7 |
| different conditions, different runs | 38.8 |
| s0: r1 ~ r2 | 68.8 |
| s1f: r1 ~ r2 | 68.0 |
| s3: r1 ~ r2 | 69.2 |
| a2: r1 ~ r2 | 77.9 |
| within run r1 | 39.3 |
| within run r2 | 38.2 |

Mean agreement with the other systems: s0/r1 36.1, s0/r2 36.3, s1f/r1 45.3, s1f/r2 45.1, s3/r1 48.5, s3/r2 48.2, a2/r1 44.4, a2/r2 43.0

| category | points | mean number of different choices | mean pairwise agreement |
|---|---|---|---|
| sense | 331 | 2.5 | 43.2 |
| role | 1283 | 2.8 | 41.5 |
| concept | 1108 | 2.7 | 45.6 |
| structure | 1501 | 3.0 | 39.8 |
| attr | 1011 | 2.5 | 47.9 |
| doc-temporal | 615 | 3.1 | 41.3 |
| doc-modal | 471 | 2.9 | 42.6 |
| doc-coref | 574 | 2.6 | 47.4 |

How often a system is alone with its choice: s0/r1 1045, s0/r2 1037, s1f/r1 735, s1f/r2 758, s3/r1 552, s3/r2 602, a2/r1 515, a2/r2 645

## 2. Accuracy at the points (ok / (ok + minor + bad); open points left out)

| annotation | ok % | bad % | ok | minor | bad | open |
|---|---|---|---|---|---|---|
| gold | 55.9 | 18.0 | 4620 | 2150 | 1488 | 106 |
| s0/r1 | 60.2 | 9.2 | 4827 | 2452 | 735 | 350 |
| s0/r2 | 59.6 | 9.4 | 4761 | 2481 | 750 | 372 |
| s1f/r1 | 72.5 | 5.0 | 5960 | 1852 | 408 | 144 |
| s1f/r2 | 72.1 | 5.4 | 5927 | 1848 | 442 | 147 |
| s3/r1 | 83.6 | 1.6 | 6901 | 1221 | 134 | 108 |
| s3/r2 | 83.5 | 1.6 | 6898 | 1224 | 136 | 106 |
| a2/r1 | 81.2 | 3.1 | 6689 | 1293 | 253 | 129 |
| a2/r2 | 80.1 | 3.7 | 6593 | 1327 | 308 | 136 |

ok % by category:

| annotation | sense (431) | role (1548) | concept (1406) | structure (1754) | attr (1252) | doc-temporal (663) | doc-modal (560) | doc-coref (750) |
|---|---|---|---|---|---|---|---|---|
| gold | 65.0 | 61.9 | 62.3 | 60.2 | 55.5 | 38.1 | 44.3 | 40.8 |
| s0/r1 | 45.4 | 62.6 | 59.2 | 57.4 | 71.6 | 32.0 | 61.8 | 74.2 |
| s0/r2 | 44.8 | 61.6 | 60.1 | 56.7 | 71.3 | 28.8 | 63.4 | 69.8 |
| s1f/r1 | 53.6 | 66.8 | 73.1 | 65.0 | 78.4 | 91.7 | 80.3 | 79.7 |
| s1f/r2 | 48.9 | 66.5 | 73.9 | 66.2 | 78.0 | 88.2 | 74.6 | 82.5 |
| s3/r1 | 91.1 | 86.0 | 78.0 | 77.6 | 83.4 | 94.1 | 87.6 | 86.9 |
| s3/r2 | 91.8 | 86.7 | 78.6 | 78.3 | 83.4 | 92.4 | 85.3 | 85.1 |
| a2/r1 | 94.1 | 84.6 | 77.2 | 77.5 | 81.9 | 93.6 | 72.4 | 77.4 |
| a2/r2 | 92.0 | 84.1 | 76.6 | 76.1 | 81.5 | 89.9 | 70.4 | 77.4 |

Where the gold is wrong (2407 points) and where it is right (4620 points):

| system | fixes the gold % | repeats the gold's error % | wrong or minor where the gold is right % |
|---|---|---|---|
| s0/r1 | 60.4 | 5.6 | 42.8 |
| s0/r2 | 59.7 | 5.3 | 43.2 |
| s1f/r1 | 79.9 | 3.4 | 32.1 |
| s1f/r2 | 80.3 | 3.6 | 33.5 |
| s3/r1 | 88.6 | 2.2 | 19.2 |
| s3/r2 | 88.7 | 2.1 | 19.6 |
| a2/r1 | 86.3 | 3.1 | 22.4 |
| a2/r2 | 84.8 | 3.6 | 23.1 |

## 3. Voting (strict majority; a flag = the vote differs from the gold)

| set | systems | votes needed | vote ok % | no decision | flags | good | harm | neutral | flag precision % | gold errors caught % |
|---|---|---|---|---|---|---|---|---|---|---|
| all | s0/r1 + s0/r2 + s1f/r1 + s1f/r2 + s3/r1 + s3/r2 + a2/r1 + a2/r2 | 5 | 90.0 | 2896 | 4032 | 2411 | 385 | 1236 | 60 | 100 |
| all, unanimous | s0/r1 + s0/r2 + s1f/r1 + s1f/r2 + s3/r1 + s3/r2 + a2/r1 + a2/r2 | 8 | 93.9 | 6894 | 1443 | 1035 | 72 | 336 | 72 | 43 |
| run r1 | s0/r1 + s1f/r1 + s3/r1 + a2/r1 | 3 | 90.4 | 3469 | 3666 | 2226 | 334 | 1106 | 61 | 92 |
| run r2 | s0/r2 + s1f/r2 + s3/r2 + a2/r2 | 3 | 90.4 | 3514 | 3650 | 2228 | 331 | 1091 | 61 | 93 |
| without s0 | s1f/r1 + s1f/r2 + s3/r1 + s3/r2 + a2/r1 + a2/r2 | 4 | 91.4 | 2207 | 4464 | 2680 | 382 | 1402 | 60 | 111 |
| only s0 | s0/r1 + s0/r2 | 2 | 64.6 | 2149 | 5117 | 1886 | 1442 | 1789 | 37 | 78 |
| without s1f | s0/r1 + s0/r2 + s3/r1 + s3/r2 + a2/r1 + a2/r2 | 4 | 91.8 | 2641 | 4081 | 2505 | 327 | 1249 | 61 | 104 |
| only s1f | s1f/r1 + s1f/r2 | 2 | 77.4 | 2207 | 4917 | 2365 | 991 | 1561 | 48 | 98 |
| without s3 | s0/r1 + s0/r2 + s1f/r1 + s1f/r2 + a2/r1 + a2/r2 | 4 | 83.6 | 2905 | 4128 | 2249 | 646 | 1233 | 54 | 93 |
| only s3 | s3/r1 + s3/r2 | 2 | 89.7 | 2123 | 4597 | 2674 | 452 | 1471 | 58 | 111 |
| without a2 | s0/r1 + s0/r2 + s1f/r1 + s1f/r2 + s3/r1 + s3/r2 | 4 | 83.1 | 2533 | 4441 | 2368 | 695 | 1378 | 53 | 98 |
| only a2 | a2/r1 + a2/r2 | 2 | 85.0 | 1523 | 5089 | 2722 | 714 | 1653 | 53 | 113 |
| single | s0/r1 | 1 | 60.2 | 0 | 6928 | 2232 | 2179 | 2517 | 32 | 93 |
| single | s0/r2 | 1 | 59.6 | 0 | 6923 | 2197 | 2209 | 2517 | 32 | 91 |
| single | s1f/r1 | 1 | 72.5 | 0 | 6642 | 2825 | 1564 | 2253 | 43 | 117 |
| single | s1f/r2 | 1 | 72.1 | 0 | 6734 | 2854 | 1627 | 2253 | 42 | 119 |
| single | s3/r1 | 1 | 83.6 | 0 | 6250 | 3135 | 913 | 2202 | 50 | 130 |
| single | s3/r2 | 1 | 83.5 | 0 | 6280 | 3156 | 932 | 2192 | 50 | 131 |
| single | a2/r1 | 1 | 81.2 | 0 | 6271 | 3085 | 1087 | 2099 | 49 | 128 |
| single | a2/r2 | 1 | 80.1 | 0 | 6271 | 3022 | 1131 | 2118 | 48 | 126 |

Best sets of 2 by gold errors caught (then less harm):

| set | systems | votes needed | vote ok % | no decision | flags | good | harm | neutral | flag precision % | gold errors caught % |
|---|---|---|---|---|---|---|---|---|---|---|
| size 2 | a2/r1 + a2/r2 | 2 | 85.0 | 1523 | 5089 | 2722 | 714 | 1653 | 53 | 113 |
| size 2 | s3/r1 + s3/r2 | 2 | 89.7 | 2123 | 4597 | 2674 | 452 | 1471 | 58 | 111 |
| size 2 | s3/r2 + a2/r1 | 2 | 92.0 | 3025 | 3926 | 2450 | 306 | 1170 | 62 | 102 |
| size 2 | s3/r1 + a2/r1 | 2 | 92.0 | 3061 | 3885 | 2416 | 302 | 1167 | 62 | 100 |
| size 2 | s3/r2 + a2/r2 | 2 | 92.4 | 3136 | 3845 | 2396 | 291 | 1158 | 62 | 100 |
| size 2 | s3/r1 + a2/r2 | 2 | 92.2 | 3173 | 3792 | 2372 | 288 | 1132 | 63 | 99 |

Best sets of 3 by gold errors caught (then less harm):

| set | systems | votes needed | vote ok % | no decision | flags | good | harm | neutral | flag precision % | gold errors caught % |
|---|---|---|---|---|---|---|---|---|---|---|
| size 3 | s3/r1 + s3/r2 + a2/r1 | 2 | 87.7 | 631 | 5680 | 3096 | 670 | 1914 | 55 | 129 |
| size 3 | s3/r1 + s3/r2 + a2/r2 | 2 | 87.7 | 634 | 5672 | 3088 | 663 | 1921 | 54 | 128 |
| size 3 | s3/r1 + a2/r1 + a2/r2 | 2 | 84.8 | 405 | 5836 | 3060 | 834 | 1942 | 52 | 127 |
| size 3 | s3/r2 + a2/r1 + a2/r2 | 2 | 84.8 | 428 | 5830 | 3056 | 833 | 1941 | 52 | 127 |
| size 3 | s1f/r1 + s3/r1 + s3/r2 | 2 | 87.5 | 687 | 5626 | 3051 | 657 | 1918 | 54 | 127 |
| size 3 | s1f/r2 + s3/r1 + s3/r2 | 2 | 87.1 | 684 | 5652 | 3034 | 676 | 1942 | 54 | 126 |

Best sets of 4 by gold errors caught (then less harm):

| set | systems | votes needed | vote ok % | no decision | flags | good | harm | neutral | flag precision % | gold errors caught % |
|---|---|---|---|---|---|---|---|---|---|---|
| size 4 | s1f/r1 + s3/r1 + s3/r2 + a2/r1 | 3 | 91.7 | 2316 | 4403 | 2674 | 356 | 1373 | 61 | 111 |
| size 4 | s3/r1 + s3/r2 + a2/r1 + a2/r2 | 3 | 91.3 | 2308 | 4400 | 2652 | 379 | 1369 | 60 | 110 |
| size 4 | s1f/r2 + s3/r1 + s3/r2 + a2/r1 | 3 | 91.3 | 2313 | 4417 | 2649 | 375 | 1393 | 60 | 110 |
| size 4 | s1f/r1 + s3/r1 + s3/r2 + a2/r2 | 3 | 91.7 | 2329 | 4380 | 2644 | 357 | 1379 | 60 | 110 |
| size 4 | s1f/r2 + s3/r1 + s3/r2 + a2/r2 | 3 | 91.3 | 2319 | 4397 | 2627 | 373 | 1397 | 60 | 109 |
| size 4 | s1f/r1 + s3/r2 + a2/r1 + a2/r2 | 3 | 91.6 | 2591 | 4191 | 2576 | 355 | 1260 | 61 | 107 |

Gold errors for which at least one system has a correct different choice: 2347 of 2407.


# Test set by language: ok % at the points (ok / (ok + minor + bad))

| annotation | zh (2717) | en (1430) | cs (1582) | it (629) | la (482) | arp (376) | nv (1148) | all |
|---|---|---|---|---|---|---|---|---|
| gold | 45.2 | 52.7 | 62.7 | 55.1 | 72.9 | 86.6 | 59.9 | 55.9 |
| s0/r1 | 63.2 | 60.2 | 63.5 | 64.7 | 62.4 | 34.2 | 54.2 | 60.2 |
| s0/r2 | 63.1 | 59.5 | 60.6 | 69.2 | 59.4 | 37.1 | 52.3 | 59.6 |
| s1f/r1 | 73.7 | 76.3 | 71.4 | 79.2 | 77.2 | 54.1 | 66.6 | 72.5 |
| s1f/r2 | 72.9 | 76.0 | 71.2 | 80.6 | 77.8 | 50.1 | 66.8 | 72.1 |
| s3/r1 | 90.5 | 87.5 | 80.8 | 80.4 | 79.4 | 60.6 | 76.9 | 83.6 |
| s3/r2 | 89.5 | 89.6 | 82.2 | 85.8 | 72.8 | 63.0 | 73.1 | 83.5 |
| a2/r1 | 86.3 | 90.1 | 76.7 | 87.7 | 65.8 | 62.5 | 72.9 | 81.2 |
| a2/r2 | 85.1 | 89.3 | 74.3 | 87.8 | 66.4 | 60.8 | 72.4 | 80.1 |

bad % by language:

| annotation | zh | en | cs | it | la | arp | nv | all |
|---|---|---|---|---|---|---|---|---|
| gold | 27.8 | 19.4 | 10.2 | 11.9 | 7.8 | 5.1 | 15.4 | 18.0 |
| s0/r1 | 12.2 | 11.0 | 3.4 | 3.2 | 5.7 | 21.8 | 8.9 | 9.2 |
| s0/r2 | 12.4 | 10.8 | 3.4 | 3.4 | 5.7 | 22.7 | 9.9 | 9.4 |
| s1f/r1 | 8.8 | 4.3 | 1.8 | 1.3 | 1.1 | 10.7 | 2.9 | 5.0 |
| s1f/r2 | 9.4 | 4.7 | 1.7 | 0.8 | 1.7 | 11.2 | 4.0 | 5.4 |
| s3/r1 | 0.6 | 0.6 | 1.4 | 1.0 | 2.3 | 10.0 | 2.9 | 1.6 |
| s3/r2 | 1.0 | 0.5 | 1.4 | 0.2 | 2.5 | 7.0 | 3.8 | 1.6 |
| a2/r1 | 2.8 | 0.6 | 2.8 | 0.3 | 4.2 | 11.2 | 5.7 | 3.1 |
| a2/r2 | 3.6 | 0.9 | 3.1 | 1.1 | 4.4 | 13.2 | 6.8 | 3.7 |

Points where the gold should change, by language: zh 1171 of 2717, en 430 of 1430, cs 324 of 1582, it 160 of 629, la 69 of 482, arp 32 of 376, nv 221 of 1148


# C. All documents, 6 systems (no baseline)

Systems: s1f/r1, s1f/r2, s3/r1, s3/r2, a2/r1, a2/r2. 14674 points in 48 documents (arp-0003, arp-0005, cs-0000, cs-0001, cs-0002, cs-0003, cs-0004, en-0000, en-0005, en-0006, en-0007, en-0008, it-0000, la-0001, nv-0004, zh-0001, zh-0002, zh-0003, zh-0004, zh-0005, zh-0006, zh-0007, zh-0008, zh-0009, zh-0010, zh-0011, zh-0012, zh-0013, zh-0014, zh-0015, zh-0016, zh-0017, zh-0018, zh-0021, zh-0022, zh-0023, zh-0024, zh-0026, zh-0027, zh-0028, zh-0029, zh-0030, zh-0031, zh-0032, zh-0033, zh-0034, zh-0035, zh-0036); 4957 where the gold should change.

## 1. Agreement between systems (10432 points where the systems differ)

| | s1f/r1 | s1f/r2 | s3/r1 | s3/r2 | a2/r1 | a2/r2 | gold |
|---|---|---|---|---|---|---|---|
| **s1f/r1** | – | 61 | 40 | 39 | 26 | 24 | 21 |
| **s1f/r2** | 61 | – | 39 | 38 | 26 | 23 | 20 |
| **s3/r1** | 40 | 39 | – | 66 | 48 | 45 | 29 |
| **s3/r2** | 39 | 38 | 66 | – | 49 | 46 | 29 |
| **a2/r1** | 26 | 26 | 48 | 49 | – | 75 | 31 |
| **a2/r2** | 24 | 23 | 45 | 46 | 75 | – | 32 |

Pairs from closest to farthest: a2/r1 ~ a2/r2 75; s3/r1 ~ s3/r2 66; s1f/r1 ~ s1f/r2 61; s3/r2 ~ a2/r1 49; s3/r1 ~ a2/r1 48; s3/r2 ~ a2/r2 46; s3/r1 ~ a2/r2 45; s1f/r1 ~ s3/r1 40; s1f/r2 ~ s3/r1 39; s1f/r1 ~ s3/r2 39; s1f/r2 ~ s3/r2 38; s1f/r1 ~ a2/r1 26; s1f/r2 ~ a2/r1 26; s1f/r1 ~ a2/r2 24; s1f/r2 ~ a2/r2 23

| pairs | mean agreement |
|---|---|
| same condition, the two runs | 67.4 |
| different conditions, same run | 36.8 |
| different conditions, different runs | 36.9 |
| s1f: r1 ~ r2 | 61.3 |
| s3: r1 ~ r2 | 65.6 |
| a2: r1 ~ r2 | 75.4 |
| within run r1 | 37.8 |
| within run r2 | 35.9 |

Mean agreement with the other systems: s1f/r1 37.8, s1f/r2 37.6, s3/r1 47.5, s3/r2 47.4, a2/r1 44.7, a2/r2 42.8

| category | points | mean number of different choices | mean pairwise agreement |
|---|---|---|---|
| sense | 694 | 2.4 | 43.9 |
| role | 1943 | 2.5 | 42.7 |
| concept | 1520 | 2.4 | 44.0 |
| structure | 2317 | 2.7 | 40.0 |
| attr | 1293 | 2.4 | 45.8 |
| doc-temporal | 830 | 2.6 | 44.1 |
| doc-modal | 931 | 2.6 | 41.1 |
| doc-coref | 904 | 2.3 | 45.9 |

How often a system is alone with its choice: s1f/r1 1968, s1f/r2 2050, s3/r1 1238, s3/r2 1290, a2/r1 987, a2/r2 1278

## 2. Accuracy at the points (ok / (ok + minor + bad); open points left out)

| annotation | ok % | bad % | ok | minor | bad | open |
|---|---|---|---|---|---|---|
| gold | 51.5 | 22.3 | 7480 | 3806 | 3248 | 140 |
| s1f/r1 | 72.1 | 7.2 | 10443 | 2994 | 1043 | 194 |
| s1f/r2 | 72.0 | 7.4 | 10410 | 2980 | 1071 | 213 |
| s3/r1 | 85.5 | 1.3 | 12427 | 1907 | 194 | 146 |
| s3/r2 | 85.8 | 1.2 | 12475 | 1887 | 172 | 140 |
| a2/r1 | 82.8 | 3.2 | 12010 | 2040 | 462 | 162 |
| a2/r2 | 81.4 | 3.9 | 11803 | 2142 | 561 | 168 |

ok % by category:

| annotation | sense (910) | role (2575) | concept (2229) | structure (3025) | attr (1950) | doc-temporal (1333) | doc-modal (1218) | doc-coref (1434) |
|---|---|---|---|---|---|---|---|---|
| gold | 64.3 | 58.9 | 60.0 | 56.3 | 52.5 | 30.6 | 38.9 | 34.4 |
| s1f/r1 | 47.1 | 64.1 | 75.1 | 67.5 | 79.1 | 88.9 | 73.4 | 81.9 |
| s1f/r2 | 45.3 | 64.0 | 73.6 | 68.5 | 78.9 | 86.6 | 73.2 | 84.8 |
| s3/r1 | 91.8 | 88.8 | 79.3 | 80.3 | 83.8 | 93.2 | 89.6 | 88.4 |
| s3/r2 | 91.3 | 89.6 | 80.7 | 81.1 | 84.4 | 92.8 | 88.2 | 87.4 |
| a2/r1 | 94.5 | 87.4 | 79.5 | 80.7 | 83.2 | 93.9 | 70.6 | 75.7 |
| a2/r2 | 93.0 | 86.9 | 78.3 | 78.9 | 82.7 | 89.9 | 67.2 | 76.1 |

Where the gold is wrong (4957 points) and where it is right (7480 points):

| system | fixes the gold % | repeats the gold's error % | wrong or minor where the gold is right % |
|---|---|---|---|
| s1f/r1 | 80.5 | 3.8 | 34.3 |
| s1f/r2 | 80.5 | 3.6 | 35.0 |
| s3/r1 | 90.3 | 2.3 | 17.6 |
| s3/r2 | 91.0 | 2.0 | 17.7 |
| a2/r1 | 86.1 | 4.2 | 20.2 |
| a2/r2 | 84.0 | 4.8 | 20.8 |

## 3. Voting (strict majority; a flag = the vote differs from the gold)

| set | systems | votes needed | vote ok % | no decision | flags | good | harm | neutral | flag precision % | gold errors caught % |
|---|---|---|---|---|---|---|---|---|---|---|
| all | s1f/r1 + s1f/r2 + s3/r1 + s3/r2 + a2/r1 + a2/r2 | 4 | 92.9 | 3763 | 8183 | 5359 | 559 | 2265 | 65 | 108 |
| all, unanimous | s1f/r1 + s1f/r2 + s3/r1 + s3/r2 + a2/r1 + a2/r2 | 6 | 95.2 | 10432 | 3843 | 2922 | 167 | 754 | 76 | 59 |
| run r1 | s1f/r1 + s3/r1 + a2/r1 | 2 | 90.3 | 1785 | 9672 | 5912 | 853 | 2907 | 61 | 119 |
| run r2 | s1f/r2 + s3/r2 + a2/r2 | 2 | 90.5 | 1903 | 9586 | 5889 | 828 | 2869 | 61 | 119 |
| without s1f | s3/r1 + s3/r2 + a2/r1 + a2/r2 | 3 | 93.0 | 4136 | 7865 | 5197 | 525 | 2143 | 66 | 105 |
| only s1f | s1f/r1 + s1f/r2 | 2 | 77.1 | 4040 | 8883 | 4584 | 1749 | 2550 | 52 | 92 |
| without s3 | s1f/r1 + s1f/r2 + a2/r1 + a2/r2 | 3 | 92.0 | 6467 | 6559 | 4427 | 484 | 1648 | 67 | 89 |
| only s3 | s3/r1 + s3/r2 | 2 | 91.3 | 3593 | 8450 | 5343 | 668 | 2439 | 63 | 108 |
| without a2 | s1f/r1 + s1f/r2 + s3/r1 + s3/r2 | 3 | 90.7 | 4958 | 7779 | 4924 | 623 | 2232 | 63 | 99 |
| only a2 | a2/r1 + a2/r2 | 2 | 85.9 | 2571 | 9026 | 5278 | 1097 | 2651 | 58 | 106 |
| single | s1f/r1 | 1 | 72.1 | 0 | 12100 | 5523 | 2799 | 3778 | 46 | 111 |
| single | s1f/r2 | 1 | 72.0 | 0 | 12210 | 5551 | 2839 | 3820 | 45 | 112 |
| single | s3/r1 | 1 | 85.5 | 0 | 11256 | 6221 | 1361 | 3674 | 55 | 125 |
| single | s3/r2 | 1 | 85.8 | 0 | 11298 | 6282 | 1358 | 3658 | 56 | 127 |
| single | a2/r1 | 1 | 82.8 | 0 | 11059 | 6005 | 1621 | 3433 | 54 | 121 |
| single | a2/r2 | 1 | 81.4 | 0 | 10986 | 5843 | 1699 | 3444 | 53 | 118 |

Best sets of 2 by gold errors caught (then less harm):

| set | systems | votes needed | vote ok % | no decision | flags | good | harm | neutral | flag precision % | gold errors caught % |
|---|---|---|---|---|---|---|---|---|---|---|
| size 2 | s3/r1 + s3/r2 | 2 | 91.3 | 3593 | 8450 | 5343 | 668 | 2439 | 63 | 108 |
| size 2 | a2/r1 + a2/r2 | 2 | 85.9 | 2571 | 9026 | 5278 | 1097 | 2651 | 58 | 106 |
| size 2 | s3/r2 + a2/r1 | 2 | 93.5 | 5350 | 7075 | 4807 | 430 | 1838 | 68 | 97 |
| size 2 | s3/r1 + a2/r1 | 2 | 93.4 | 5459 | 6968 | 4717 | 435 | 1816 | 68 | 95 |
| size 2 | s3/r2 + a2/r2 | 2 | 93.9 | 5615 | 6839 | 4645 | 396 | 1798 | 68 | 94 |
| size 2 | s1f/r1 + s1f/r2 | 2 | 77.1 | 4040 | 8883 | 4584 | 1749 | 2550 | 52 | 92 |

Best sets of 3 by gold errors caught (then less harm):

| set | systems | votes needed | vote ok % | no decision | flags | good | harm | neutral | flag precision % | gold errors caught % |
|---|---|---|---|---|---|---|---|---|---|---|
| size 3 | s3/r1 + s3/r2 + a2/r1 | 2 | 89.9 | 1088 | 10241 | 6155 | 943 | 3143 | 60 | 124 |
| size 3 | s3/r1 + s3/r2 + a2/r2 | 2 | 90.0 | 1115 | 10198 | 6137 | 924 | 3137 | 60 | 124 |
| size 3 | s1f/r1 + s3/r1 + s3/r2 | 2 | 89.2 | 1179 | 10245 | 6077 | 975 | 3193 | 59 | 123 |
| size 3 | s1f/r2 + s3/r1 + s3/r2 | 2 | 89.3 | 1201 | 10233 | 6055 | 973 | 3205 | 59 | 122 |
| size 3 | s3/r1 + a2/r1 + a2/r2 | 2 | 85.9 | 711 | 10347 | 5952 | 1264 | 3131 | 58 | 120 |
| size 3 | s1f/r1 + s3/r2 + a2/r1 | 2 | 90.4 | 1794 | 9658 | 5944 | 843 | 2871 | 62 | 120 |

Best sets of 4 by gold errors caught (then less harm):

| set | systems | votes needed | vote ok % | no decision | flags | good | harm | neutral | flag precision % | gold errors caught % |
|---|---|---|---|---|---|---|---|---|---|---|
| size 4 | s1f/r1 + s3/r1 + s3/r2 + a2/r1 | 3 | 93.0 | 3913 | 8125 | 5345 | 532 | 2248 | 66 | 108 |
| size 4 | s1f/r2 + s3/r1 + s3/r2 + a2/r1 | 3 | 92.9 | 3908 | 8148 | 5334 | 544 | 2270 | 65 | 108 |
| size 4 | s1f/r1 + s3/r1 + s3/r2 + a2/r2 | 3 | 93.0 | 3986 | 8046 | 5274 | 530 | 2242 | 66 | 106 |
| size 4 | s1f/r2 + s3/r1 + s3/r2 + a2/r2 | 3 | 92.9 | 3962 | 8071 | 5273 | 540 | 2258 | 65 | 106 |
| size 4 | s3/r1 + s3/r2 + a2/r1 + a2/r2 | 3 | 93.0 | 4136 | 7865 | 5197 | 525 | 2143 | 66 | 105 |
| size 4 | s1f/r2 + s3/r2 + a2/r1 + a2/r2 | 3 | 93.0 | 4578 | 7570 | 5052 | 510 | 2008 | 67 | 102 |

Gold errors for which at least one system has a correct different choice: 4866 of 4957.


# D. Chinese documents, 6 systems (no baseline)

Systems: s1f/r1, s1f/r2, s3/r1, s3/r2, a2/r1, a2/r2. 9027 points in 33 documents (zh-0001, zh-0002, zh-0003, zh-0004, zh-0005, zh-0006, zh-0007, zh-0008, zh-0009, zh-0010, zh-0011, zh-0012, zh-0013, zh-0014, zh-0015, zh-0016, zh-0017, zh-0018, zh-0021, zh-0022, zh-0023, zh-0024, zh-0026, zh-0027, zh-0028, zh-0029, zh-0030, zh-0031, zh-0032, zh-0033, zh-0034, zh-0035, zh-0036); 3721 where the gold should change.

## 1. Agreement between systems (6477 points where the systems differ)

| | s1f/r1 | s1f/r2 | s3/r1 | s3/r2 | a2/r1 | a2/r2 | gold |
|---|---|---|---|---|---|---|---|
| **s1f/r1** | – | 60 | 39 | 38 | 27 | 24 | 19 |
| **s1f/r2** | 60 | – | 39 | 38 | 26 | 23 | 18 |
| **s3/r1** | 39 | 39 | – | 69 | 49 | 47 | 29 |
| **s3/r2** | 38 | 38 | 69 | – | 51 | 48 | 28 |
| **a2/r1** | 27 | 26 | 49 | 51 | – | 77 | 32 |
| **a2/r2** | 24 | 23 | 47 | 48 | 77 | – | 34 |

Pairs from closest to farthest: a2/r1 ~ a2/r2 77; s3/r1 ~ s3/r2 69; s1f/r1 ~ s1f/r2 60; s3/r2 ~ a2/r1 51; s3/r1 ~ a2/r1 49; s3/r2 ~ a2/r2 48; s3/r1 ~ a2/r2 47; s1f/r1 ~ s3/r1 39; s1f/r2 ~ s3/r1 39; s1f/r1 ~ s3/r2 38; s1f/r2 ~ s3/r2 38; s1f/r1 ~ a2/r1 27; s1f/r2 ~ a2/r1 26; s1f/r1 ~ a2/r2 24; s1f/r2 ~ a2/r2 23

| pairs | mean agreement |
|---|---|
| same condition, the two runs | 68.4 |
| different conditions, same run | 37.2 |
| different conditions, different runs | 37.3 |
| s1f: r1 ~ r2 | 60.0 |
| s3: r1 ~ r2 | 68.7 |
| a2: r1 ~ r2 | 76.7 |
| within run r1 | 38.4 |
| within run r2 | 36.1 |

Mean agreement with the other systems: s1f/r1 37.5, s1f/r2 36.9, s3/r1 48.5, s3/r2 48.7, a2/r1 45.8, a2/r2 43.5

| category | points | mean number of different choices | mean pairwise agreement |
|---|---|---|---|
| sense | 560 | 2.3 | 44.2 |
| role | 1136 | 2.4 | 44.0 |
| concept | 834 | 2.4 | 43.8 |
| structure | 1328 | 2.6 | 41.5 |
| attr | 651 | 2.4 | 45.9 |
| doc-temporal | 607 | 2.6 | 44.4 |
| doc-modal | 741 | 2.7 | 39.9 |
| doc-coref | 620 | 2.3 | 46.4 |

How often a system is alone with its choice: s1f/r1 1304, s1f/r2 1388, s3/r1 753, s3/r2 732, a2/r1 559, a2/r2 785

## 2. Accuracy at the points (ok / (ok + minor + bad); open points left out)

| annotation | ok % | bad % | ok | minor | bad | open |
|---|---|---|---|---|---|---|
| gold | 45.5 | 28.0 | 4082 | 2385 | 2513 | 47 |
| s1f/r1 | 72.3 | 9.7 | 6470 | 1614 | 871 | 72 |
| s1f/r2 | 72.1 | 9.9 | 6437 | 1609 | 880 | 101 |
| s3/r1 | 88.8 | 0.9 | 7977 | 925 | 77 | 48 |
| s3/r2 | 89.1 | 0.7 | 8000 | 920 | 62 | 45 |
| a2/r1 | 85.2 | 3.2 | 7652 | 1042 | 284 | 49 |
| a2/r2 | 83.6 | 3.9 | 7504 | 1120 | 349 | 54 |

ok % by category:

| annotation | sense (678) | role (1474) | concept (1212) | structure (1770) | attr (971) | doc-temporal (983) | doc-modal (957) | doc-coref (982) |
|---|---|---|---|---|---|---|---|---|
| gold | 63.5 | 56.1 | 53.7 | 51.8 | 47.7 | 21.5 | 36.4 | 25.9 |
| s1f/r1 | 44.3 | 60.2 | 79.8 | 70.5 | 78.4 | 87.5 | 71.6 | 82.8 |
| s1f/r2 | 42.8 | 59.9 | 76.1 | 71.0 | 78.2 | 86.4 | 72.6 | 87.3 |
| s3/r1 | 93.2 | 93.0 | 84.0 | 84.1 | 83.2 | 94.4 | 91.4 | 91.7 |
| s3/r2 | 92.6 | 93.6 | 85.2 | 85.0 | 84.6 | 94.0 | 89.9 | 90.7 |
| a2/r1 | 95.1 | 90.7 | 84.2 | 85.3 | 84.6 | 95.0 | 69.4 | 77.4 |
| a2/r2 | 93.8 | 90.4 | 82.9 | 83.3 | 84.7 | 90.3 | 65.3 | 77.9 |

Where the gold is wrong (3721 points) and where it is right (4082 points):

| system | fixes the gold % | repeats the gold's error % | wrong or minor where the gold is right % |
|---|---|---|---|
| s1f/r1 | 81.2 | 3.7 | 36.7 |
| s1f/r2 | 81.3 | 3.4 | 37.6 |
| s3/r1 | 92.5 | 2.1 | 14.2 |
| s3/r2 | 92.9 | 1.6 | 14.1 |
| a2/r1 | 86.4 | 4.5 | 16.3 |
| a2/r2 | 84.0 | 5.4 | 16.5 |

## 3. Voting (strict majority; a flag = the vote differs from the gold)

| set | systems | votes needed | vote ok % | no decision | flags | good | harm | neutral | flag precision % | gold errors caught % |
|---|---|---|---|---|---|---|---|---|---|---|
| all | s1f/r1 + s1f/r2 + s3/r1 + s3/r2 + a2/r1 + a2/r2 | 4 | 94.6 | 2192 | 5346 | 3848 | 257 | 1241 | 72 | 103 |
| all, unanimous | s1f/r1 + s1f/r2 + s3/r1 + s3/r2 + a2/r1 + a2/r2 | 6 | 95.6 | 6477 | 2507 | 2051 | 85 | 371 | 82 | 55 |
| run r1 | s1f/r1 + s3/r1 + a2/r1 | 2 | 92.7 | 1061 | 6191 | 4214 | 370 | 1607 | 68 | 113 |
| run r2 | s1f/r2 + s3/r2 + a2/r2 | 2 | 93.0 | 1141 | 6131 | 4181 | 350 | 1600 | 68 | 112 |
| without s1f | s3/r1 + s3/r2 + a2/r1 + a2/r2 | 3 | 95.1 | 2481 | 5061 | 3693 | 215 | 1153 | 73 | 99 |
| only s1f | s1f/r1 + s1f/r2 | 2 | 77.1 | 2593 | 5677 | 3197 | 1075 | 1405 | 56 | 86 |
| without s3 | s1f/r1 + s1f/r2 + a2/r1 + a2/r2 | 3 | 93.5 | 3995 | 4258 | 3128 | 224 | 906 | 73 | 84 |
| only s3 | s3/r1 + s3/r2 | 2 | 93.4 | 2027 | 5546 | 3858 | 309 | 1379 | 70 | 104 |
| without a2 | s1f/r1 + s1f/r2 + s3/r1 + s3/r2 | 3 | 93.0 | 3096 | 5051 | 3529 | 273 | 1249 | 70 | 95 |
| only a2 | a2/r1 + a2/r2 | 2 | 87.6 | 1512 | 5672 | 3700 | 517 | 1455 | 65 | 99 |
| single | s1f/r1 | 1 | 72.3 | 0 | 7750 | 3882 | 1690 | 2178 | 50 | 104 |
| single | s1f/r2 | 1 | 72.1 | 0 | 7829 | 3900 | 1719 | 2210 | 50 | 105 |
| single | s3/r1 | 1 | 88.8 | 0 | 7138 | 4457 | 599 | 2082 | 62 | 120 |
| single | s3/r2 | 1 | 89.1 | 0 | 7152 | 4480 | 589 | 2083 | 63 | 120 |
| single | a2/r1 | 1 | 85.2 | 0 | 6901 | 4218 | 746 | 1937 | 61 | 113 |
| single | a2/r2 | 1 | 83.6 | 0 | 6790 | 4079 | 783 | 1928 | 60 | 110 |

Best sets of 2 by gold errors caught (then less harm):

| set | systems | votes needed | vote ok % | no decision | flags | good | harm | neutral | flag precision % | gold errors caught % |
|---|---|---|---|---|---|---|---|---|---|---|
| size 2 | s3/r1 + s3/r2 | 2 | 93.4 | 2027 | 5546 | 3858 | 309 | 1379 | 70 | 104 |
| size 2 | a2/r1 + a2/r2 | 2 | 87.6 | 1512 | 5672 | 3700 | 517 | 1455 | 65 | 99 |
| size 2 | s3/r2 + a2/r1 | 2 | 95.3 | 3185 | 4605 | 3413 | 187 | 1005 | 74 | 92 |
| size 2 | s3/r1 + a2/r1 | 2 | 95.2 | 3274 | 4534 | 3369 | 185 | 980 | 74 | 91 |
| size 2 | s3/r2 + a2/r2 | 2 | 95.7 | 3384 | 4400 | 3275 | 158 | 967 | 74 | 88 |
| size 2 | s3/r1 + a2/r2 | 2 | 95.5 | 3458 | 4330 | 3243 | 157 | 930 | 75 | 87 |

Best sets of 3 by gold errors caught (then less harm):

| set | systems | votes needed | vote ok % | no decision | flags | good | harm | neutral | flag precision % | gold errors caught % |
|---|---|---|---|---|---|---|---|---|---|---|
| size 3 | s3/r1 + s3/r2 + a2/r1 | 2 | 92.7 | 602 | 6559 | 4396 | 399 | 1764 | 67 | 118 |
| size 3 | s3/r1 + s3/r2 + a2/r2 | 2 | 92.8 | 629 | 6522 | 4386 | 382 | 1754 | 67 | 118 |
| size 3 | s1f/r1 + s3/r1 + s3/r2 | 2 | 91.9 | 675 | 6580 | 4346 | 428 | 1806 | 66 | 117 |
| size 3 | s1f/r2 + s3/r1 + s3/r2 | 2 | 92.2 | 705 | 6552 | 4335 | 410 | 1807 | 66 | 117 |
| size 3 | s1f/r2 + s3/r2 + a2/r1 | 2 | 93.0 | 1070 | 6220 | 4231 | 369 | 1620 | 68 | 114 |
| size 3 | s1f/r1 + s3/r2 + a2/r1 | 2 | 92.8 | 1046 | 6204 | 4224 | 369 | 1611 | 68 | 114 |

Best sets of 4 by gold errors caught (then less harm):

| set | systems | votes needed | vote ok % | no decision | flags | good | harm | neutral | flag precision % | gold errors caught % |
|---|---|---|---|---|---|---|---|---|---|---|
| size 4 | s1f/r2 + s3/r1 + s3/r2 + a2/r1 | 3 | 94.9 | 2246 | 5356 | 3855 | 238 | 1263 | 72 | 104 |
| size 4 | s1f/r1 + s3/r1 + s3/r2 + a2/r1 | 3 | 94.7 | 2250 | 5336 | 3839 | 244 | 1253 | 72 | 103 |
| size 4 | s1f/r2 + s3/r1 + s3/r2 + a2/r2 | 3 | 94.9 | 2299 | 5283 | 3807 | 238 | 1238 | 72 | 102 |
| size 4 | s1f/r1 + s3/r1 + s3/r2 + a2/r2 | 3 | 94.7 | 2307 | 5267 | 3792 | 241 | 1234 | 72 | 102 |
| size 4 | s3/r1 + s3/r2 + a2/r1 + a2/r2 | 3 | 95.1 | 2481 | 5061 | 3693 | 215 | 1153 | 73 | 99 |
| size 4 | s1f/r2 + s3/r2 + a2/r1 + a2/r2 | 3 | 94.9 | 2757 | 4884 | 3573 | 219 | 1092 | 73 | 96 |

Gold errors for which at least one system has a correct different choice: 3681 of 3721.
