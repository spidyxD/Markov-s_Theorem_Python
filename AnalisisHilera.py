from Regla import Regla

def getRules(rule):
    rules = []
    aux = [] 
    rule = rule.strip().split()
    for r in rule:
        aux.append(r)

    for a in aux:
        entrada = a[0:a.find("→")]
        #print(entrada)
        salida =  a[a.find("→")+1:len(a)]
        #print(salida)
        rules.append(Regla(entrada,salida))      
    return rules    



def AnalisisHilera(hilera,rules):
    Reglas = getRules(rules)
    for r in getRules(rules):
      print("entrada: "+r.entrada +" / " +"salida: "+r.salida)  
    reglaAct = 0 #La regla a evaluar en la lista de Reglas
    ini = 0 #inicio de la parte de la hilera que se va a evaluar con la regla
    fin = ini + Reglas[reglaAct].getEntrada().__len__() #final de la parte de la hilera que se va a evaluar con la regla
    while(reglaAct < Reglas.__len__()+1): #revision de toda la lista de Reglas
        while(fin < str(hilera).__len__()+1): #revision de toda la hilera
            if(Reglas[reglaAct].getEntrada().__len__() > hilera.__len__()):
                # si la hilera es mas pequeña a la regla a aplicar, se pasa a la siguiente regla
                reglaAct = reglaAct + 1
                ini = 0
                fin = ini + Reglas[reglaAct].getEntrada().__len__()
            else:
                #se evalua su se aplica la regla
                if(Reglas[reglaAct].getEntrada() == hilera[ini:fin]): #si la regla y la parte de la hilera son iguales, se cambian
                    if(ini == 0): #si el match esta al inicio de la hilera, se usa la entrada de la regla y se concatena al resto de la hilera
                        hilera = Reglas[reglaAct].getSalida() + hilera[fin:hilera.__len__()]
                        ini = 0
                        reglaAct = 0
                        fin = ini + Reglas[reglaAct].getEntrada().__len__()
                    else: #si no, se agarra la entrada y se concatena al pedazo antes y despues de la porcion que acabo de reemplazar
                        hilera = hilera[0:ini] + Reglas[reglaAct].getSalida() + hilera[fin:hilera.__len__()]
                        ini = 0
                        reglaAct = 0
                        fin = ini + Reglas[reglaAct].getEntrada().__len__()
                else: #si no son iguales, se pasa busca en el siguiente pedazo de la hilera
                    ini = ini + 1
                    fin = ini + Reglas[reglaAct].getEntrada().__len__()
        reglaAct = reglaAct + 1
        ini = 0
        if(reglaAct < Reglas.__len__()):
            fin = ini + Reglas[reglaAct].getEntrada().__len__()
        else:
            return hilera
    print(hilera)        
    return hilera


