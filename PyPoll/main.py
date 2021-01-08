# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("/Users/nicksullivan/Desktop/python-challenge/PyPoll/Resources/election_data.csv")

# Create lists/variables to store data
votes_by_candidate = []

# Open and read csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip first row
    csv_header = next(csv_reader)
    # Read list of votes
    list_of_votes = [row[2] for row in csv_reader]
    # Determine total votes
    total_votes = len(list_of_votes)
    # Determine list of candidates
    candidates_list = list(set(list_of_votes))
    # Determine total number of votes for each candidate
    for candidate_name in candidates_list:
        votes_by_candidate.append([candidate_name, list_of_votes.count(candidate_name)])
    # Sort candidates by total number of votes
    votes_by_candidate.sort(key=lambda x:x[1], reverse =True)
   
# Print election results
print("Election Results")
print("------------------------")

    # Print total votes
print("Total Votes: " + str(total_votes))
print("------------------------")

    # Determine percent of votes for each candidate by looping through data
for row in votes_by_candidate:
    percent_of_vote = row[1] * 100 / total_votes
    percent_of_vote_rounded = round(percent_of_vote, 3)
    candidate_name = row[0] + ":"

    # Print results for each candidate
    print(str(candidate_name) + " " + str(percent_of_vote_rounded) + "% " + "(" + str(row[1]) + ")")

    # Print winner
print("------------------------")
print("Winner: " + votes_by_candidate[0][0])
print("------------------------")

# Export results to .txt file
with open("election_results.txt", "w") as text_file:
    print("Election Results", file = text_file)
    print("------------------------", file = text_file)
    print("Total Votes: " + str(total_votes), file = text_file)
    print("------------------------", file = text_file)
    for row in votes_by_candidate:
        percent_of_vote = row[1] * 100 / total_votes
        percent_of_vote_rounded = round(percent_of_vote, 3)
        candidate_name = row[0] + ":"
        print(str(candidate_name) + " " + str(percent_of_vote_rounded) + "% " + "(" + str(row[1]) + ")", file = text_file)
    print("------------------------", file = text_file)
    print("Winner: " + votes_by_candidate[0][0], file = text_file)
    print("------------------------", file = text_file)

# Move .txt file into Analysis folder
    os.replace("/Users/nicksullivan/Desktop/python-challenge/election_results.txt", "/Users/nicksullivan/Desktop/python-challenge/PyPoll/Analysis/election_results.txt")
