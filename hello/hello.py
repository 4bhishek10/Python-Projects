
def find_sum_of_digits(number):
    sum_of_digits = 0
    tostring = str(number)
    string_list = []
    in_list = []
    for num in range(0, len(tostring)):
        string_list.append(tostring[num])
    for num1 in range(0, len(tostring)):
        in_list.append(int(string_list[num1]))
        sum_of_digits = sum_of_digits + in_list[num1]
    return sum_of_digits


# Provide different values for number and test your program
sum_of_digits = find_sum_of_digits(12345)
print("Sum of digits:", sum_of_digits)
