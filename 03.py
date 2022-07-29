from secretpy import Playfair, CryptMachine
from secretpy.cmdecorators import UpperCase

from sage.combinat.words import alphabet


def encdec(machine, plaintext):
    print(plaintext)
    enc = machine.encrypt(plaintext)
    print(enc)
    dec = machine.decrypt(enc)
    print(dec)
    print("----------------------------------")


cm = UpperCase(CryptMachine(Playfair()))
key = [
    "t", "u", "e", "s", "d",
    "a", "y", "o", "b", "c",
    "f", "g", "h", "i", "k",
    "l", "m", "n", "p", "q",
    "r", "v", "w", "x", "z",
]
cm.set_alphabet(alphabet)
plaintext = u"Hide the gold in the tree stump"
encdec(cm, plaintext)

plaintext = "sometext"
encdec(cm, plaintext)

plaintext = "this is a secret message"
encdec(cm, plaintext)

plaintext = "classicalcryptography"
encdec(cm, plaintext)