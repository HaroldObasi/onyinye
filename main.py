account_balance = 10000000
rate = 10 / 100 

year = 0

print("Onyinye's Starting account balance is: ", account_balance)

while year < 5:
    interest = account_balance * rate
    account_balance = account_balance + interest

    print("At the end of year: ", year + 1 ," Onyinye's account balance is ", account_balance)
    year = year + 1