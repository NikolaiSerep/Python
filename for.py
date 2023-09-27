for i in range(10,99):
    a = i%10
    b = i//10
    if 2*(a*b) == i:
        print(f'{i}:  2*({a}*{b})={a}*{b}')
    