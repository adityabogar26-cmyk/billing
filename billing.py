prices = []

n = int(input("Enter number of items: "))

for i in range(n):
    price = float(input(f"Enter price of item {i+1}: "))
    prices.append(price)

total = sum(prices)

discount = 0

if total > 1000:
    discount = total * 0.10

final_amount = total - discount

print("\n----- BILL -----")
print("Total Bill: ₹", total)
print("Discount: ₹", discount)
print("Final Amount: ₹", final_amount)