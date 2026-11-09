# ==========================================
# Task 4: Contact Cleaner
# ==========================================

# Import Functions from format_checker.py
from format_checker import is_valid_pin, find_mobile


# Open Input File
file = open("contacts.txt", "r")

# Read All Contact Lines
contacts = file.readlines()

file.close()


# Open Output Files
valid_file = open("valid_contacts.txt", "w")
rejected_file = open("rejected_contacts.txt", "w")


# Check Each Contact
for contact in contacts:

    name, mobile, pin = contact.strip().split(",")

    # Check Mobile Number
    valid_mobile = find_mobile(mobile) == mobile

    # Check PIN Code
    valid_pin = is_valid_pin(pin)

    # Store Valid Contacts
    if valid_mobile and valid_pin:

        valid_file.write(contact)

    # Store Rejected Contacts
    else:

        reasons = []

        if not valid_mobile:
            reasons.append("Invalid mobile number")

        if not valid_pin:
            reasons.append("Invalid PIN code")

        reason = " and ".join(reasons)

        rejected_file.write(
            contact.strip() + " - " + reason + "\n"
        )


# Close Output Files
valid_file.close()
rejected_file.close()


print("Contact cleaning completed!")
print("Valid contacts saved in valid_contacts.txt")
print("Rejected contacts saved in rejected_contacts.txt")