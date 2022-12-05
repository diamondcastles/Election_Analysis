# Election_Analysis
## Overview 
The Colorado board of elections had interest in creating an election auditing tool. This tool, created in Python, will aid in tabulating data from an election for a U.S. Congressional precinct. By running this script, results can be tabulated and even placed into a report, providing a means for the board of elections to certify the race.

## Election-Audit Results
- In this election, there were 369,711 votes.
- In this congressional district, three counties were involved. Denver county placed a majority of the votes with 306,055 making up 82.8% of votes cast, followed by Jefferson county with 38,855 votes making up 10.5% of total votes cast, and Arapahoe county placed 24,801 votes, making up 6.7% of votes.
- Denver County placed the majority of votes and had the largest number of votes with 306,055 votes cast.
- Candidates Charles Casper Stockham won 85,213 votes, making up 23.0% of the votes cast, Diana DeGette won 272,892 votes, making up 73.8% of the votes cast, and Raymon Anthony Doane earned 11,606 votes, making up 3.1% of the vote.
- Candidate Diane DeGette won the election, winning 272,892 votes which made up 73.8% of the total votes.

## Election-Audit Summary

Ensuring that data is properly tabulated and is properly accounted for should be the utmost priority for any Democratic society. With this script, the election commission can automate a perhaps once tedious task and even gain valuable sociological data from the voters and areas in which they live. With this script, the sky is the limit with how large or small the election is, and with a few easy to make adjustments, you can go from a classroom, to a national election, for anything from congress candidates, to elections for a local mayor. Whatever data you bring to the table, this script can accommodate. 

An example of this accommodation includes a countys election for a new commissioner- in which you can adjust the library of townships within that county, and see a birds eye view of where the most voting effort happens, and for which candidates.

This script can also be adjusted for if the board of elections had a vested interest in voter demographic data itself. Typically, voter demographic data is gathered through the U.S. Census in surveys carried out in November of each year, however, it may benefit smaller boards of elections to send their own surveys. By finding out demographic information, this could give the board of elections a greater understanding of any unforseen disparity in voter accessibility in their locale. 

### Modifying the Code for Future Elections / Voter Demographic Data

```
[...]
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_results.txt")

# Import in demographic data from census results
demos_file = os.path.join("Resources", "national_census_data.csv")
```

With our census data loaded, we can use that information to create different reports based on the demographic data as a variable. For example, we could compare the election results with census data that looks at trends within certain age groups for a county:

```
[...]
county_list = []
county_votes = {}

# Create a list of age groups to help tally relevent census data
age_groups = ["18-29", "30-49", "50-64", "65"]
age_groups_tally = {}
```

From there, while we are going through the election data, we can simultaneously parse out the census data for that county to get demos by age:

```
[...]
# Function to get demo information for county
for rows in demos_file:
    for group in age_groups:
        # Iterate through age groups and tally up each county's reported data
    age_groups_tally[age_groups]
```

For our first example, we can modify this same logic we used to tally county votes, for townships to see which had the greatest concentration of voting (this is assuming in the next election we collect township votes in addition to county votes):

```
[...]
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_results.txt")

[...]
county_list = []
county_votes = {}

# Create a list of age groups to help tally relevent census data
township_name = []
township_votes = {}

[...]
# Function to get demo information for county
for rows in reader:
    [...]
    if township_name not in township_list:
        township_list.append(township_name)
        township_votes[township_name] = 0
    township_votes[township_name] +=1
```