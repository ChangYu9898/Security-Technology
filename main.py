
alpha="abcdefghijklmnopqrstuvwxyz"

def is_alpha_char(c):
    return (c.lower() in alpha)

def get_alpha_index(c):
    return alpha.index(c.lower())

def get_key_index(c,key):
    return key.index(c.upper())

def encrypt_ma(k, plaintext):
     ciphertext = ""
     if len(k)==26:
         key=k
         for j in range(len(plaintext)):
             p=plaintext[j]
             if is_alpha_char(p):
                 x = get_alpha_index(p)
                 c = key[x]
             else:
                 c = p
             ciphertext +=c
         return ciphertext
     else:
         print("wrong key size")

def decrypt_ma(k, ciphertext):
     plaintext = ""
     if len(k)==26:
         key=k
         for j in range(len(ciphertext)):
             c=ciphertext[j]
             if is_alpha_char(c):
                 x = get_key_index(c,key)
                 p = alpha[x]
             else:
                 p = c
             plaintext +=p
         return plaintext
     else:
         print("wrong key size")


#### Example  ###################
### k="DKVQFIBJWPESCXHTMYAUOLRGZN"
## myplaintext = "IfwewIshtoreplaceletters"
## encrypt_ma(k, myplaintext)
## ciphertext ="WIRFRWAJUHYFTSDVFSFUUFYA"
## decrypt_ma(k, ciphertext)