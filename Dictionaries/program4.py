digit_word = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
}

def integer_to_words(number):
    
    number_str = str(number)
   
    words = [digit_word[int(digit)] for digit in number_str]
  
    result = " ".join(words)

    return result

number = int(input("Enter an integer: "))

words = integer_to_words(number)

print(words)
