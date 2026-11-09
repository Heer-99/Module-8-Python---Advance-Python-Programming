# ==========================================
# Task 2: Hardware Shop Stock Management
# ==========================================


# Create Custom Exception
class OutOfStockError(Exception):
    pass


# Dictionary to Store Hardware Items
hardware_items = {
    "Cement": {"quantity": 50, "price": 350},
    "Paint": {"quantity": 30, "price": 800},
    "Bricks": {"quantity": 100, "price": 10},
    "Tiles": {"quantity": 40, "price": 600},
    "Pipes": {"quantity": 25, "price": 450},
    "Nails": {"quantity": 60, "price": 120},
    "Wires": {"quantity": 35, "price": 500},
    "Tools": {"quantity": 20, "price": 900}
}


# Function to Check Stock
def check_stock(item):

    if item in hardware_items:
        return hardware_items[item]
    else:
        return None


# Function to Reduce Stock
def reduce_stock(item, qty):

    if item not in hardware_items:
        raise OutOfStockError("Item does not exist!")

    if qty > hardware_items[item]["quantity"]:
        raise OutOfStockError("Not enough stock available!")

    hardware_items[item]["quantity"] -= qty

    return hardware_items[item]["quantity"]