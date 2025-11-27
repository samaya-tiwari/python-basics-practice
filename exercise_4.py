
# Exercise 4: Word Counter

def wordcounter(text):
    total = text.split()
    return total

user_text = input('Enter the text: ')
words = wordcounter(user_text)
print("Total number of words in the text is", len(words))