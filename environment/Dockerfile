FROM python:3.12-slim

# Install minimal tools needed by agents, solve.sh, and tests/test.sh.
# - bash: for shell scripts
# - curl/git: useful agent utilities
# - patch: included because executable task templates often expect it
# - ca-certificates: safe HTTPS access if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    git \
    patch \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create standard runtime directories used by Harbor, the agent, oracle, and verifier.
RUN mkdir -p \
    /workspace \
    /testbed \
    /logs/agent \
    /logs/verifier \
    /environment/input_artifacts

# Copy task input artifacts into the exact path used by instruction.md,
# verify.py, and solve.sh.
#
# IMPORTANT:
# Put your datasets here on the host:
# environment/input_artifacts/
#
# They will appear inside the container at:
# /environment/input_artifacts/
COPY input_artifacts/ /environment/input_artifacts/

# Set the working directory used in instruction.md.
WORKDIR /workspace

# Python stdlib is enough for this task:
# csv, json, re, pathlib, datetime, collections.
# No extra pip packages are required.
