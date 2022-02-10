import unittest
import cipher
import string

class test_cipher_caesar(unittest.TestCase):

    def test_encrypt1(self):
        assert cipher.cipher_ceasar_encrypt("A", "1") == "B"
    
    def test_encrypt2(self):
        assert cipher.cipher_ceasar_encrypt("a", "1") == "b"

    def test_encrypt3(self):
        assert cipher.cipher_ceasar_encrypt("a", "26") == "a"

    def test_encrypt4(self):
        assert cipher.cipher_ceasar_encrypt("A", "26") == "A"

    def test_encrypt5(self):
        assert cipher.cipher_ceasar_encrypt("A", "3056") == "O"

    def test_error(self):
        with self.assertRaises(ValueError):
            cipher.cipher_ceasar_encrypt("A", "A") == "A"

    def test_punctuation1(self):
        assert cipher.cipher_ceasar_encrypt(string.punctuation, "1") == string.punctuation

    def test_punctuation2(self):
        assert cipher.cipher_ceasar_encrypt(string.punctuation, "46") == string.punctuation
    
    def test_real(self):
        assert cipher.cipher_ceasar_encrypt("The quick brown fox jumps over the lazy dog.", "23") == "Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald."

class test_cipher_vigenere(unittest.TestCase):
    def test_encrypt1(self):
        assert cipher.cipher_vigenere_encrypt("The quick brown fox jumps over the lazy dog.", "key") == "Dlc aygmo zbsux jmh nswtq yzcb xfo pyjc byk."

if __name__ == '__main__':
    unittest.main()