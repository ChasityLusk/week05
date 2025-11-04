starting_salary = float(input("Enter the starting salary: "))
percent_increase = float(input("Enter the annual percentage increase: "))
years = int(input("Enter the number of years: "))

salary = starting_salary

for year in range(1, years + 1):
    print(f"{year}\t${salary:,.2f}")

    salary += salary * (percent_increase / 100)
    
