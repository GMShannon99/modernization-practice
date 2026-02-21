import random

def generate_random_list(min_value: int, max_value: int, length: int) -> list:
    result_list = []
    for i in range(0, length):
        result_list.append(random.randint(min_value, max_value))

    return result_list

rlst = generate_random_list(1, 3, 5)
print(rlst)  