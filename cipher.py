def cipher_caesar_encrypt(plaintext: str, key: int):
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

def cipher_caesar_decrypt(ciphertext: str):
    return [cipher_caesar_encrypt(ciphertext, key) for key in range(1, 27)]
            
    #return "".join([(chr(ord(letter) + (int(key) % 26))) for letter in str(plaintext)])
    #original attempt at list comprehension but it got too complex for its gracefulness.

# #perhaps flesh this cipher out first.
# def cipher_a1z26_encrypt(plaintext: str):
#     ciphertext = []
#     for letter in plaintext:
#         if ord(letter.lower()) not in range(97,123):
#             ciphertext.append(letter)
#             continue
#         ciphertext.append(str(ord(letter.lower())-96))
#     return "".join(ciphertext)

# #current draft of the vigenere cipher. there's still something wrong with this?
# def cipher_vigenere_encrypt(plaintext: str, key: str):
#     ciphertext = ""

#     for i, letter in enumerate(plaintext):
#         if ord(letter.lower()) not in range(97,123):
#             ciphertext += letter
#             continue

#         ciphertext += cipher_ceasar_encrypt(letter, cipher_a1z26_encrypt(letter))
#     return ciphertext    

def main():
    pass


if __name__ == "__main__":
    main()