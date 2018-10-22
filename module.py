from collections import OrderedDict
#variables necesarias
symbols = ""
variables = ""
markers = ""
rules = ""
chain = ""

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

 #funcion que recibe los valores ingresados del texfield y textinput
def getValues(s,v,m,r,c):
    global symbols
    symbols = s
    global values
    values = v
    global markers
    markers = m
    global rules 
    rules = r
    global chain 
    chain = c

def getSymbols():
    return symbols

def getVariables():
    return variables

def getMarkers():
    return markers 

def getRules():
    return rules

def getChain():
    return chain

#funcion que valida si la hilera de entrada contiene los simbolos permitidos
def validateSymbols():
    flag = None
    searchMarkers()
    print(getChain() + " / " + getSymbols())
    for ch in getChain():
        if getSymbols().find(ch) == -1:
              if getMarkers().find(ch) == -1:
                flag = False
                break
        else: flag = True           
    return flag

def searchMarkers():
    num = 0
    mrs = []
    print(getMarkers() + "/" + getChain())
    for m in getMarkers():
        if (getChain().find(m) > -1):
            num = getChain().find(m)
            mrs.append(getChain()[num])
    return mrs         

def outFormat(t, b, e):
    title = t
    body = b + "\n" +"\n"+ "\n"+"\n"
    endline = e    
    return title + body + endline  

def resultados():
   print("escriba un valor a")
   a = input()
   print("escriba un valor b")
   b = input()
   print(multBinarios(a,b))
   
