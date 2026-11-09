# ==========================================
# Task 2: Test Hardware Shop Stock
# ==========================================

import hardware_shop.stock as stock


# Display Available Stock
print("Cement Stock:", stock.check_stock("Cement"))

print("Paint Stock:", stock.check_stock("Paint"))


# Reduce Stock
remaining = stock.reduce_stock("Cement", 10)

print("Remaining Cement Stock:", remaining)


# Test Failing Request
try:

    stock.reduce_stock("Cement", 100)

except stock.OutOfStockError as error:

    print("Error:", error)


# Display Updated Stock
print("Updated Cement Stock:", stock.check_stock("Cement"))