#!/bin/bash
# 直接调 API 的全部子实验（第一步两个，第二步三个），测试集是 UMR parsing shared task 的中文 15 个文件、英文 5 个文件。
# 用法：bash exp/run_api.sh [模型，默认 claude-opus-5-5] [effort，默认 high] [语言，默认 zh,en；all 为全部七种]
# 需要 UMR_MODEL_KEY；回答缓存在 exp/.cache/answers/，重跑只问变了的部分。
set -e
cd "$(dirname "$0")/.."
MODEL=${1:-claude-opus-5-5}
EFFORT=${2:-high}
LANGS=${3:-zh,en}
[ -n "$UMR_MODEL_KEY" ] || { echo "UMR_MODEL_KEY is not set"; exit 1; }
bash exp/data/fetch_umr22.sh > /dev/null
for SUB in s1-abridged s1-full s2-search s2-propbank s2-gold; do
  python3 exp/run.py api $SUB --model $MODEL --effort $EFFORT --langs $LANGS --jobs 4
done
python3 exp/run.py table
