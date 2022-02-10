def cipher_ceasar_encrypt(plaintext: str, key: int):
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

#current draft of the vigenere cipher.
#ISSUE: The vigenere cipher ignores spaces but the keystream does not.
def cipher_vigenere_encrypt(plaintext: str, key: str):
    ciphertext = ""
    keystream = []

    for letter in plaintext:
        if ord(letter.lower()) not in range(97,123):
            ciphertext += letter
            continue

    #generate keystream that needs to be the same length as the plaintext from the key.
    while (len(plaintext) > len(keystream)):
        keystream.extend(list(key))
    else:
        if len(plaintext) < len(keystream):
            keystream = keystream[:-(len(keystream)-len(plaintext))]

    #convert the keystream to numbers, 1-26
    keystream = [ord(k.lower()) - 96 for k in keystream]

    #print(keystream)
    #pass
    #call the caesar cipher as the vigenere is just an extension of that.
    for plaintext_letter, cipher_number in zip(plaintext, keystream):
        #print(type(plaintext_letter), type(plaintext_letter))
        ciphertext += cipher_ceasar_encrypt(plaintext_letter, cipher_number)

    return ciphertext

def main():
    print(cipher_vigenere_encrypt("The quick brown fox jumps over the lazy dog.", "key"))
    pass


if __name__ == "__main__":
    main()