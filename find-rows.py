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


def read_rows(file):
    entries = {}
    with open(file) as sheet:
        reports = csv.reader(sheet, delimiter=',')
        for r in reports:
            id = r[13]
            entries[id] = r
    return entries


if __name__ == "__main__":
    file_a = read_rows('status-migration.csv')
    file_b = read_rows('Steam_Play_Compatibility_Reports_-_Submissions.csv')

    for id_a in file_a:
        row_a = file_a[id_a]
        row_b = file_b[id_a]
        note_a = row_a[5]
        note_b = row_b[5]
        if note_a != note_b:
            print(id_a)

