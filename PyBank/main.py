# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("/Users/nicksullivan/Desktop/python-challenge/PyBank/Resources/budget_data.csv")

# Create lists to store data
month_list = []
profitloss_list = []

# Open and read csv
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip first row
    csv_header = next(csv_reader)
    # Create lists 
    for row in csv_reader:
        month_list.append(row[0])
        profitloss_list.append(int(row[1]))

# Determine total months
total_months = len(month_list)

# Determine net total profit or loss
total_profitloss = sum(profitloss_list)

# Determine average profit or loss
average_profitloss = total_profitloss/total_months

# Determine amount and month of greatest increase in profits
greatest_increase = max(profitloss_list)
greatest_increase_month = month_list[profitloss_list.index(greatest_increase)]

# Determine amount and month of greatest decrease in profits
greatest_decrease = min(profitloss_list)
greatest_decrease_month = month_list[profitloss_list.index(greatest_decrease)]

# Print results
print("Financial Analysis")
print("--------------------------")
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profitloss))
print("Average Change: $" + str(average_profitloss))
print("Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ")")

# Export results to .txt file
with open("financial_analysis.txt", "w") as text_file:
    print("Financial Analysis", file = text_file)
    print("--------------------------", file = text_file)
    print("Total Months: " + str(total_months), file = text_file)
    print("Total: $" + str(total_profitloss), file = text_file)
    print("Average Change: $" + str(average_profitloss), file = text_file)
    print("Greatest Increase in Profits: " + greatest_increase_month + " ($" + str(greatest_increase) + ")", file = text_file)
    print("Greatest Decrease in Profits: " + greatest_decrease_month + " ($" + str(greatest_decrease) + ")", file = text_file)

# Move .txt file into Analysis folder
    os.replace("/Users/nicksullivan/Desktop/python-challenge/financial_analysis.txt", "/Users/nicksullivan/Desktop/python-challenge/PyBank/Analysis/financial_analysis.txt")