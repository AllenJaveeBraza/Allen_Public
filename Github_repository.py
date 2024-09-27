# Salary Amount
Salary=input("Please input your monthly salary here:")
if float(Salary)>=30000:
    print("You are eligible for a loan")
else:
    print("You are not eligible for a loan.")
    exit()

# Loan Amount    
Loan=input("Please insert loan amount.(Note that you may only loan for a certain amount depending on your monthly salary.):")
if float(Loan)>=float(Salary)*10:
    print("Loan amount is too high, please input a lower amount.")
    exit()
else:
    Month=input("Loan eligible, how many months would you like to pay:")
    print("You are about to pay",Loan, "in", Month , "Months.")
    Total=float(Loan) + float(Loan) * 0.10
    print(f"total payment with 10% Interest:{Total:.2f}")
    print("Have a great day.")
