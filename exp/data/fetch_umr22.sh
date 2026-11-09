#!/bin/bash
# 下载 UMR 2.2（DMR 2026 UMR parsing shared task 的官方数据：training、test-blind、test-gold、两支队伍的系统输出），
# 解压到 exp/.cache/umr22/（不进 git：各语言的许可证见包里的 README.txt，中文 CC BY-NC-ND 4.0）。
# 来源：http://hdl.handle.net/11234/1-6132（LINDAT），Štěpánek et al. 2026, First Shared Task on UMR Parsing。
# 官方打分工具 ufal/umrtools（compare_umr.pl、validate.py）放到 exp/.cache/umrtools/。
set -e
cd "$(dirname "$0")/.."
mkdir -p .cache
if [ ! -d .cache/umr22/test-gold ]; then
  curl -sSL -o .cache/umr22.zip \
    https://lindat.mff.cuni.cz/repository/server/api/core/bitstreams/c29371c6-16d7-41d8-b7cb-50f67322bd96/content
  python3 -I -m zipfile -e .cache/umr22.zip .cache/
  mv .cache/uniform-meaning-representation-2.2 .cache/umr22
  rm .cache/umr22.zip
fi
[ -d .cache/umrtools ] || git clone -q --depth 1 https://github.com/ufal/umrtools .cache/umrtools
ls .cache/umr22/test-blind | wc -l
