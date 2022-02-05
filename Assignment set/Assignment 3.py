
def make_amount(rupees_to_make, no_of_five, no_of_one):
    five_needed = 0
    one_needed = 0

    five_needed = int(rupees_to_make/5)
    value_of_fives = five_needed * 5
    one_needed = rupees_to_make - value_of_fives

    if no_of_five >= five_needed and no_of_one >= one_needed:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)


make_amount(105, 20, 5)
