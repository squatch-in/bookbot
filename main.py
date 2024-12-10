#This function opens a file and returns and prints the contents of the file.
def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents  
book = main()
# print(book)

#This counts the number of words from the book function.
number_of_words = len(book.split())
# print(number_of_words)

# The book in all lowercase
lower_case_book = book.lower()

#filters of only alphabet
alphabet ="".join(c for c in lower_case_book if c.isalpha())
# print(alphabet)


from collections import Counter
def character_count(abc):
    return dict(Counter(abc))

letters = character_count(alphabet)
# print(letters)

# def counter(string):
#     counter = {}
#     for i in string:
#         if i not in counter:
#             counter[i] = 1
#         else:
#             counter[i] += 1
#     return counter
# counted = counter(lower_case_book)
# print(counted)
print("--- Begin report of books/frankenstein.txt ---")
print(f"{number_of_words} words found in document", end='\n\n')
for key in letters:
    # print (key, letters[key] )
    print(f"The '{key}' character was found {letters[key]} times")
print("--- End Report ---")