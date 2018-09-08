# Import dependencies
import os

import csv

import collections

from operator import itemgetter

# Create a path to csv file
election_csv = os.path.join('.', '03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

# Define variables
total_votes = 0

votes = collections.Counter()

# Read in the CSV file
with open(election_csv, newline='') as csvfile:

	# Split the data on commas
	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)

	# Loop through rows in csvreader
	for row in csvreader:

		# Calculate total votes
		total_votes = total_votes + 1

		# Collect votes for each candidate's name in a counter
		votes[row[2]] += 1

# Sort through the votes counter to find the candidate with the most votes
winner = sorted(votes.items(), key=itemgetter(1), reverse=True)

# Print out relevant statements
print("Election Results")

print("-------------------------")

print("Total Votes: " + str(total_votes))

print("-------------------------")

print("Khan: "+"{:.2%}".format(float((votes["Khan"])/total_votes)) + " (" + str(votes["Khan"]) + ")")

print("Correy: "+"{:.2%}".format(float((votes["Correy"])/total_votes)) + " (" + str(votes["Correy"]) + ")")

print("Li: "+"{:.2%}".format(float((votes["Li"])/total_votes)) + " (" + str(votes["Li"]) + ")")

print("O'Tooley: "+"{:.2%}".format(float((votes["O'Tooley"])/total_votes)) + " (" + str(votes["O'Tooley"]) + ")")

print("-------------------------")

print("Winner: " + str(winner[0]))

print("-------------------------")

# Create a path to txt file
output_file = os.path.join('output.txt')

# Output to txt file
with open(output_file, "w") as txt_file:

	txt_file.write("Election Results")
	
	txt_file.write("\n")

	txt_file.write("-------------------------")

	txt_file.write("\n")

	txt_file.write("Total Votes: " + str(total_votes))
	
	txt_file.write("\n")

	txt_file.write("-------------------------")

	txt_file.write("\n")
	
	txt_file.write("Khan: "+"{:.2%}".format(float((votes["Khan"])/total_votes)) + " (" + str(votes["Khan"]) + ")")

	txt_file.write("\n")

	txt_file.write("Correy: "+"{:.2%}".format(float((votes["Correy"])/total_votes)) + " (" + str(votes["Correy"]) + ")")

	txt_file.write("\n")

	txt_file.write("Li: "+"{:.2%}".format(float((votes["Li"])/total_votes)) + " (" + str(votes["Li"]) + ")")

	txt_file.write("\n")

	txt_file.write("O'Tooley: "+"{:.2%}".format(float((votes["O'Tooley"])/total_votes)) + " (" + str(votes["O'Tooley"]) + ")")

	txt_file.write("\n")

	txt_file.write("-------------------------")

	txt_file.write("\n")

	txt_file.write("Winner: " + str(winner[0]))

	txt_file.write("\n")

	txt_file.write("-------------------------")
