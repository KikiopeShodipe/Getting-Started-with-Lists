# function to check weather
#first and last character of words match
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
        print("List of words with first and last character same \n", lst)
        return ctr
    # Ask the user for input
user_input = input("Enter words separated by spaces: ")
words_list = user_input.split()
count = match_words(words_list)
print("Number of words having first and last character same:", count)