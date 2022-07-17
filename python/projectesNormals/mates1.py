#la media de 3 números,
#-- * la suma de euros de una colección de monedas,
#-- * el volumen de la esfera,
#-- * el área de una corona circular,
#-- * la intercalación de pares,
#-- * la última cifra de un número,
#-- * la rotación de listas,
#-- * el rango de una lista,
#-- * sacar maximo y minimo de una array,
#-- * el reconocimiento de palíndromos,
#-- * la igualdad y diferencia de 3 elementos,
#-- * la igualdad de 4 elementos,
#-- * el máximo de 3 elementos,
#Ejercicios de programación funcional (2011–12)
#-- * el área de un triángulo mediante la fórmula de Herón.

def primero():
    numeros = [3,5,5]
    total = 0
    for x in numeros:
        total = total + x

    mitjana = total/len(numeros)
    print(mitjana)

def segundo():
    monedas = [3,5,5]
    total_euros = 0
    for x in monedas:
        total_euros = total_euros + x

    print(total_euros)

def tercero():
    #forumla: v = 4/3 . pi. r^3
    #supondremos que el diametro de la esfera es de 12cm (radio 6cm)

    volum = (4/3)*3.14*6**3
    print(volum)

def quarto():
    #formula: A= pi.(R^2-r^2)
    #supondremos que el Radio mayor es de 18 y el menor de 6

    Area = 3.14*((18**2)-(6**2))
    print(Area)

def quinto():
    #intercala [1,4] [3,2] == [1,3,4,2] (es un ejemplo del resultado a querer obtener)

    primero = [1,4]
    segundo = [3,2]
    tercero = []

    for x in range(len(primero)):
        tercero.append(primero[x])
        tercero.append(segundo[x])

    print(tercero)    

def sexto():
    #ejemplo de resultado a obtener: ultimaCifra 325 == 5   
    numero = 924234

    for x in str(numero):
        ultimoNumero = x

    print(ultimoNumero) 

def septimo():
    #ejemplo resultado a obtener: rota1 [3,2,5,7] == [2,5,7,3] (se mueven todo 1 hacia la izquierda)
    array = [3,2,5,7]  
    temp = array[0]
    largo_array = 0
    
    for x in range(len(array)):
        if(x < len(array)-1):
            array[x] = array[x+1] 
        largo_array = largo_array + 1     

    array[largo_array-1] = temp       

    print(array)        

#el numero 8 no lo se hacer

def noveno():
    # sacar el maximo y el minimo de los nombres de la array
    array = [3,2,7,5]
    maximo = 0
    minimo = 0

    for x in array:
        
        for y in array:
            if (x  < y):
                maximo = y
            if (x  > y):
                minimo = y    

    print(maximo) 
    print(minimo)           
            

noveno()    