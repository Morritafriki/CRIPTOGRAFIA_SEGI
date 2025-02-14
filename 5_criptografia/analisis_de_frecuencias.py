# ---------------------------- Análisis de frecuencias (Cifrado Cesar) ----------------------

# FUNCIONES AUXILIARES
def cal_max(lis_des): 
    # Entrada: lista de dos dimensiones del tipo: [["a",14],["b",1],["c",45],....]
    # Salida: Lista con el valor máximo colocado en la primera posición: [["c", 45], ["b",1],["a",14],...]

    # Variables auxiliares
    max_ini = lis_des.copy() # Copiamos la lista para no afectar a la original
    max = lis_des[0][1] # Inicializamos el valor máximo con el primer valor de nuestra lista
    clave = lis_des[0][0] # Inicializamos la cavle con la primera clave de nuestra lista
    pos = 0 # Inicializamos la variable de posición a 0

    # Guardamos los datos relevantes del elemento maximo
    for i in range(len(lis_des)):
        if max <= lis_des[i][1]:
            max = lis_des[i][1]
            clave = lis_des[i][0]
            pos = i

    # Modificamos los valores para colocar en la primera posición los valores maximos
    max_ini[0][0] = clave
    max_ini[0][1] = max

    # El valor que ocupaba la primera posición se almacena en la posición donde esta el maximo
    max_ini[pos][0] = lis_des[0][0]
    max_ini[pos][1] = lis_des[0][1]

    return max_ini #Devuelve una lista

def ord_lis(lis_des):
    # Entrada: lista de dos dimensiones del tipo: [["a",14],["b",1],["c",45],....]
    # Salida: Lista ordenada de mayor a menor: [["c", 45], ["a",14],["b",1],...]

    # Variables auxiliares
    lis_ord = []
    lis_des_cop = lis_des.copy()

    # Vamos recorriendo la cadena original y almacenando el elemento mas grande en una lista nueva
    for i in range(len(lis_des) - 1):
        salida = cal_max(lis_des_cop)
        lis_ord.append(salida[0])
        lis_des_cop = salida[1:]

    # Añadimos el ultimo elemento de la lista
    lis_ord.append(salida[-1])

    return lis_ord # Devolvemos la lista ordenada

def cal_frq_let(cadena):
    # Entrada: cadena de texto con el contenido cifrado
    # Salida: lista de dos dimensiones indicando el número de veces que se repite cada caracter

    ele_sin_rep = list(set(cadena))
    var_rep = []
    # Contamos el numero de veces que se repite una letra dentro de la cadena original
    for let in ele_sin_rep:
        if let != " ":
            var_rep.append([let, cadena.count(let)])

    # Ordenamos la lista de elementos de mayor a menor segun su frecuencia
    var_rep_ord = ord_lis(var_rep)

    return var_rep_ord # Devolvemos la lista con la frecuencia de cada caracter 

def cal_clv_pro(ele_cad, ele_pro):
    # Entrada: cadena de texto con el contenido cifrado
    # Salida: lista de dos dimensiones indicando el número de veces que se repite cada caracter


    global abc
    abc = list("abcdefghijklmnñopqrstuvwxyz")
    pos_ele_cad = abc.index(ele_cad)
    pos_ele_pro = abc.index(ele_pro)
    if pos_ele_cad > pos_ele_pro:
        clv = len(abc) - pos_ele_cad + pos_ele_pro
    else:
        clv = pos_ele_pro - pos_ele_cad
    
    return clv

def descifrado_cesar(cad_cif, des):
    new_cad = ""

    if des >= len(abc):
        des = des % len(abc)

    for i in cad_cif:
        if i in abc:
            pos = max(max(abc.index(i) - des, 0), (abc.index(i) - des) % len(abc))
            new_cad += abc[pos]
        else:
            new_cad += " "

    return new_cad

def ana_frq(cadena, num_let_cad):

    global let_max_frq
    let_max_frq = ["e", "a", "o", "l", "s", "n", "d"]
    cadena = cadena.lower()
    lis_clv = []
    lis_var_rep = cal_frq_let(cadena)

    for i in range(num_let_cad):
        for j in range(len(let_max_frq)):
            ele_cad = lis_var_rep[i][0]
            ele_pro = let_max_frq[j]
            clv = cal_clv_pro(ele_cad, ele_pro)
            cad_des = descifrado_cesar(cadena, clv)
            lis_clv.append([ele_cad, ele_pro, clv ,cad_des])
    
    return lis_clv

def ejecuta():
    
    # Paso 1: Leer el contenido del archivo original
    ruta = "C://Users//trabajo//Documents//IES_Alberti//2_SMR//seg_inf//Tema2"
    with open(ruta + "//mensaje_cifrado.txt", "r") as archivo_lectura:
        contenido = archivo_lectura.read()  # Leer todo el contenido

    # Paso 2: Llamamos a la función que desencriptará el mensaje 
    cad_des_opc = ana_frq(contenido, 3)

    # Paso 3: Escribir el contenido en un archivo nuevo
    with open(ruta + "//archivo_salida.txt", "w") as archivo_escritura:
        elementos = ["Caracter + frecuente", "Caracter + probable", "Clave", "Cadena descifrada"]
        for i in range(len(cad_des_opc)):
            for j in range(len(elementos)):
                cad = elementos[j] + ": " + str(cad_des_opc[i][j]) + "\n"
                archivo_escritura.write(cad)  # Escribir el contenido leído en el nuevo archivo
            cad = 60*"-" + "\n"
            archivo_escritura.write(cad)

ejecuta()


