#!/bin/bash
# 直接调 API 的全部子实验：第一步两个，第二步三个。每个子实验 11 篇测试文档（中文 7 篇 99 句、英文 4 篇 95 句）。
# 用法：bash exp/run_api.sh [模型，默认 claude-opus-5-5] [effort，默认 high]
# 需要 UMR_MODEL_KEY；回答缓存在 exp/.cache/answers/，重跑只问变了的部分。
set -e
cd "$(dirname "$0")/.."
MODEL=${1:-claude-opus-5-5}
EFFORT=${2:-high}
[ -n "$UMR_MODEL_KEY" ] || { echo "UMR_MODEL_KEY is not set"; exit 1; }
[ -d exp/.cache/umrtools ] || git clone -q --depth 1 https://github.com/ufal/umrtools exp/.cache/umrtools || echo "no umrtools: juːmæʧ will be missing"
for SUB in s1-abridged s1-full s2-search s2-propbank s2-gold; do
  python3 exp/run.py api $SUB --model $MODEL --effort $EFFORT --jobs 4
done
python3 exp/run.py table
