# ==========================================
# Task 1: Test Hardware Shop Pricing
# ==========================================

# Import Functions from Pricing Module
from hardware_shop.pricing import gst_amount, boxes_needed, round_down_to_five


# Test GST Amount
print("GST Amount:", gst_amount(1000))


# Test Required Boxes
print("Boxes Needed:", boxes_needed(120, 50))


# Test Round Down to Five
print("Rounded Amount:", round_down_to_five(1237))
