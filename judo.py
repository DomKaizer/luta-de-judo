ippon=10
wazaari=5
golpe=3
ganhar=10
lutador1=0
lutador2=0

escolha=0

print("prezado juiz bem vindo..")
print("registre abaixo o golpe aplicado pelos dois lutadores ")

while lutador1<ganhar:
    print("para registrar a pontuação registre na lista abaixo")
    print("\n1-ippon\n2-waza-ari\n3-golpe")
    escolha=int(input("golpe a ser registrado pra o lutador1..."))
    if ( escolha==1):
        lutador1+=ippon
    elif(escolha==2):
        lutador1+=wazaari
    elif(escolha==3):
        lutador1+=golpe

    escolha=int(input("golpe a ser registrado para lutador 2"))
    if (escolha==1):
        lutador2+=ippon
    elif(escolha==2):
        lutador2+=wazaari
    elif(escolha==3):
        lutador2+=golpe

    
    print("\n pontuação registrada")
    print("\n pontuação registrada")
    
    if(lutador1>=lutador2):
        print("lutador1 venceu ")
    elif(lutador2>=lutador1):
        print("lutador2 venceu")





