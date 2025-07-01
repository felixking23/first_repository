def sumar(a,b):
    return a + b

while True:
    try:
        num1 = int(input("Ingrese un numero")) 
        num2 = int(input("Ingrese un numero"))
        break
    except:
        print("Recuerda ingresar numeros")

    result = sumar()
    print(result)
