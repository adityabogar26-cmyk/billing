prices = []

n = int(input("Enter number of items: "))

for i in range(n):
    price = float(input(f"Enter price of item {i+1}: "))
    prices.append(price)

total = sum(prices)

print("\n----- BILL -----")
print("Total Bill: ₹", total)