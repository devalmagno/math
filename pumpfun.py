import os

def main():
    x = 2608.750473  # Initial reserve of ARB
    y = 1000000000.0  # Initial reserve of PumpToken
    fee = 0.0
    value_in_fees = 0.0  # Value in fees accumulated

    userBalance = 0.0

    dxSell = 0.0
    dySell = 0.0
    dxBuy = 0.0
    dyBuy = 0.0

    while True:
        poolInfo(x, y, dxBuy, dyBuy, dxSell, dySell)        

        if (y == 206900000):
            print("\nBounding Curve reached.")
            print("Adding LP...")
            break

        print("\n1. Buy PumpToken\t2. Sell PumpToken \t3. Exit")
        option = int(input("\nEnter option: "))
        print("\n============================================================")
        if (option == 1):
            (x, y, userBalance, dxBuy, dyBuy) = buy(x, y, fee, userBalance)
        elif (option == 2):
            (x, y, userBalance, dxSell, dySell) = sell(x, y, fee, userBalance)
        elif (option == 3):
            break
        

def poolInfo(x, y, dxBuy, dyBuy, dxSell, dySell):
    initialReserve = 2608.750473  # Initial reserve of ARB
    liquidity = 206900000.0  # Initial liquidity
    max_x = 10000.0  # Target value for ARB reserve to reach

    clear_terminal()
    print("============================================================")
    print("Welcome to PumpFun.")
 
    print(f"ARB reserve: {x - initialReserve}")
    print(f"PumpToken reserve: {y - liquidity}")

    print(f"\nLatest buy - {dxBuy} ARB -> {dyBuy} PumpToken")
    print(f"Latest sell - {dySell} PumpToken -> {dxSell} ARB")

def buy(x, y, fee, userBalance):
    dx = float(input("Enter amount to buy in ARB: "))

    # Calculate tentative dy and update value in fees
    dy = (dx * (1 - fee) * y) / (x + dx * (1 - fee))

    if (y - dy < 206900000):
        dy = (y - 206900000)
        dx = (dy * (1 - fee) * x) / (y - dy)

    y -= dy
    x += dx
    userBalance += dy

    return (x, y, userBalance, dx, dy)

def sell(x, y, fee, userBalance):
    if (userBalance == 0.0):
        print("\nYou don't have any PumpToken to sell.")
        input()
        return (x, y, userBalance, 0, 0)

    print("\nSell PumpToken")
    dy = float(input("Enter amount to sell in PumpToken: "))
    if (dy > userBalance):
        print("\nYou don't have that much PumpToken to sell.")
        input()
        return (x, y, userBalance, 0, 0)

    dx = (dy * (1 - fee) * x) / (y + dy * (1 - fee))

    y += dy
    x -= dx
    userBalance -= dy

    return (x, y, userBalance, dx, dy)


def clear_terminal():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Mac and Linux (os.name is 'posix')
    else:
        os.system('clear')

if __name__ == "__main__":
    main()
