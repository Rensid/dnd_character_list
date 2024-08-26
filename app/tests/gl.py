# def process(input_string: str) -> str:
#     upper_than_zero = 0
#     lower_than_zero = 0
#     zero = 0
#     list_of_values = [int(i) for i in input_string.split(" ")]
#     for value in list_of_values:
#         if value < 0:
#             lower_than_zero += 1
#         elif value > 0:
#             upper_than_zero += 1
#         elif value == 0:
#             zero += 1
#     return f"выше нуля: {upper_than_zero}, ниже нуля: {lower_than_zero}, равна нулю: {zero}"


# values = "5 -2 0 0 7 8 -1"
# res = process(values)
# print(res)


import random


def generate_secret_code():
    code = random.randint(100000, 999999)
    return code


print(generate_secret_code())
