soma_impar = 0
soma_par = 0

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.")
for i in range(1, 50, 2):
    nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
    soma_impar += nota

print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.")
for i in range(2, 51, 2):
    nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
    soma_par += nota

media_impar = soma_impar / 25
media_par = soma_par / 25

if media_impar > media_par:
    print("A metade ímpar teve a maior média: ", media_impar)
else:
    print("A metade par teve a maior média: ", media_par)
