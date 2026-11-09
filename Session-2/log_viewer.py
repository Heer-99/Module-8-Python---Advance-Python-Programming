
# ==========================================
# Task 1: Read Issue Log Line by Line
# ==========================================

# Open issue_log.txt in read mode
file = open("issue_log.txt", "r")

# Initialize line number
line_number = 1

# Read first line
line = file.readline()

# Read all lines using while loop
while line != "":
    # Display line number and record
    print(line_number, line.strip())

    # Increase line number
    line_number = line_number + 1

    # Read next line
    line = file.readline()

# Close the file
file.close()


# ==========================================
# Task 2: Create Line Index Using tell()
# ==========================================

# Open issue_log.txt in read mode
file = open("issue_log.txt", "r")

# Initialize line number
line_number = 1

# Create an empty list
line_index = []

# Read lines using while loop
while True:
    # Get current file position
    position = file.tell()

    # Read one line
    line = file.readline()

    # Stop at the end of file
    if line == "":
        break

    # Store line number and position
    line_index.append((line_number, position))

    # Display line number and record
    print(line_number, line.strip())

    # Increase line number
    line_number = line_number + 1

# Print line index
print("\nLine Index:")
print(line_index)

# Close the file
file.close()


# ==========================================
# Task 3: Lookup Line Using seek()
# ==========================================

# Ask user for line number
search_line = int(input("\nEnter line number to search: "))

# Open issue_log.txt in read mode
file = open("issue_log.txt", "r")

# Check whether line number exists
if search_line >= 1 and search_line <= len(line_index):

    # Get saved position from line_index
    position = line_index[search_line - 1][1]

    # Jump to saved position
    file.seek(position)

    # Read and display the required line
    line = file.readline()
    print("Line:", line.strip())

else:
    print("No such line")

# Close the file
file.close()




# ==========================================
# Task 4: Menu-Driven Log Viewer
# ==========================================

# Open issue_log.txt in read mode
file = open("issue_log.txt", "r")

while True:
    print("\n===== Library Log Viewer =====")
    print("A. Show All")
    print("J. Jump to a Line")
    print("R. Show Last 3 Entries")
    print("Q. Quit")

    choice = input("Enter your choice: ").upper()

    # Option A: Show all entries
    if choice == "A":
        file.seek(0)

        print("\nAll Log Entries:")
        line_number = 1

        while True:
            line = file.readline()

            if line == "":
                break

            print(line_number, line.strip())
            line_number = line_number + 1

    # Option J: Jump to a specific line
    elif choice == "J":
        search_line = int(input("Enter line number: "))

        if search_line >= 1 and search_line <= len(line_index):
            position = line_index[search_line - 1][1]

            file.seek(position)
            line = file.readline()

            print("Line:", line.strip())
        else:
            print("No such line")

    # Option R: Show last 3 entries
    elif choice == "R":
        recent_entries = line_index[-3:]

        if len(recent_entries) > 0:
            position = recent_entries[0][1]
            file.seek(position)

            print("\nLast 3 Entries:")

            while True:
                line = file.readline()

                if line == "":
                    break

                print(line.strip())
        else:
            print("No entries found")

    # Option Q: Quit program
    elif choice == "Q":
        print("Thank you! Program exited.")
        break

    else:
        print("Invalid choice! Please try again.")

# Close the file
file.close()

