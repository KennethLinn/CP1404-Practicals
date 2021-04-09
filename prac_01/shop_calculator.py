num_item = int(input("Number of items: "))
total = 0
while num_item < 0:
    print("Invalid input")
    num_item = int(input("Number of items: "))
for i in range(num_item):
    price = float(input("Price of item: "))
    total += price
if total > 100:
    total = total * 0.9  # apply 10% discount
print(f'Total price for {num_item} items is ${total:.2f}')