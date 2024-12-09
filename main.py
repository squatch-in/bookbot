#This function opens a file and returns and prints the contents of the file.
def main():
    with open ("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents  
book = main()
print(book)

#This counts the number of words from the book function.
number_of_words = len(book.split())
print(number_of_words)

