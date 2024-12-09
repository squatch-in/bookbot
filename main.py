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

def character_count():
    all_characters = {}
    unique_set = set()
    for character in lower_case_book:
        if character not in unique_set:
            unique_set.add(character)
            
    
    

    

character_count()