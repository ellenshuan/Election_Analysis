#The data we need to retrieve. 
#1. The total number of votes cast 
#2. A complete list of candidates who recieved votes 
#3. The percentages of votes each candidate won 
#4. The total number of votes each candidate won
#5. The winnder of the election based on popular vote. 

#add our dependencies 
import csv
import os

# Assign a variable to load a file from a path 
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze the data here 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

#using the open() function with the "w" mode we will write the data to the file 
with open(file_to_save, "w") as txt_file: 

  # Write three counties to the file.
     txt_file.write("Arapahoe\nDenver\nJefferson")