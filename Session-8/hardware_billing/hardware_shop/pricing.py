# ==========================================
# Hardware Shop Pricing Module
# ==========================================

import math


# Calculate GST Amount
def gst_amount(amount, rate=18):
    return amount * rate / 100


# Calculate Required Boxes
def boxes_needed(quantity, box_size):
    return math.ceil(quantity / box_size)


# Round Down Amount to Nearest Five
def round_down_to_five(amount):
    return math.floor(amount / 5) * 5
