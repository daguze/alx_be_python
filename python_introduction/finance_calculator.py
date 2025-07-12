monthly_income = int(input("enter your total monthly income:"))
monthly_expenses = int(input("enter your total monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
interest_rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)
print ("Your monthly savings is:", monthly_savings)
print ("Projected savings after one year, with interest, is:", projected_savings)