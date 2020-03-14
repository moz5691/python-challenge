import os
import csv
import math

csvpath = os.path.join(".", "Resources", "election_data.csv")
txtpath = os.path.join(".", "election_data_report.txt")


def print_twice(*args, **kwargs):
    """Print and save on file
    """
    print(*args, **kwargs)
    with open(txtpath, "a", newline="") as f:
        print(file=f, *args, **kwargs)


def max_key(dict):
    return max(dict, key=dict.get)


def sum_values(dict):
    return sum(dict.values())


def to_percent(a, b):
    return round((a/b)*100, 4)


def summary(dict):
    """Create summary

    Arguments:
        dict {} -- dictionary with name(key) and count(value)

    Returns:
        string -- created report
    """
    total = sum_values(dict)
    out = []
    for (key, val) in dict.items():
        out.append(key + ":  " + str(to_percent(val, total)) +
                   "%" + " (" + str(val) + ")")
    return '\n'.join(out)


counts = dict()

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None)
    for row in csvreader:
        counts[row[2]] = counts.get(row[2], 0) + 1

total_votes = sum_values(counts)

print(counts)

print_twice("Election Results")
print_twice("--------------------------")
print_twice(f"Total Votes: {total_votes}")
print_twice("--------------------------")
print_twice(summary(counts))
print_twice("--------------------------")
print_twice(f"Winner: {max_key(counts)}")
print_twice("--------------------------")
