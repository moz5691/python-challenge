import os
import csv
from datetime import datetime

csvpath = os.path.join(".", "Resources", "budget_data.csv")
txtpath = os.path.join(".", "budget_data_report.txt")

prev_month = 0
date = []
profits_losses = []
changes = []
dt = datetime.now()


def average(lst):
    return sum(lst) / (len(lst) - 1)


def greatest_inc_or_dec_profit(lst1, lst2, inc_dec):
    if inc_dec == 'dec':
        profit = min(lst1)
    else:
        profit = max(lst1)
    index = lst1.index(profit)
    return lst2[index], "$" + str(profit)


def print_twice(*args, **kwargs):
    print(*args, **kwargs)
    with open(txtpath, "a", newline="") as f:
        print(file=f, *args, **kwargs)


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None)
    for row in csvreader:
        if prev_month == 0:
            # if first month,
            row.append(prev_month)
            prev_month = int(row[1])
        else:
            # if not first month,
            row.append(int(row[1]) - prev_month)
            prev_month = int(row[1])
        date.append(row[0])
        profits_losses.append(int(row[1]))
        changes.append(row[2])

try:
    if os.path.exists(txtpath):
        os.remove(txtpath)
except:
    print("Error while deleting file ", txtpath)

print_twice('Financial Analysis')
print_twice('====================================')
print_twice(f'Total months: {len(date)}')
print_twice(f'Total: {sum(profits_losses)}')
print_twice('Average change: ${:.2f}'.format(average(changes), 0.2))
print_twice(
    f'Greatest Increase in Profits: {greatest_inc_or_dec_profit(changes, date, "inc")}'
)
print_twice(
    f'Greatest Decrese in Profits : {greatest_inc_or_dec_profit(changes, date, "dec")}'
)
print_twice('====================================')
print_twice(f"Report was generated on {dt.isoformat(timespec='minutes')}")
