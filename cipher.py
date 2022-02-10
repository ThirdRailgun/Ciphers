def cipher_ceasar_encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        if ord(letter.lower()) not in range(97,123):
            ciphertext += letter
            continue

        ciphered_letter_ascii = ord(letter.lower()) + (int(key) % 26)
        while ciphered_letter_ascii > 122: ciphered_letter_ascii -= 26

        if letter.isupper():
            ciphertext += chr(ciphered_letter_ascii).upper()
        else:
            ciphertext += chr(ciphered_letter_ascii)
    
    return ciphertext
            
    #return "".join([(chr(ord(letter) + (int(key) % 26))) for letter in str(plaintext)])
    #original attempt at list comprehension but it got too complex for its gracefulness.

def main():
    pass

if __name__ == "__main__":
    main()