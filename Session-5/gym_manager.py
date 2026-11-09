
# ==========================================
# Task 1: Gym Manager
# ==========================================

# Dictionary to store monthly plan fees
plan_fees = {
    "Basic": 800,
    "Standard": 1200,
    "Premium": 1800
}


# Create Member class
class Member:

    def __init__(self, name, plan, months):
        self.name = name
        self.plan = plan
        self.months = months
        self.monthly_fee = plan_fees[plan]

    # Calculate total membership fee
    def total_fee(self):
        return self.monthly_fee * self.months

    # Renew membership
    def renew(self, extra_months):
        self.months += extra_months


# Create 5 Member objects
member1 = Member("Jiya", "Basic", 3)
member2 = Member("Priya", "Standard", 6)
member3 = Member("Avinash", "Premium", 12)
member4 = Member("Neha", "Basic", 2)
member5 = Member("Krish", "Standard", 4)


# Display member details
print("===== Gym Member Details =====")

print("Name:", member1.name)
print("Plan:", member1.plan)
print("Monthly Fee: ₹", member1.monthly_fee)

print("\nName:", member2.name)
print("Plan:", member2.plan)
print("Monthly Fee: ₹", member2.monthly_fee)

print("\nName:", member3.name)
print("Plan:", member3.plan)
print("Monthly Fee: ₹", member3.monthly_fee)

print("\nName:", member4.name)
print("Plan:", member4.plan)
print("Monthly Fee: ₹", member4.monthly_fee)

print("\nName:", member5.name)
print("Plan:", member5.plan)
print("Monthly Fee: ₹", member5.monthly_fee)


# ==========================================
# Task 2: Total Fee and Renewal
# ==========================================

# Create Standard member for 3 months
member6 = Member("Rahul", "Standard", 3)

print("\n===== Membership Renewal =====")

print("Name:", member6.name)
print("Plan:", member6.plan)
print("Months:", member6.months)
print("Total Fee: ₹", member6.total_fee())

# Renew membership for 2 extra months
member6.renew(2)

print("\nAfter Renewal:")
print("Months:", member6.months)
print("New Total Fee: ₹", member6.total_fee())


# ==========================================
# Task 3: Gym Manager Menu
# ==========================================

# List to store members
members = []

while True:

    print("\n===== Gym Manager Menu =====")
    print("1. Add Member")
    print("2. Show All")
    print("3. Exit")
    print("4. Renew Membership")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter member name: ")
        plan = input("Enter plan (Basic/Standard/Premium): ").strip().title()

        if plan not in plan_fees:
            print("Invalid plan! Please enter a valid plan.")
            continue

        try:
            months = int(input("Enter months (1 to 12): "))

            if months < 1 or months > 12:
                print("Invalid months! Please enter between 1 and 12.")
                continue

        except ValueError:
            print("Please enter a valid number of months!")
            continue

        member = Member(name, plan, months)
        members.append(member)

        print("Member added successfully!")

    elif choice == "2":

        print("\n===== All Gym Members =====")

        if len(members) == 0:
            print("No members found!")

        else:
            total_revenue = 0

            for member in members:
                print("\nName:", member.name)
                print("Plan:", member.plan)
                print("Months:", member.months)
                print("Monthly Fee: ₹", member.monthly_fee)
                print("Total Fee: ₹", member.total_fee())

                total_revenue += member.total_fee()

            print("\nTotal Revenue: ₹", total_revenue)



    # ==========================================
    # Task 4: Renew Membership
    # ==========================================
    
    elif choice == "4":

        name = input("Enter member name: ")

        found = False

        for member in members:

            if member.name.lower() == name.lower():

                try:
                    extra_months = int(input("Enter extra months: "))

                    if extra_months <= 0:
                        print("Please enter valid extra months!")

                    else:
                        member.renew(extra_months)

                        print("Membership renewed successfully!")
                        print("New Total Fee: ₹", member.total_fee())

                except ValueError:
                    print("Please enter a valid number!")

                found = True
                break

        if found == False:
            print("Member not found")

    elif choice == "3":
        print("Thank you! Exiting Gym Manager.")
        break

    else:
        print("Invalid choice! Please try again.")
