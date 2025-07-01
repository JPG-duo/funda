def sumar(a,b):
    return a+b

while True:
    try:

        n1 = int(input("Ingese valor"))
        n2 = int(input("Ingese valor"))
        break
    except:
        print("repite")

print(sumar(n1,n2))