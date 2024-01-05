import os
import csv
total_votes=0
candidate_list=[]
candidate_votes={}
csvpath=os.path.join("Resources","election_data.csv")
output_path=os.path.join("Analysis","election_analysis.txt")
with open(csvpath,encoding="UTF-8") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader) 
    for row in csvreader:
        total_votes+=1      
        candidate=row[2]
        if candidate not in candidate_list:
            candidate_list+=[candidate]
            candidate_votes[candidate]=0
        candidate_votes[candidate]+=1
with open(output_path,"w")as file:
    output_vote=(
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes:{total_votes}\n"
        f"-------------------------\n"
    )
    print(output_vote)
    file.write(output_vote)

    winning_vote=0
    winner=""

    for candidate in candidate_votes:
        votes=candidate_votes.get(candidate)
        percent=float(votes)/total_votes*100


        if votes > winning_vote:
            winning_vote=votes
            winner=candidate

        candidate_total=f"{candidate}: {percent:.3f}% ({votes})\n"
        print(candidate_total)
        file.write(candidate_total)


    winning_candidate=(
        f"-------------------------\n"
        f"Winner:{winner}\n"
        f"-------------------------\n"
    )
    print(winning_candidate)
    file.write(winning_candidate)