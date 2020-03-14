import os
import csv
import math

csvpath = os.path.join(".", "Resources", "budget_data.csv")
txtpath = os.path.join(".", "Resources", "budget_data_report.txt")

prev_month = 0
date = []
profits_losses = []
changes = []


def average(lst):
    return sum(lst)/(len(lst)-1)


def greatest_inc_or_dec_profit(lst1, lst2, inc_dec):
    '''
    '''
    if inc_dec == 'dec':
        profit = min(lst1)
    else:
        profit = max(lst1)
    index = lst1.index(profit)
    return lst2[index], "$"+str(profit)


def print_twice(*args, **kwargs):
    print(*args, **kwargs)
    with open(txtpath, "a", newline="") as f:
        print(file=f, *args, **kwargs)


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader, None)
    for row in csvreader:
        if prev_month == 0:
            # first month
            row.append(prev_month)
            prev_month = float(row[1])
        else:
            # not first monath
            row.append(int(row[1])-prev_month)
            prev_month = int(row[1])
        date.append(row[0])
        profits_losses.append(int(row[1]))
        changes.append(row[2])

print_twice('Financial Analysis')
print_twice('====================================')
print_twice(f'Total months: {len(date)}')
print_twice(f'Total {sum(profits_losses)}')
print_twice('Average change ${:.2f}'.format(
    average(changes), 0.2))
print_twice(
    f'Greatest Increase in Profits: {greatest_inc_or_dec_profit(changes, date, "inc")}')
print_twice(
    f'Greatest Decrese in Profits : {greatest_inc_or_dec_profit(changes, date, "dec")}')
