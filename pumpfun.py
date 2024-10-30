def main():
    x0 = 13051.7  # Initial reserve of Matic
    y0 = 1000000000.0  # Initial reserve of PumpToken
    fee = 0.0
    value_in_fees = 0.0  # Value in fees accumulated
    max_x0 = 50000.0  # Target value for Matic reserve to reach

    while True:
        dx = float(input("Enter amount to buy in TokenGas: "))

        # Calculate tentative dy and update value in fees
        dy = (dx * (1 - fee) * y0) / (x0 + dx * (1 - fee))

        if (y0 - dy < 206900000):
            dy = (y0 - 206900000)
            dx = (boundingCurveY * (1 - fee) * x0) / (y0 - boundingCurveY)

        else:



        value_in_fees += dx * fee
        y0 -= dy
        x0 += dx

        # Print results
        print(f"\nTokenGas reserve: {x0}")
        print(f"PumpToken reserve: {y0}")
        print(f"Fee: {fee}")
        print(f"Amount to buy in TokenGas: {dx}")
        print(f"Amount to receive in PumpToken: {dy}")
        print(f"Amount in fees accumulated: {value_in_fees}\n")

        if (y0 == 206900000):
            print("\nBounding Curve reached.")
            print("Adding LP...")
            break
        
        option = int(input("Enter 1 to continue, 0 to exit: "))
        if option == 0:
            break

if __name__ == "__main__":
    main()
