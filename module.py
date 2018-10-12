from collections import OrderedDict

# 1- invertir una hilera
def invertirHilera(chain):
    return chain[::-1]

# 2- duplica una cadena
def duplicarHilera(chain):
    return chain * 2

# 3- valida si una cadena es un palidromo 
def esPalindromo(chain):
    standart = str(chain).lower().replace(' ','')
    return standart == standart[::-1]

# 4- convertir un número binario en su equivalente unario


# 5- suma de binarios
def sumaBinarios(a,b):
    return bin(int(a,2) + int(b,2))

# 6- triplicar numeros binarios
def triplicarBinarios(a,b):
    return bin(int(a,2) * 3)

# 7- multiplicacion binarios
def multBinarios(a,b):
    return bin(int(a,2) * int(b,2))

# 8- Realizar una suma de números decimales
def sumaDecimales(a,b):
    return float(a) + float(b)
   
# 9- esta funcion preserva el orden original de la cadena, 
# solo elimina los caracteres repetidos
def eliminaRepetido(chain):
    aux = set()    
    c = [x for x in chain if not (x in aux or aux.add(x))]
    return "".join(c)

# 10- verificar la estructura de una hilera que contenga únicamente paréntesis, 
# que se encuentren correctamente balanceados


def resultados():
   print("escriba un valor a")
   a = input()
   print("escriba un valor b")
   b = input()
   print(multBinarios(a,b)) 
