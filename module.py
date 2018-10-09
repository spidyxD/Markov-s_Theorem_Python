from collections import OrderedDict
#duplica una cadena
def duplicarHilera(chain):
    return chain * 2

#valida si una cadena es un palidromo 
def esPalindromo(chain):
    standart = str(chain).lower().replace(' ','')
    return standart == standart[::-1]

#suma de binarios
def sumaBinarios(a,b):
    return bin(int(a,2) + int(b,2))

#multiplicacion binarios
def multBinarios(a,b):
    return bin(int(a,2) * int(b,2))
   
#esta funcion preserva el orden original de la cadena, solo elimina los caracteres repetidos
def eliminaRepetido(chain):
    aux = set()    
    c = [x for x in chain if not (x in aux or aux.add(x))]
    return "".join(c)

def resultados():
   print("escriba un valor a")
   a = input()
   print("escriba un valor b")
   b = input()
   print(multBinarios(a,b)) 
