
a, b, c = list(map(int, input().split()))

def mul(a, b):
    if b == 1:
        return a % c
    temp = mul(a, b // 2)
    if b % 2 == 0:
        return temp * temp % c
    else : 
        return temp * temp * a % c
    
print(mul(a, b))
