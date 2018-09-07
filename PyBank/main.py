import os

import csv


budget_csv = os.path.join('.', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

total_months = 0

total_profits_losses = 0

profits_losses = []

months = []

changes = []


with open(budget_csv, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)

	for row in csvreader:

		total_months = total_months + 1

		total_profits_losses = total_profits_losses + int(row[1])

		profits_losses.append(int(row[1]))

		months.append(row[0])

	for i in range(1, len(profits_losses)):

		changes.append(profits_losses[i]-profits_losses[i-1])

		average_change = sum(changes) / len(changes)

		max_change = max(changes)

		min_change = min(changes)

		max_change_month = str(months[changes.index(max(changes))])

		min_change_month = str(months[changes.index(min(changes))])

print("Financial Analysis")

print("-------------------------")

print("Total Months: " + str(total_months))

print("Total: " + "$" + str(total_profits_losses))

print("Average Change: " + "$" + str(round(average_change, 2)))

print("Greatest Increase in Revenue:", max_change_month,"($",max_change,")")

print("Greatest Decrease in Revenue:", min_change_month,"($",min_change,")")


output_file = os.path.join('output.txt')

with open(output_file, "w") as txt_file:

	txt_file.write("Financial Analysis")

	txt_file.write("\n")

	txt_file.write("-------------------------")

	txt_file.write("\n")
	
	txt_file.write("Total Months: " + str(total_months))

	txt_file.write("\n")

	txt_file.write("Total: " + "$" + str(total_profits_losses))

	txt_file.write("\n")

	txt_file.write("Average Change: " + "$" + str(round(average_change, 2)))

	txt_file.write("\n")

	txt_file.write("Greatest Increase in Revenue:" + max_change_month + "($" + str(max_change) + ")")

	txt_file.write("\n")

	txt_file.write("Greatest Decrease in Revenue:" + min_change_month + "($" + str(min_change) + ")")


