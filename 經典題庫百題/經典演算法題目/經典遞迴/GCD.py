# 遞迴 #GCD

a = 10
b = 12

'''
GCD(a, b):

a%b==0: b
else: GCD(b, a%b)

'''

def GCD(a, b):
    if a%b==0:
        return b
    else:
        return GCD(b, a%b)


print(GCD(a, b))
