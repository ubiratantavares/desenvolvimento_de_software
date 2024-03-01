numero1 = 5

# combinando if com operadores logicos
if 0 <= numero1 and numero1 <= 6:
    print(numero1)

# multiplas condicoes com or e and
nota = 80
presenca = 70

if nota < 70 or presenca < 70:
    print("Você não passou")
    if nota < 70:
        print("Tente melhorar sua nota")
    if presenca < 70:
        print("Você deveria ter ido mais às aulas")
else:
    print("Você passou")
    
    if nota == 100 and presenca == 100:
        print("Aprovado com louvor")
    elif (nota > 80 and nota < 90) and (presenca > 80 and presenca < 90):
        print("Bom trabalho")
    
    if nota >= 90:
        print("Excelente nota")
    elif (nota > 80 and nota < 90):
        print("Boa nota")

    if nota < 75:
        print("Quase que fica reprovado por nota. Tente se dedicar mais as suas notas.")
    
    if presenca < 75:
        print("Quase que fica reprovado por presença. Tente comparecer mais as aulas.")