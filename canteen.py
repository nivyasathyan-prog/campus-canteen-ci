def calculate_total(subtotal):
    """
    Calculate the final canteen bill.

    Rules:
    - Apply 10% discount if subtotal is above Rs. 300.
    - Apply 5% GST after the discount.
    - Return the final amount rounded to 2 decimal places.
    """

    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")

    discount = 0

    if subtotal > 300:
        discount = subtotal * 0.10

    discounted_amount = subtotal - discount

    gst = discounted_amount * 0.05

    final_amount = discounted_amount + gst

    return round(final_amount, 2)