#!/bin/sh
# when the skill after document n is written, test it: 5 runs (one per wording) on the test set; the last one also on the training set
cd /home/user/HarnessOntologyAnnotation/exp/round3
for n in 1 2 3 4; do
  until [ -f skills/pm-h$n.md ]; do sleep 30; done
  python3 run_claude.py --conds s3-full-two-tool --group test --reps 1 --skill skills/pm-h$n.md --tag pm-h$n --jobs 5 > logs/pm-h$n-test.log 2>&1 &
done
python3 run_claude.py --conds s3-full-two-tool --group train --reps 1 --skill skills/pm-h4.md --tag pm-h4 --jobs 5 > logs/pm-h4-train.log 2>&1
wait
echo ALLDONE
