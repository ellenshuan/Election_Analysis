#add our dependencies 
import csv
import os
# Assign a variable to load a file from a path 
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize a total vote counter.
total_votes = 0 
#Candidate Options 
candidate_options = []
#Candidate Votes 
candidate_votes = {}
# County List 
county_list = []
county_votes = {}
#Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 
# Track the largest county and county voter turnout 
largest_county = ""
largest_county_turnout = 0 
largest_county_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file 
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1 
        # Print the candidate name from each row.
        candidate_name = row[2]
        #Extract the county name from each row 
        county_name = row[1]
        #If the candidate does not match any existing candidate add it to the candidate list 
        if candidate_name not in candidate_options:
            #Add candidate name the list of candidates.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count 
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count. 
        candidate_votes[candidate_name] += 1
        #Decision statement that checks that the county does not match any existing county in the county list 
        if county_name not in county_list:
            #then add the existing county to the list
            county_list.append(county_name)
            #Begin tracking the county's vote county 
            county_votes[county_name] = 0
        #Add a vote to that county's vote count 
        county_votes[county_name] += 1
#Save the results to our text file 
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    #Write a repetition statement to get the county from the county dictionary 
    for county_name in county_votes:
        #Retrieve county vote count 
        countyvotes = county_votes[county_name]
        #Calculate the percent of total votes for the county 
        county_vote_percentage = float(countyvotes) / float(total_votes) * 100 
        #Print the county results to the terminal 
        county_results =(
            f"{county_name}: {county_vote_percentage:.1f}% ({countyvotes:,})\n")
        print(county_results)
        #Save the county results to the terminal 
        txt_file.write(county_results)
        #Write a decision statement to determine the winning county and get its vote count
        if (countyvotes > largest_county_turnout) and (county_vote_percentage > largest_county_percentage): 
            largest_county_turnout = countyvotes
            county_vote_percentage = largest_county_percentage
            winning_county = county_name
    #Print the county with the largest turnout to the terminal.
        winning_county_summary = (
            f"-------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"-------------------------\n")
        print(winning_county_summary)
    #Save the winning county's name to the text file 
    txt_file.write(winning_county_summary)
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the terminal
        candidate_results =(
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #Save the candidate results to our text file.
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's name to the text file 
    txt_file.write(winning_candidate_summary)









