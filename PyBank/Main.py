import os
import csv
total_month=0
total_net=0
net_change_list=[]




csvpath=os.path.join("Resources","budget_data.csv")
txtpath=os.path.join("analysis","budget_analysis.txt")


greatest_inc=["",0]
greatest_dec=["",0]
with open(csvpath,encoding="UTF-8") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header = next(csvreader) 
    first_row=next(csvreader)
    total_month=total_month+1
    profit_loss=int(first_row[1])
    total_net=total_net+profit_loss
    previous=int(first_row[1])

    for row in csvreader:
        total_month=total_month+1
        profit_loss=int(row[1])
        total_net=total_net+profit_loss
        net_change=profit_loss-previous
        previous=int(row[1])
        net_change_list+=[net_change]

        if net_change>greatest_inc[1]:
            greatest_inc[1]=net_change
            greatest_inc[0]=row[0]


        if net_change<greatest_dec[1]:
            greatest_dec[1]=net_change
            greatest_dec[0]=row[0]

monthly_average=sum(net_change_list)/len(net_change_list)
    
# Greatest_increase=max(net_change_list)
# Greatest_decrease=min(net_change_list)
# print(Greatest_increase)
# print(Greatest_decrease)

output=(
    f"Financial Analysis\n"
    f"------------------------\n"
    f"Total Months: {total_month}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${monthly_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n"
    f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})"
)
print(output)
with open(txtpath,"w") as txtfile:
    txtfile.write(output)

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
