# ==========================================
# Task 4: Hardware Shop Billing System
# ==========================================

# Import pricing module
import hardware_shop.pricing as pricing

# Import stock functions and custom exception
from hardware_shop.stock import reduce_stock, OutOfStockError

# Import bill number function
from hardware_shop import new_bill_number


# Create function to generate customer bill
def create_bill(customer_name, item, quantity, box_size, price):

    bill_number = new_bill_number()

    # Calculate required boxes
    boxes = pricing.boxes_needed(quantity, box_size)

    print("\n===================================")
    print("          HARDWARE SHOP BILL")
    print("===================================")
    print("Customer Name:", customer_name)
    print("Bill Number:", bill_number)
    print("Item:", item)
    print("Boxes:", boxes)

    try:
        # Reduce available stock
        reduce_stock(item, boxes)

        # Calculate amount and GST
        amount = boxes * price
        gst = pricing.gst_amount(amount)

        # Calculate final total rounded down to multiple of 5
        total = pricing.round_down_to_five(amount + gst)

        print("Amount: ₹", amount)
        print("GST (18%): ₹", gst)
        print("Total: ₹", total)
        print("===================================")

    except OutOfStockError as error:
        print("Stock Error:", error)
        print("Bill could not be completed.")
        print("===================================")


# Customer 1
create_bill("Rahul", "Cement", 120, 50, 350)

# Customer 2
create_bill("Nidhi", "Paint", 40, 10, 800)

# Customer 3 - Requests more boxes than available stock
create_bill("Sahil", "Cement", 2600, 50, 350)