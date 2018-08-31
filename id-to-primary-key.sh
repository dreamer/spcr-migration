#!/bin/env bash

sed -i '2,$ s/,\([0-9]\+\)$/,\1primaryKey/g' status-migration.csv
