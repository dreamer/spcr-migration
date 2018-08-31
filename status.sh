#!/bin/env bash

all=$(csv 1 < status-migration.csv | wc -l)
echo "All reports: $all"

rated=$(csv 4 < status-migration.csv | sed '/^\s*$/d' | wc -l)
echo "Reports with 'Rating' field: $rated"

percent=$(echo "scale=2; $rated/$all*100" | bc)
echo "Progress: $percent%"
