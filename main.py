#This function opens a file and returns and prints the contents of the file.
def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents  
book = main()
# print(book)

#This counts the number of words from the book function.
number_of_words = len(book.split())
print(number_of_words)

# The book in all lowercase
lower_case_book = book.lower()
# print(lower_case_book)

from collections import Counter
def character_count(abc):
    return dict(Counter(abc))

letters = character_count(lower_case_book)
print(letters)