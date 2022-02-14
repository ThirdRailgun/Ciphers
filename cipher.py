import re
import string

def caesar_encrypt(plaintext: str, key: int):
    ciphertext = []

    for letter in plaintext:
        if letter.isalpha() == False:
            ciphertext.append(letter)
            continue

        ciphered_letter_ascii = ord(letter.lower()) + int(key)
        while ciphered_letter_ascii > 122: ciphered_letter_ascii -= 26 #122 refers to z on the ASCII table.
        while ciphered_letter_ascii < 97: ciphered_letter_ascii += 26 #97 refers to a on the ASCII table.

        if letter.isupper():
            ciphertext.append(chr(ciphered_letter_ascii).upper())
        else:
            ciphertext.append(chr(ciphered_letter_ascii))
    
    return "".join(ciphertext)

    #return "".join([(chr(ord(letter) + (int(key) % 26))) for letter in str(plaintext)])
    #original attempt at list comprehension but it got too complex for its gracefulness.

def caesar_decrypt(ciphertext: str):
    return [caesar_encrypt(ciphertext, key) for key in range(1, 27)]

def a1z26_encrypt(plaintext: str):
    plaintext = plaintext.upper() #A1Z26 does not distinguish between upper and lower cases.
    ciphertext = []

    #https://stackoverflow.com/questions/367155/splitting-a-string-into-words-and-punctuation
    for word in re.findall(r"[\w']+|[.,!?;]", plaintext):
        ciphertext_word = []

        for letter in word:
            if letter.isalpha() == False:
                ciphertext_word.append(letter)
                continue

            ciphertext_word.append(str(ord(letter) - 64))
        
        ciphertext.append("-".join(ciphertext_word))

    #side effect of pretending that punctuation is its own word is that it gets joined with spaces as well.
    ciphertext = " ".join(ciphertext)
    for punctuation in string.punctuation:
        ciphertext = ciphertext.replace(" " + punctuation, punctuation)

    return ciphertext

        #ciphertext.append(" ".join("-".join(ciphertext_word))) #there is a dash between each letter but not each word to distinguish 26, 2, 6

    #return #"".join(ciphertext)

# #current draft of the vigenere cipher. there's still something wrong with this?
# def vigenere_encrypt(plaintext: str, key: str):
#     ciphertext = ""

#     for i, letter in enumerate(plaintext):
#         if ord(letter.lower()) not in range(97,123):
#             ciphertext += letter
#             continue

#         ciphertext += ceasar_encrypt(letter, a1z26_encrypt(letter))
#     return ciphertext    

def main():
    pass


if __name__ == "__main__":
    main()