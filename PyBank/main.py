# Import dependencies
import os

import csv

# Create a path to csv file
budget_csv = os.path.join('.', '03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

# Define variables
total_months = 0

total_profits_losses = 0

profits_losses = []

months = []

changes = []

# Read in the CSV file
with open(budget_csv, newline='') as csvfile:
	
	# Split the data on commas
	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)

	# Loop through rows in csvreader
	for row in csvreader:

		# Calculate total months
		total_months = total_months + 1

		# Calculate total profits/losses
		total_profits_losses = total_profits_losses + int(row[1])

		# Add data from "Profits/Losses" column into profits/losses list
		profits_losses.append(int(row[1]))

		# Add data from "Date" column into date list
		months.append(row[0])

	# Loop through values between 1 and the length of the profits/losses list
	for i in range(1, len(profits_losses)):

		# Add the change in profits/losses between each month into the changes list
		changes.append(profits_losses[i]-profits_losses[i-1])

		# Calculate the average change
		average_change = sum(changes) / len(changes)

		# Calculate the greatest amount of change
		max_change = max(changes)

		# Calculate the least amount of change
		min_change = min(changes)

		# Define variable for months of greatest/least change
		max_change_month = str(months[changes.index(max(changes)) + 1])

		min_change_month = str(months[changes.index(min(changes)) + 1])

# Print out relevant statements
print("Financial Analysis")

print("-------------------------")

print("Total Months: " + str(total_months))

print("Total: " + "$" + str(total_profits_losses))

print("Average Change: " + "$" + str(round(average_change, 2)))

print("Greatest Increase in Revenue:", max_change_month,"($",max_change,")")

print("Greatest Decrease in Revenue:", min_change_month,"($",min_change,")")

# Create a path to txt file
output_file = os.path.join('output.txt')

# Output to txt file
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


