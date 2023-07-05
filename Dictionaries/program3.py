""" Generate a dictionary where keys are numbers and values consist of a set of its factors in a specified range.

Factors = {1:{1} , 2:{1,2}, 3: {1,3}, 4:{1,2,4} , 5:{1,5}, 6:{1,2,3,6}, 7:{1,7}, 8:{1,2,4,8}, 9:{1,3,9,}} """


def generate_factors_dictionary(start, end):
    factors = {}
    for num in range(start, end + 1):
        factors[num] = {i for i in range(1, num + 1) if num % i == 0}
    return factors


start_range = 1
end_range = 9

factors_dict = generate_factors_dictionary(start_range, end_range)

print("Factors:", factors_dict)
