#!/bin/env bash

echo -n "All reports: "
csv 1 < status-migration.csv | wc -l

echo -n "Reports missing 'Rating' field: "
csv 4 < status-migration.csv | sed '/^\s*$/d' | wc -l
