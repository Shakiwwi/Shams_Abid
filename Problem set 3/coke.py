ACCEPTED = {25, 10, 5}
 
due = 50
while due > 0:
    coin = int(input(f"Amount Due: {due}\nInsert Coin: "))
    if coin in ACCEPTED:
        due -= coin
 
print(f"Change Owed: {abs(due)}")