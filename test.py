import unittest
import cipher
import string

class test_cipher_caesar(unittest.TestCase):

    def test_encrypt1(self):
        assert cipher.cipher_caesar_encrypt("A", "1") == "B"
    
    def test_encrypt2(self):
        assert cipher.cipher_caesar_encrypt("a", "1") == "b"

    def test_encrypt3(self):
        assert cipher.cipher_caesar_encrypt("A", "26") == "A"

    def test_encrypt4(self):
        assert cipher.cipher_caesar_encrypt("a", "26") == "a"

    def test_encrypt5(self):
        assert cipher.cipher_caesar_encrypt("A", "3056") == "O"

    def test_encrypt6(self):
        assert cipher.cipher_caesar_encrypt("a", "-6") == "u"

    def test_error(self):
        with self.assertRaises(ValueError):
            cipher.cipher_caesar_encrypt("A", "A") == "A"

    def test_punctuation1(self):
        assert cipher.cipher_caesar_encrypt(string.punctuation, "1") == string.punctuation

    def test_punctuation2(self):
        assert cipher.cipher_caesar_encrypt(string.punctuation, "46") == string.punctuation
    
    def test_real(self):
        assert cipher.cipher_caesar_encrypt("The quick brown fox jumps over the lazy dog.", "23") == "Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald."

    def test_decrypt(self):
        assert cipher.cipher_caesar_decrypt("Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald.") == [
            "Rfc osgai zpmul dmv hsknq mtcp rfc jyxw bme.",
            "Sgd pthbj aqnvm enw itlor nudq sgd kzyx cnf.",
            "The quick brown fox jumps over the lazy dog.",
            "Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.",
            "Vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi.",
            "Wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj.",
            "Xli uymgo fvsar jsb nyqtw sziv xli pedc hsk.",
            "Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl.",
            "Znk waoiq hxuct lud pasvy ubkx znk rgfe jum.",
            "Aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.",
            "Bpm ycqks jzwev nwf rcuxa wdmz bpm tihg lwo.",
            "Cqn zdrlt kaxfw oxg sdvyb xena cqn ujih mxp.",
            "Dro aesmu lbygx pyh tewzc yfob dro vkji nyq.",
            "Esp bftnv mczhy qzi ufxad zgpc esp wlkj ozr.",
            "Ftq cguow ndaiz raj vgybe ahqd ftq xmlk pas.",
            "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.",
            "Hvs eiwqy pfckb tcl xiadg cjsf hvs zonm rcu.",
            "Iwt fjxrz qgdlc udm yjbeh dktg iwt apon sdv.",
            "Jxu gkysa rhemd ven zkcfi eluh jxu bqpo tew.",
            "Kyv hlztb sifne wfo aldgj fmvi kyv crqp ufx.",
            "Lzw imauc tjgof xgp bmehk gnwj lzw dsrq vgy.",
            "Max jnbvd ukhpg yhq cnfil hoxk max etsr whz.",
            "Nby kocwe vliqh zir dogjm ipyl nby futs xia.",
            "Ocz lpdxf wmjri ajs ephkn jqzm ocz gvut yjb.",
            "Pda mqeyg xnksj bkt fqilo kran pda hwvu zkc.",
            "Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald."
        ]

# class test_cipher_vigenere(unittest.TestCase):
#     def test_encrypt1(self):
#         assert cipher.cipher_vigenere_encrypt("The quick brown fox jumps over the lazy dog.", "password") == "Ihw iqwtn qrgoj tfa yueho cmhg tzw hoqb soy."

if __name__ == '__main__':
    unittest.main()