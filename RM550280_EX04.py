minutos = int(input("Digite os minutos atuais: "))

fatorial = 1
for i in range(1, minutos+1):
    fatorial *= i

senha = "LIBERDADE" + str(fatorial)
print("Senha para desbloqueio:", senha)
