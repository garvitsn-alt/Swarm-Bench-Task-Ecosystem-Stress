#!/bin/bash
set -euo pipefail
mkdir -p /logs/verifier

cd /testbed

set +e
python3 /tests/verify.py 2>&1 | tee /logs/verifier/test-output.log
exit_code=$?
set -e

# Preserve fractional reward written by verify.py.
# If verify.py failed before writing reward.txt, write a binary fallback.
if [ ! -f /logs/verifier/reward.txt ]; then
  if [ "${exit_code}" -eq 0 ]; then
    echo 1 > /logs/verifier/reward.txt
  else
    echo 0 > /logs/verifier/reward.txt
  fi
fi

exit 0