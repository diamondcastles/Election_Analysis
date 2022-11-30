#The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Adding Dependencies
import csv
import os

# # Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# # Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

# # Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader=csv.reader(election_data)

#Read and print the header row
    headers = next(file_reader)
    print(headers)
     # Print the file object.
     #df = election_data.read()
     #print(df)

# msg = "meep"

# print(f'{msg}')
# make filename variable to a path to the file
# file_to_save = os.path.join("analysis","election_analysis.txt")
# #using open() function with "w" will allow us to write data to the file
# open(file_to_save,"w")
# outfile = open(file_to_save,"w")
# #Write three counties to the file.
# outfile.write("Counties in election\n-----------------\n")
# outfile.write("Arapahoe\nDevner\nJefferson")
# outfile.close()

