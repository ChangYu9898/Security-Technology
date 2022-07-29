ans = []
#for x in range(0,3127):
    #if(x**17%3127==x):
        #ans.append(x)
#print(ans)
#x=200**50&841
#print(x)
def fastExpMod(b, e, m):
    result = 1
    while e != 0:
        if (e&1) == 1:
            # ei = 1, then mul
            result = (result * b) % m
        e >>= 1
        # b, b^2, b^4, b^8, ... , b^(2^n)
        b = (b*b) % m
    return result

print(fastExpMod(200,205,551))
