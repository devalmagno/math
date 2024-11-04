total_sum = 0.0

while True:
    try:
        user_input = input("Enter a float number (or type 'done' to finish): ")
        
        if user_input.lower() == 'done':
            break

        number = float(user_input)
        total_sum += number - 0.02

    except ValueError:
        print("Please enter a valid float number or type 'done' to finish.")

print(f"Total sum: {total_sum:.2f}")

