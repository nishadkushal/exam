    while True:
        try:
            # Input: Number of people
            num_people = int(input("Enter number of people: "))
            if num_people <= 0:
                print("Number of people must be greater than 0.")
                continue

            # Input: Total bill amount
            total_bill = float(input("Enter total bill amount: "))
            if total_bill < 0:
                print("Bill amount cannot be negative.")
                continue

            # Input: Tip percentage
            tip_percentage = int(input("Enter tip percentage (0, 5, 10, 15, 20): "))
            if tip_percentage not in [0, 5, 10, 15, 20]:
                print("Invalid tip percentage. Choose from 0, 5, 10, 15, 20.")
                continue

            # Calculation
            tip_amount = (tip_percentage / 100) * total_bill
            total_with_tip = total_bill + tip_amount
            per_person = total_with_tip / num_people

            # Output
            print(f"Tip amount: ₹{tip_amount:.2f}")
            print(f"Total amount with tip: ₹{total_with_tip:.2f}")
            print(f"Amount per person: ₹{per_person:.2f}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Optional looping task
        repeat = input("Do you want to calculate another bill? (yes/no): ").strip().lower()
        if repeat != "yes":
            print("Thank you for using the bill splitter!")
            break

