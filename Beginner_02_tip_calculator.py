#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the Tip Calculator.")
total_bill = input("What was the total bill? $")
percentage_bill = input("What percentage bill? ")
number_of_people = input("How many people to split? ")

output = float(total_bill)/int(number_of_people)* (1+ int(percentage_bill)/100)
output = "{:.2f}".format(output)
print(output)