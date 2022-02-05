# lex_auth_012693782475948032141

def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0
    if food_type == "N":
        food_bill = 150 * quantity_ordered
    else:
        food_bill = 120 * quantity_ordered

    if distance_in_kms <= 3:
        delivery_bill = 0
    if distance_in_kms > 3 and distance_in_kms <= 6:
        delivery_bill = (distance_in_kms - 3) * 3
    if distance_in_kms > 6:

        delivery_bill = 9 + (distance_in_kms - 6) * 6

    bill_amount = food_bill + delivery_bill

    return bill_amount


# Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount = calculate_bill_amount("N", 2, 5)
print(bill_amount)
