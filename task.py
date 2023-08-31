def create_inator_word(word):
    vowels = 'aeiouAEIOU'
    ending = "inator" if word[-1] not in vowels else "-inator"
    length = len(word)
    result = f"{word}{ending} {length}000"
    return result
user_input = input("Enter the word: ")# Input 
output = create_inator_word(user_input)
print(output)
