
def find_product_of_digits(usr):
    product_of_digits = 1
    tostring = str(usr)
    string_list = []
    in_list = []

    for num in range(0, len(tostring)):
        string_list.append(tostring[num])
        if("7" in string_list):
            index = string_list.index("7")
            string_list.pop(index)
            if index != 0:
                string_list.pop(index - 1)
    for num1 in range(0, len(string_list)):
        in_list.append(int(string_list[num1]))
        product_of_digits = product_of_digits * in_list[num1]
    return product_of_digits


# Provide different values for number and test your program
usr = input("Please enter the number ")
product_of_digits = find_product_of_digits(usr)
print("product of digits:", product_of_digits)
