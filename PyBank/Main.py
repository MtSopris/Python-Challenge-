#This code calculates total months reviewed, the net total over that period, the avrage change in p/l, and the greatest increase/decrease
import  os
import csv

csvpath= os.path.join('Resources','budget_data.csv')
csvpath_w= os.path.join('Analysis','PyBank.txt')

with open(csvpath) as csvfile:
    with open(csvpath_w,'w') as csvfile_w:

        csvreader=csv.reader(csvfile, delimiter=',')
        csvwriter=csv.writer(csvfile_w, delimiter=',')

        print(csvreader)

        csvheader = next(csvreader)
        # print(f'CSV Header: {csvheader}')

        # print totals rows for months
        row_count = sum(1 for row in csvreader)
        print ('Total Months: ' , row_count)
        
        # this resets the loop to row 2 in excel
        csvfile.seek(0)
        csvheader = next(csvreader)

        # total sum of column 2 aka total P/L
        # deifnes the variable /container to begin at 0 outside of loop
        TotalSum= 0
        TotalAvg=0
        Changes=[]
        ChangeVal=0
        LastPL=0
        GreatIn=0
        GreatInMonth=''
        LeastIn=0
        LeastInMonth=''
        rows= csvreader
        
        # loop through rows to calc total sum of column[1] aka B
        for row in rows:
            PL=int(row[1])
            TotalSum+=PL

            if LastPL != 0:
                ChangeVal=(PL-LastPL)
                Changes.append (ChangeVal)
                if GreatIn < ChangeVal:
                    GreatIn=ChangeVal
                    GreatInMonth=row[0]
                if LeastIn > ChangeVal:
                    LeastIn=ChangeVal
                    LeastInMonth=row[0]

            LastPL=PL

        # print(LastPL,PL)
        # print(len(Changes))
        # print (Changes)
        # print (row_count)
        print('Total: ','${:,}'.format(TotalSum))
        print('Average Change: ','${:,.2f}'.format(sum(Changes)/(row_count-1)))
        print('Greatest increase in profits: ',GreatInMonth,'(${:,})'.format(GreatIn))
        print('Greatest decrease in profits: ',LeastInMonth,'(${:,})'.format(LeastIn))
        csvwriter.writerow(['Financial Analysis'])
        csvwriter.writerow(['--------------------------------'])
        csvwriter.writerow(['Total: ','${:,}'.format(TotalSum)])
        csvwriter.writerow(['Average Change: ','${:,.2f}'.format(sum(Changes)/row_count)])
        csvwriter.writerow(['Greatest increase in profits: ',GreatInMonth,'(${:,})'.format(GreatIn)])
        csvwriter.writerow(['Greatest decrease in profits: ',LeastInMonth,'(${:,})'.format(LeastIn)])
        