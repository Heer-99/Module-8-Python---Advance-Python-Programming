# ==========================================
# Task 1: Indian PIN Code Format Checker
# ==========================================

import re


# Function to Check Valid PIN Code
def is_valid_pin(text):

    pattern = r"^[1-9][0-9]{5}$"

    if re.match(pattern, text):
        return True
    else:
        return False


# Test PIN Codes
pin_codes = [
    "380015",
    "110001",
    "056001",
    "38001",
    "3800155",
    "38O015"
]


# Check Each PIN Code
for pin in pin_codes:

    if is_valid_pin(pin):
        print(pin, "is Valid")
    else:
        print(pin, "is Invalid")


# ==========================================
# Task 2: Find Indian Mobile Number
# ==========================================

# Function to Find Mobile Number
def find_mobile(text):

    pattern = r"(?<!\d)(?:\+91)?[6-9][0-9]{9}(?!\d)"

    match = re.search(pattern, text)

    if match:
        return match.group()
    else:
        return None


# Test Sentences
sentences = [
    "Call 9000012345 after 6 pm",
    "Reach me on +919000012345",
    "Flat 5000012345",
    "Ring 900001234"
]


# Check Each Sentence
for sentence in sentences:

    result = find_mobile(sentence)

    print("Sentence:", sentence)
    print("Mobile Number:", result)
    print()


# ==========================================
# Task 3: Count PIN Codes from Addresses
# ==========================================

# Function to Count PIN Codes
def count_pins():

    file = open("addresses.txt", "r")

    text = file.read()

    file.close()

    # Find All PIN Codes
    pins = re.findall(r"\b[1-9][0-9]{5}\b", text)

    # Create Dictionary
    pin_count = {}

    # Count Each PIN Code
    for pin in pins:

        if pin in pin_count:
            pin_count[pin] += 1
        else:
            pin_count[pin] = 1

    # Display PIN Code Counts
    for pin, count in pin_count.items():
        print(pin, "appears", count, "times")


# Call Function
count_pins()