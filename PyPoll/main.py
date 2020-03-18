import os
import csv
from datetime import datetime

csvpath = os.path.join(".", "Resources", "election_data.csv")
txtpath = os.path.join(".", "election_data_report.txt")

vote_counts = dict()
dt = datetime.now()


def print_twice(*args, **kwargs):
    print(*args, **kwargs)
    with open(txtpath, "a", newline="") as f:
        print(file=f, *args, **kwargs)


def max_key(dict):
    return max(dict, key=dict.get)


def sum_values(dict):
    return sum(dict.values())


def to_percent(a, b):
    return round((a / b) * 100, 4)


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
        out.append(key + ":  " + str(to_percent(val, total)) + "%" + " (" +
                   str(val) + ")")
    return '\n'.join(out)


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None)
    for row in csvreader:
        vote_counts[row[2]] = vote_counts.get(row[2], 0) + 1

total_votes = sum_values(vote_counts)

try:
    if os.path.exists(txtpath):
        os.remove(txtpath)
except:
    print("Error while deleting file ", txtpath)

print_twice("Election Results")
print_twice("--------------------------")
print_twice(f"Total Votes: {total_votes}")
print_twice("--------------------------")
print_twice(summary(vote_counts))
print_twice("--------------------------")
print_twice(f"Winner: {max_key(vote_counts)}")
print_twice("--------------------------")
print_twice(f"Report was generated on {dt.isoformat(timespec='minutes')}")