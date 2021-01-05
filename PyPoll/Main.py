# This code calculates total votes, canadate totals, Precentage of votes won, and the final winner
import os
import csv

pollpath= os.path.join('Resources','election_data.csv')
# pollpath= os.path.join('Resources','V2.csv')
pollpath_w=os.path.join('PyBank.txt')

TotalVotes =0
KhanVotes=0
KhanPer=0
CorreyVotes=0
CorreyPer=0
LiVotes=0
LiPer=0
OTooleyVotes=0
OTooleyPer=0



with open(pollpath) as pollfile:
    with open(pollpath_w,'w') as pollfile_w:

        pollreader=csv.reader(pollfile, delimiter=',')
        # pollwriter=csv.writer(pollfile_w, delimiter=',')

        print(pollreader)

        pollheader= next(pollreader)
        # print(f'Poll Header: {pollheader}')

        for rows in pollreader:
            
            #test+
            TotalVotes += 1
            
            if rows[2]=='Khan':
                 KhanVotes += 1
            elif rows[2] =='Correy':
                 CorreyVotes += 1
            elif rows[2]=='Li':
                LiVotes += 1
            elif rows[2]=="O'Tooley":
                 OTooleyVotes += 1
       
    KhanPer=(KhanVotes/TotalVotes)*100
    CorreyPer=(CorreyVotes/TotalVotes)*100
    LiPer=(LiVotes/TotalVotes)*100
    OTooleyPer=(OTooleyVotes/TotalVotes)*100
    
    winner=' '
    maxVotes=0

    Canadates= {
        'Khan': KhanVotes,
        'Correy':CorreyVotes,
        'Li': LiVotes,
        "O'Tooley":OTooleyVotes}


    for Name,Votes in Canadates.items():
        if Votes > maxVotes:
            maxVotes = Votes
            winner = Name

output = f"""
Eleation Results
------------------------
Total Votes: {TotalVotes}
--------------------------
Kahn: {KhanPer:.2f}% ({KhanVotes:,})
Correy: {CorreyPer:.2f}% ({CorreyVotes:,})
Li: {LiPer:.2f}% ({LiVotes:,})
O'Tooley: {OTooleyPer:.2f}% ({OTooleyVotes:,})
----------------------------
Winner: {winner}
"""
print(output) 

with open(pollpath_w, 'w') as pollfile:
    pollfile.write(output)
