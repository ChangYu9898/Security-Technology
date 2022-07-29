import numpy as np
from sage.crypto.block_cipher.des import DES
des = DES()
import re
message = 'WISHINGYOUGOODLUCKINTHISCOURSEANDALLOTHERCOURSESOFYOURPROGRAM'
def convert(message):
    out = []
    for i in range(len(message)):
        x = ord(message[i])-65
        if i==0:
            out.append("0x%02x" % x)
        else:
            out.append(format(int(hex(x),16),'x').zfill(2).upper())
    out_1 = "".join(out)
    str = out_1[2:]
    str=re.findall(r'.{16}|.+',str)
    for i in range(len(str)):
        str[i]='0x'+str[i]
    return str


P = convert(message)
#P = ['0x16081207080D0618', '0x0E14060E0E030B14', '0x020A080D13070812', '0x020E14111204000D', '0x03000B0B0E130704', '0x11020E1411120412', '0x0E05180E14110F11', '0x0E0611000C']
K = 0x1F08260D1AC135E
for i in range(len(P)):
    P[i]= hex(int(P[i],16))
    C = des.encrypt(plaintext=int(P[i],16), key=K)
    C.hex()


