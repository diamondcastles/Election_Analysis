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

#Establish total_votes variable to zero- must be above the file we are opening bc of way Python reads code and we always want this to be starting out at zero when file is
#open
total_votes = 0

##Establishing list
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# # Open the election results and read the file.
with open(file_to_load) as election_data:

    file_reader=csv.reader(election_data)

#Read the header row.
    headers = next(file_reader)

    for row in file_reader:
        candidate_name = row[2]
        total_votes += 1
        


# If the candidate does not match any existing candidate. Indentation required because this if statement is now outside of foor loop, the if only runs once.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
# Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] +=1

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        

        if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name 
        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

# print(candidate_votes)
# Print the  total votes
# print(total_votes)
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

