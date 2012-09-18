#!/usr/bin/env bash

rm -rf output && \
pig -x local -f analyzer/find_candidates.pig -l /dev/null
