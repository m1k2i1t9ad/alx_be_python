# finance_calculator.py

# Prompting the user for financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculating monthly savings
monthly_savings = monthly_income - monthly_expenses

# Projecting annual savings with a simple interest rate of 5%
annual_projection = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Outputting the results
print(f'Your monthly savings are ${monthly_savings:.2f}.')
print(f'Projected savings after one year, with interest, is: ${annual_projection:.2f}.')
