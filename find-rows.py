#!/usr/bin/env python3

import csv


def find_rows():
    with open('status-migration.csv') as sheet:
        reports = csv.reader(sheet, delimiter=',')
        row_no = 0
        for r in reports:
            row_no += 1
            id = r[13]
            name = r[1]
            rating = r[3] # Platinum, Gold, etc
            status = r[4] # Stable, Unstable, etc
            notes = r[5]
            if not rating and status and not notes:
                print(row_no, name, status)


if __name__ == "__main__":
    find_rows()
