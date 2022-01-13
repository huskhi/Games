""""
Hello! Khushi here.welcome to Ceasar's world!
"""
import string
def encrypt (text , key):
    whitespace = " "
    newletter = 0
    punc = string.punctuation
    for letter in text:
        if letter.isupper():
            newletter = chr((ord(letter)+ key -65)%26 + 65)
        if letter.islower():
            newletter = chr((ord(letter)+ key -97)%26 + 97)
        if letter.isnumeric():
            newletter = int(letter) + key
        if letter == whitespace:
            newletter= letter
        else:
            for i in range(len(punc)):
                if letter == punc[i] :
                    newletter=  chr((ord(letter)+ key -33)% 14+ 33)
        print(newletter, end = "")

text = input("enter the text to be encrypted\n")
key = int(input("enter encryption key number\n"))
print("Encypted word is ")
encrypt(text, key)