import os

import csv

import collections


election_csv = os.path.join('.', '03-Python_Homework_Instructions_PyPoll_Resources_election_data.csv')

total_votes = 0

votes = collections.Counter()


with open(election_csv, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	csv_header = next(csvreader)

	for row in csvreader:

		total_votes = total_votes + 1

		votes[row[2]] += 1

print("Election Results")

print("-------------------------")

print("Total Votes: " + str(total_votes))

print("-------------------------")

print("Khan: "+"{:.2%}".format(float((votes["Khan"])/total_votes)) + " (" + str(votes["Khan"]) + ")")

print("Correy: "+"{:.2%}".format(float((votes["Correy"])/total_votes)) + " (" + str(votes["Correy"]) + ")")

print("Li: "+"{:.2%}".format(float((votes["Li"])/total_votes)) + " (" + str(votes["Li"]) + ")")

print("O'Tooley: "+"{:.2%}".format(float((votes["O'Tooley"])/total_votes)) + " (" + str(votes["O'Tooley"]) + ")")

print("-------------------------")

print("Winner: Khan")

print("-------------------------")


output_file = os.path.join('output.txt')

with open(output_file, "w") as txt_file:

	txt_file.write("Election Results")
	
	txt_file.write("\n")

	txt_file.write("Total Votes: " + str(total_votes))
	
	txt_file.write("\n")
	
	txt_file.write("Khan: "+"{:.2%}".format(float((votes["Khan"])/total_votes)) + " (" + str(votes["Khan"]) + ")")

	txt_file.write("\n")

	txt_file.write("Correy: "+"{:.2%}".format(float((votes["Correy"])/total_votes)) + " (" + str(votes["Correy"]) + ")")

	txt_file.write("\n")

	txt_file.write("Li: "+"{:.2%}".format(float((votes["Li"])/total_votes)) + " (" + str(votes["Li"]) + ")")

	txt_file.write("\n")

	txt_file.write("O'Tooley: "+"{:.2%}".format(float((votes["O'Tooley"])/total_votes)) + " (" + str(votes["O'Tooley"]) + ")")

	txt_file.write("\n")

	txt_file.write("Winner: Khan")
