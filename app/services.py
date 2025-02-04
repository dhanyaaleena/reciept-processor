import math
from app.models import Receipt

def calculate_points(receipt: Receipt) -> int:
    points = 0

    # One point for every alphanumeric character in the retailer name
    points += sum(c.isalnum() for c in receipt.retailer)

    # Convert total to float for calculations
    total = float(receipt.total)

    # 50 points if the total is a round dollar amount with no cents
    if total.is_integer():
        points += 50

    # 25 points if the total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # 5 points for every two items on the receipt
    points += (len(receipt.items) // 2) * 5

    # Points for item descriptions that are multiples of 3
    for item in receipt.items:
        trimmed_desc = item.shortDescription.strip()
        if len(trimmed_desc) % 3 == 0:
            price = float(item.price)
            points += math.ceil(price * 0.2)

    # 6 points if the day in the purchase date is odd
    purchase_day = int(receipt.purchaseDate.split("-")[2])
    if purchase_day % 2 == 1:
        points += 6

    # 10 points if the time of purchase is between 2:00 PM and 4:00 PM
    purchase_hour, purchase_minute = map(int, receipt.purchaseTime.split(":"))
    if 14 <= purchase_hour < 16:
        points += 10

    return points
