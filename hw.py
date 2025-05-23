bill = float(input("Enter bill amount: "))
cash = float(input("Now enter what you paid: "))
x = bill - cash
if x > 0:
    print ("You owe $", x)
elif x == 0:
    print ("You paid the bill.")
elif x < 0:
    print ("You paid $", -1*x, " extra.")