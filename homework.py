#coding:utf-8

alpha = "abcdefghijklmnopqrstuvwxyz"

def BruteForceAttack(ciphertext):
    for key in range(len(alpha)):
        plaintext = ''
        for i in ciphertext:
            if i in alpha:
                num = alpha.find(i)
                num = num - key

                if num < 0:
                    num = num + len(alpha)

                plaintext = plaintext + alpha[num]

            else:
                plaintext = plaintext + i
        print("key %s : %s" %(key,plaintext))
    
BruteForceAttack("fabuoe uz eqogdufk fqotzaxask")