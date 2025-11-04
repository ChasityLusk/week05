price = float(input("Enter the purchase price: "))

balance = price * 0.9
monthly_payment = price * 0.05
interest_rate = 0.12

month = 0

print(f"{'Month':>5} {'Balance':>12} {'Interest':>12} {'Principal':>12} {'Payment':>12} {'Remaining Balance':>12}")
print("-" * 75)
while balance > 0:
    month += 1
    interest = balance * (interest_rate / 12)
    principal = monthly_payment - interest

    if principal > balance:
        principal = balance
        monthly_payment = interest + principal

    remaining_balance = balance - principal

    print(f"{month:5d} {balance:11,.2f} ${interest:11,.2f} ${principal:11,.2f} "
          f"${monthly_payment:11,.2f} ${remaining_balance:15,.2f}$")

    balance = remaining_balance

print(f"\nLoan paid off in {month} months.")
