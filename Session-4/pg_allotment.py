
# ==========================================
# Task 1: PG Room Allotment
# ==========================================

# Dictionary to store room capacities
rooms = {
    "R101": 2,
    "R102": 3,
    "R103": 2,
    "R104": 3,
    "R105": 2,
    "R106": 3
}

# Dictionary to store students in each room
room_students = {
    "R101": [],
    "R102": [],
    "R103": [],
    "R104": [],
    "R105": [],
    "R106": []
}


# Function to allot a student to a room
def allot(student_name, room_no):

    if room_no not in rooms:
        return "Room does not exist!"

    if len(room_students[room_no]) < rooms[room_no]:
        room_students[room_no].append(student_name)
        return student_name + " successfully allotted to " + room_no

    return room_no + " is already full!"


# Test with 4 students in 2 different rooms
print(allot("Kiran Patel", "R101"))
print(allot("Diya Shah", "R101"))

print(allot("Meera Joshi", "R102"))
print(allot("Jay Panchal", "R102"))


# Display room details
print("\n===== PG Room Details =====")

for room_no in rooms:
    print(room_no, "Capacity:", rooms[room_no],
          "Students:", room_students[room_no])


# ==========================================
# Task 2: Custom Exceptions
# ==========================================

class InvalidRoomError(Exception):
    pass


class RoomFullError(Exception):
    pass


class DuplicateStudentError(Exception):
    pass


# Updated allot function using custom exceptions
def allot(student_name, room_no):

    if room_no not in rooms:
        raise InvalidRoomError("Room does not exist!")

    for room in room_students:
        if student_name in room_students[room]:
            raise DuplicateStudentError("Student already has a room!")

    if len(room_students[room_no]) >= rooms[room_no]:
        raise RoomFullError("Room is already full!")

    room_students[room_no].append(student_name)

    return student_name + " successfully allotted to " + room_no


# Test custom exceptions with user input
print("\n===== Student Room Allotment =====")

student_name = input("Enter student name: ").strip()
room_no = input("Enter room number: ").strip().upper()

if not student_name:
    print("Student name cannot be empty!")

else:
    try:
        message = allot(student_name, room_no)
        print(message)

    except InvalidRoomError as e:
        print("InvalidRoomError:", e)

    except DuplicateStudentError as e:
        print("DuplicateStudentError:", e)

    except RoomFullError as e:
        print("RoomFullError:", e)


# Display updated room details
print("\n===== Updated PG Room Details =====")

for room_no in rooms:
    print(room_no, "Capacity:", rooms[room_no],
          "Students:", room_students[room_no])




# ==========================================
# Task 3: Menu Loop for PG Room Allotment
# ==========================================

while True:

    print("\n===== PG Room Allotment Menu =====")
    print("1. Allot Student")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        student_name = input("Enter student name: ").strip()
        room_no = input("Enter room number: ").strip().upper()

        if not student_name:
            print("Student name cannot be empty!")
            continue

        try:
            message = allot(student_name, room_no)
            print(message)

        except InvalidRoomError as e:
            print("InvalidRoomError:", e)

        except RoomFullError as e:
            print("RoomFullError:", e)

        except DuplicateStudentError as e:
            print("DuplicateStudentError:", e)

    elif choice == "2":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")


# Display updated room details
print("\n===== Updated PG Room Details =====")

for room_no in rooms:
    print(room_no, "Capacity:", rooms[room_no],
          "Students:", room_students[room_no])



# ==========================================
# Task 4: Student Not Found Exception
# ==========================================

class StudentNotFoundError(Exception):
    pass


# Function to vacate a student
def vacate(student_name):

    for room in room_students:
        if student_name in room_students[room]:
            room_students[room].remove(student_name)
            return student_name + " successfully vacated from " + room

    raise StudentNotFoundError("Student not found!")


# Test vacate function
print("\n===== Vacate Student =====")

student_name = input("Enter student name to vacate: ")

try:
    message = vacate(student_name)
    print(message)

except StudentNotFoundError as e:
    print("StudentNotFoundError:", e)
