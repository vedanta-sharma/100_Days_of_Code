#DAY - 2
#100DaysofCode
# Life in weeks

# age = int(input("Enter your age: "))
# life_expectancy = int(input("Enter the avg life expecancy in your country: "))
# years_left = life_expectancy - age
# days_left = years_left * 365
# weeks_left = years_left * 52
# months_left = years_left * 12
# print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

#Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\nRs."))
tip = float(input("How much tip would you like to give? (Ex: 10%, 12%, 15%)\n"))
people = int(input("How many people to split the bill?\n"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: Rs.{final_amount}")
