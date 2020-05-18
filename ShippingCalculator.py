Items = int(input("Please input the amount of items here: "))

def shipping_items():
    TotalCost = (((Items - 1) * 2.95) + 10.95)
    return TotalCost

print("The total cost of the shipping is $" + str(shipping_items()))