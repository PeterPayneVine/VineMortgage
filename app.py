def calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_payments = loan_term_years * 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)
    return monthly_payment

def remaining_balance(loan_amount, annual_interest_rate, loan_term_years, months_paid):
    monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years)
    remaining_balance = loan_amount * ((1 + annual_interest_rate / 12 / 100) ** months_paid) - (monthly_payment / (annual_interest_rate / 12 / 100)) * ((1 + annual_interest_rate / 12 / 100) ** months_paid - 1)
    return remaining_balance

def mortgage_calculator():
    # Get user inputs
    loan_amount = float(input("Enter the loan amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (%): "))
    loan_term_years = int(input("Enter the loan term in years: "))
    months_paid = int(input("Enter the number of months already paid: "))

    # Calculate and display remaining balance for each month
    for month in range(months_paid + 1, loan_term_years * 12 + 1):
        remaining_balance_month = remaining_balance(loan_amount, annual_interest_rate, loan_term_years, month)
        print(f'Month {month}: Remaining Balance = ${remaining_balance_month:.2f}')

if __name__ == "__main__":
    mortgage_calculator()
