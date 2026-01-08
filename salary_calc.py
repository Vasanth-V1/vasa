# 1. Accept basic salary as input
try:
    basic_pay = float(input("Enter the Basic Salary: "))

    # 2. Calculate Allowances
    hra = 0.20 * basic_pay  # 20% of basic
    da = 0.10 * basic_pay   # 10% of basic

    # Calculate Gross Salary (Total before tax)
    total_salary = basic_pay + hra + da

    # 3. Calculate Tax (5% of total salary)
    tax = 0.05 * total_salary

    # 4. Display Net Salary
    net_salary = total_salary - tax

    print("-" * 30)
    print(f"Basic Pay:    {basic_pay:>10.2f}")
    print(f"HRA (20%):    {hra:>10.2f}")
    print(f"DA (10%):     {da:>10.2f}")
    print(f"Gross Total:  {total_salary:>10.2f}")
    print(f"Tax (5%):    -{tax:>10.2f}")
    print("-" * 30)
    print(f"NET SALARY:   {net_salary:>10.2f}")
    print("-" * 30)

except ValueError:
    print("Error: Please enter a valid numerical value for salary.")