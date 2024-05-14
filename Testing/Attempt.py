def convert_to_binary(num):
    binary_num = ""
    while num > 0:
        remainder = num % 2
        binary_num = str(remainder) + binary_num
        num = num // 2
    return binary_num

num = 10
binary_num = convert_to_binary(num)
print(binary_num)