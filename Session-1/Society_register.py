
# ==========================================
# Task 1: Add Society Maintenance Payment
# ==========================================

# Function to add a new payment
def add_payment():

    # Get payment details from the user
    flat = input("Enter flat number: ")
    owner = input("Enter owner name: ")
    month = input("Enter month: ")
    amount = input("Enter maintenance amount: ")

    # Open the file in append mode
    file = open("payments.txt", "a")

    # Write payment details into the file
    file.write(flat + "|" + owner + "|" + month + "|" + amount + "\n")

    # Close the file
    file.close()

    print("Payment added successfully!")


# ==========================================
# Task 2: Read and Display All Payments
# ==========================================

# Function to display all payments
def view_payments():

    # Open payments.txt in read mode
    file = open("payments.txt", "r")

    # Read all payment details once
    text = file.read()

    # Close the file
    file.close()

    # Initialize total amount
    total = 0

    # Display table headings
    print("\n{:<10}{:<20}{:<10}{:>12}".format(
        "Flat", "Owner", "Month", "Amount (₹)"
    ))
    print("-" * 52)

    # Split text into separate lines
    lines = text.split("\n")

    # Read each payment line
    for line in lines:
        if line != "":
            # Split payment details
            data = line.split("|")

            flat = data[0]
            owner = data[1]
            month = data[2]
            amount = int(data[3])

            # Display payment in aligned table format
            print("{:<10}{:<20}{:<10}{:>12}".format(
                flat, owner, month, "₹" + str(amount)
            ))

            # Add amount to total
            total = total + amount

    # Display total collected
    print("-" * 52)
    print("Total Collected: ₹", total)


# ==========================================
# Task 3: Write Monthly Payment Summary
# ==========================================

# Function to write monthly payment summary
def write_summary():

    # Open payments.txt in read mode
    file = open("payments.txt", "r")

    # Read all payment details
    text = file.read()

    # Close the file
    file.close()

    # Create an empty dictionary
    monthly_totals = {}

    # Split text into separate lines
    lines = text.split("\n")

    # Read each payment line
    for line in lines:
        if line != "":
            # Split payment details
            data = line.split("|")

            month = data[2]
            amount = int(data[3])

            # Calculate month-wise total
            if month in monthly_totals:
                monthly_totals[month] = monthly_totals[month] + amount
            else:
                monthly_totals[month] = amount

    # Open summary.txt in write mode
    file = open("summary.txt", "w", encoding="utf-8")

    # Write monthly totals into the file
    for month in monthly_totals:
        file.write(month + ": ₹" + str(monthly_totals[month]) + "\n")

    # Close the file
    file.close()

    print("Monthly summary created successfully!")


# ==========================================
# Task 4: Menu-Driven Society Register
# ==========================================

# Repeat menu until the user selects Exit
while True:

    print("\n===== Society Maintenance Register =====")
    print("1. Add Payment")
    print("2. View All Payments")
    print("3. Write Summary")
    print("4. Exit")

    # Get user's choice
    choice = input("Enter your choice: ")

    if choice == "1":
        add_payment()

    elif choice == "2":
        view_payments()

    elif choice == "3":
        write_summary()

    elif choice == "4":
        print("Thank you! Program exited.")
        break

    else:
        print("Invalid choice! Please try again.")
