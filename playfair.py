def init(key):
    table = [[0 for i in range(5)]for j in range(5)]
    index = [[0 for i in range(2)] for i in range(26)]
    sign = [0 for i in range(26)]
    colum = 0
    j = 0
    for i in range(len(key)):
        if(key[i] == 'j' or sign[ord(key[i]) - 97] == 1):
            continue
        table[colum][j] = key[i]
        index[ord(key[i]) - 97][0] = colum
        index[ord(key[i]) - 97][1] = j
        sign[ord(key[i]) - 97] = 1
        j += 1
        if(j == 5):
            j = 0
            colum += 1
    i = 0
    while colum < 5:
        while j < 5:
            while sign[i] == 1 or i == 9:
                i += 1
            table[colum][j] = chr(i + 97)
            index[i][0] = colum
            index[i][1] = j
            j += 1
            i += 1
        colum += 1
        j = 0
    return table,index
#进行加密
def encrypt(tab,index,str):
    ciphertext = ''
    while str[0] == 'j':
        str = str[:len(str)]
    for i in range(1,len(str),1):
        if(str[i] == 'j'):
            str = str[:i] + 'i' + str[i + 1:]
            continue
        if(str[i - 1] == str[i]):
            if(str[i - 1] == 'q'):
                str = str[:i] + 'x' + str[i:]
            str = str[:i] + 'q' + str[i:]
    if(len(str) % 2):
        str += 'x'
    for i in range(0,len(str),2):
        temp1 = ord(str[i]) - 97
        temp2 = ord(str[i + 1]) - 97
        x1 = index[temp1][0]
        x2 = index[temp2][0]
        y1 = index[temp1][1]
        y2 = index[temp2][1]
        if(x1 != x2 and y1 != y2):
            ciphertext += tab[x1][y2]
            ciphertext += tab[x2][y1]
        elif x1 == x2:
            if y1 == 4:
                ciphertext += tab[x1][0]
            else:
                ciphertext += tab[x1][y1 + 1]
            if y2 == 4:
                ciphertext += tab[x2][0]
            else:
                ciphertext += tab[x2][y2 + 1]
        else:
            if x1 == 4:
                ciphertext += tab[0][y1]
            else:
                ciphertext += tab[x1 + 1][y1]
            if x2 == 4:
                ciphertext += tab[0][y2]
            else:
                ciphertext += tab[x2 + 1][y2]
    return ciphertext
#用telegram作为密钥加密明文s
def main():
    tab,index = init('tuesdayo')
    s = 'classicalcryptography'
    print(encrypt(tab,index,s))

main()