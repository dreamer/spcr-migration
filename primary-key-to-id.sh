#!/bin/env bash

sed -i '2,$ s/,\([0-9]\+\)primaryKey$/,\1/g' status-migration.csv
