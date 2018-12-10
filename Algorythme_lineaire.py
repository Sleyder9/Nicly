# fibonachi
a = 0
b = 1
res = 0
fin = int(raw_input('Entrer une valeur limite : '))

while res < fin :
    print(res)
    res = a + b
    a = b
    b = res
