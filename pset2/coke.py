coke = 50
print(f"Amount Due: {abs(coke)}")


while coke > 0:
    coin = int(input("Insert Coin: "))
    if coin == 25:
        coke= coke-coin
        print(f"Chage Owed: {abs(coke)}")

    elif coin == 10:
        coke= coke-coin
        print(f"Chage Owed: {abs(coke)}")

    elif coin ==5:
        coke= coke-coin
        print(f"Chage Owed: {abs(coke)}")

    else:
        print(f"Change Owed: {abs(coke)}")

