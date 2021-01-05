import os
import csv

# pollpath= os.path.join('Resources','election_data.csv')
pollpath= os.path.join('Resources','V2.csv')
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
        pollwriter=csv.writer(pollfile_w, delimiter=',')

        print(pollreader)

        pollheader= next(pollreader)
        # print(f'Poll Header: {pollheader}')

        for rows in pollreader:
            
            TotalVotes += 1
            #test+
            # print(TotalVotes)

            # if rows[2] in pollreader:
            if rows[2]=='Khan':
                 KhanVotes += 1
            elif rows[2] =='Correy':
                 CorreyVotes += 1
            elif rows[2]=='Li':
                LiVotes += 1
            elif rows[2]=="O'Tooley":
                 OTooleyVotes += 1

        # else: 
       
    KhanPer=(KhanVotes/TotalVotes)*100
    CorreyPer=(CorreyVotes/TotalVotes)*100
    LiPer=(LiVotes/TotalVotes)*100
    OTooleyPer=(OTooleyVotes/TotalVotes)*100
    
    # Canadate_list=''
    # Votes_list=0
    winner=' '
    # Canadates={}
    # Canadates=dict()
    maxVotes=0

    Canadates= {
        'Khan': KhanVotes,
        'Correy':CorreyVotes,
        'Li': LiVotes,
        "O'Tooley":OTooleyVotes}

    # Canadates={'Name': '', 'Votes': 0}

    # Canadates_list = [
    #     'Khan',
    #     'Correy',
    #     'Li',
    #     "O'Tooley",]
    # Votes_list =[
    #     (KhanVotes),
    #     (CorreyVotes),
    #     (LiVotes),
    #     (OTooleyVotes)]
        
    # Canadates['Name']=Canadates_list
    # Canadates['Votes']=Votes_list
    # print (Canadates)

    for Name,Votes in Canadates.items():
        if Votes > maxVotes:
            maxVotes = Votes
            winner = Name

    

    # for key in Canadates:
    #     if ['Votes'] == (KhanVotes):
    #         winner='Khan'
    #     elif KhanVotes < CorreyVotes:
    #         winner= "Correy"  
    

    # print(winner)

    # print(KhanPer)
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
# print(TotalVotes)
# print('Khan: ',KhanVotes,',', KhanPer)
# print('Correy: ',CorreyVotes)
# print('Li: ',LiVotes)   
# print("O'Tooley: ",OTooleyVotes)
# print(winner)
