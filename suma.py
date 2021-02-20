def suma(n):
    suma = 0
    while(n!=0):
        suma = suma+n
        n = n-1

    return suma


def sumarec(n):
    if n == 1:
        return 1
    return n+sumarec(n-1)

print(sumarec(5))