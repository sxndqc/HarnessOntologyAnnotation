This package contains the training data for the UMR parsing shared task 2026
(https://ufal.mff.cuni.cz/umr-parsing).

There are six languages: Arapaho, Chinese, Czech, English, Latin, and Navajo.
The sizes of the available data vary significantly:

         clean                    dirty
         files sentences tokens   files sentences  tokens
Arapaho      1        53    274       2       292    1627
Chinese     20       557  15375       1      1435   18656
Czech        6       103   1587    6516    159906 2537317
English      4       180   2023     571     29872  292023
Latin        0                        3      1049   19139
Navajo       1         5     60       3       337    2663

The data is largely based on Uniform Meaning Representation releases 2.0 and 2.1
(http://hdl.handle.net/11234/1-5902, http://hdl.handle.net/11234/1-5951),
but multiple improvements have been applied.

See https://ufal.mff.cuni.cz/umr-parsing/umr-file-format for the specification of the UMR file format.
See https://github.com/ufal/umr-guidelines/blob/master/guidelines.md for the UMR annotation guidelines.

We distinguish two types of data available for training: "clean" and "dirty".
The dirty data is larger but it lacks document-level annotation, sometimes
also the node-token alignments. (Typically because it was converted from
AMR, PDT or other non-UMR formalisms where some annotation is not available.)
It may also contain additional relations not defined in UMR. Clean data should
contain all annotation parts and it should better conform to the annotation
guidelines. (Note: In Czech, the clean data has document-level annotation but
only of coreference relations, not modal and temporal relations. The same will
hold about Czech gold test data. The dirty data in both Czech and Latin also
have coreference relations, but Latin test data will contain full document
level graphs.)


LICENSE

CC BY-SA 4.0 for English
CC BY-NC-SA 4.0 for Czech and Latin
CC BY-NC-ND 4.0 for Chinese, Arapaho, and Navajo
