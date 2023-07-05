""" Write a program that inverts a dictionary. I.e., it makes key of one dictionary value of another and vice versa

Sample Input:
Dict={‘Reg.No”:123, ‘Name’:’abc’,Course’:’CSE’}
Sample Output:
Inv Dict={123:’Reg.No’, ‘abc’ : ‘Name’, ‘CSE’: ‘Course’} """


def invert_dictionary(dictionary):
    inverted_dict = {value: key for key, value in dictionary.items()}
    return inverted_dict


input_dict = {'Reg.No': 123, 'Name': 'abc', 'Course': 'CSE'}

inverted_dict = invert_dictionary(input_dict)

print("Inverted Dict:", inverted_dict)
