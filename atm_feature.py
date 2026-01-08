# 1. Store a user’s balance
balance = 5000 

print(f"Welcome to the ATM. Your current balance is: {balance}")

# 2. Take withdrawal amount as input
# We use int() because we need to do math with the input
try:
    amount = int(input("Enter the amount you wish to withdraw: "))

    # 3. Checks
    # Check if amount is a multiple of 100
    if amount % 100 != 0:
        print("Error: Amount must be a multiple of 100 (e.g., 100, 200, 500).")
    
    # Check if balance is sufficient
    elif amount > balance:
        print("Error: Insufficient balance.")
    
    # Check for invalid negative numbers
    elif amount <= 0:
        print("Error: Please enter a valid amount above 0.")

    # 4. Success: Deduct amount and display updated balance
    else:
        balance -= amount # Same as balance = balance - amount
        print("Withdrawal successful!")
        print(f"Updated balance: {balance}")

except ValueError:
    print("Error: Please enter a numeric value.")