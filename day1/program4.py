cost=float(input("Enter cost price: "))
selling=float(input("Enter selling price: "))
if cost>=selling:
    print("No profit gain")
else:
    print("Profit earned is",selling-cost)
print("Selling price if we want to gain profit of 5% is",cost+0.05*cost)
