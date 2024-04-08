import random

def ValidaCPF(CPF): 
    CodVerificador = CPF[9] + CPF[10]

    cont_Multiplicador = 10
    soma_Resultado = 0

    for index in range(0, len(CPF)-2):  
        for caracter in CPF[index]:
                caracter = int(caracter)    
                resultado = caracter * cont_Multiplicador
                cont_Multiplicador -= 1
                soma_Resultado = resultado + soma_Resultado

    CaracterValidador01 = soma_Resultado % 11 
    CaracterValidador01 -= 11
    CaracterValidador01 = abs(CaracterValidador01) 

    if CaracterValidador01 >= 10:
        CaracterValidador01 = 0

    CaracterValidador01 = str(CaracterValidador01)


    cont_Multiplicador = 11
    soma_Resultado = 0

    for index in range(0, len(CPF)-1):  
        for caracter in CPF[index]:
                caracter = int(caracter)  
                resultado = caracter * cont_Multiplicador
                cont_Multiplicador -= 1 
                soma_Resultado = resultado + soma_Resultado

    CaracterValidador02 = soma_Resultado % 11 
    CaracterValidador02 -= 11
    CaracterValidador02 = abs(CaracterValidador02)

    if CaracterValidador02 >= 10:
        CaracterValidador02 = 0

    CaracterValidador02 = str(CaracterValidador02)


    if CaracterValidador01 + CaracterValidador02 == CodVerificador:   
        return True
    else:
        return False

def FormatarCPF(CPF):
    formatedCPF = CPF[0:3] + "." + CPF[3:6] + "." + CPF[6:9] + "-" + CPF[9:]
    return formatedCPF

def GerarCPF():
    while True:
        CPF = ""
        while len(CPF) != 11:
            num = str(random.randint(0, 9))       
            CPF += num
        if ValidaCPF(CPF):
            return CPF
            break
       

CPF = GerarCPF()

if ValidaCPF(CPF):
    print(f"Cpf: {FormatarCPF(CPF)} válido! ✅")
else:
    print(f"Cpf: {FormatarCPF(CPF)} inválido! ❌")

