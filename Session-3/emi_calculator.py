
# ==========================================
# Task 1: EMI Calculator
# ==========================================

# Function to calculate EMI
def calculate_emi(principal, annual_rate, months):

    # Calculate monthly interest rate
    r = annual_rate / 12 / 100

    # Calculate EMI
    emi = (principal * r * (1 + r) ** months) / ((1 + r) ** months - 1)

    # Calculate total payable amount
    total_payable = emi * months

    # Calculate total interest
    total_interest = total_payable - principal

    return emi, total_payable, total_interest


# Task 1: Get loan details and display EMI
def task1():

    principal = float(input("Enter loan amount: "))
    annual_rate = float(input("Enter annual interest rate: "))
    months = int(input("Enter loan period in months: "))

    emi, total_payable, total_interest = calculate_emi(
        principal, annual_rate, months
    )

    print("\n===== EMI Calculator =====")
    print("Monthly EMI: ₹{:.2f}".format(emi))
    print("Total Payable: ₹{:.2f}".format(total_payable))
    print("Total Interest: ₹{:.2f}".format(total_interest))


# ==========================================
# Task 2: Handle Invalid Inputs
# ==========================================

def task2():

    while True:
        try:
            principal = float(input("Enter loan amount: "))
            annual_rate = float(input("Enter annual interest rate: "))
            months = int(input("Enter loan period in months: "))

            break

        except ValueError:
            print("Invalid input! Please enter valid numeric values. Try again.")

    emi, total_payable, total_interest = calculate_emi(
        principal, annual_rate, months
    )

    print("\n===== EMI Calculator =====")
    print("Monthly EMI: ₹{:.2f}".format(emi))
    print("Total Payable: ₹{:.2f}".format(total_payable))
    print("Total Interest: ₹{:.2f}".format(total_interest))


# ==========================================
# Task 3: Batch Mode with Exception Handling
# ==========================================

def process_batch(file, report_file=None):

    for line in file:
        data = line.strip().split(",")

        try:
            name = data[0]
            principal = float(data[1])
            annual_rate = float(data[2])
            months = int(data[3])

            emi, total_payable, total_interest = calculate_emi(
                principal, annual_rate, months
            )

            result = "{}: EMI = ₹{:.2f}".format(name, emi)

        except ValueError:
            result = "Invalid number in loan request"

        except ZeroDivisionError:
            result = "Interest rate is zero, EMI cannot be calculated"

        except IndexError:
            result = "Missing field in loan request"

        print(result)

        if report_file is not None:
            report_file.write(result + "\n")


def task3():

    file = open("loan_requests.txt", "r")
    process_batch(file)
    file.close()


# ==========================================
# Task 4: Batch Mode with File Handling
# ==========================================

def task4():

    # Ask for file name until a valid file is found
    while True:
        try:
            file_name = input("Enter file name: ")
            file = open(file_name, "r")
            break

        except FileNotFoundError:
            print("File not found! Please enter a valid file name.")

    # Open report file in write mode
    report_file = open("emi_report.txt", "w", encoding="utf-8")

    # Process loan requests and save results
    process_batch(file, report_file)

    # Close both files
    file.close()
    report_file.close()

    print("\nEMI report created successfully!")


# Run Task 4
task4()
