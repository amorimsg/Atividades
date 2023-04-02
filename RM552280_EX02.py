votos_segunda = int(input("Digite a quantidade de votos da segunda-feira: "))
votos_terca = int(input("Digite a quantidade de votos da terça-feira: "))
votos_quarta = int(input("Digite a quantidade de votos da quarta-feira: "))
votos_quinta = int(input("Digite a quantidade de votos da quinta-feira: "))
votos_sexta = int(input("Digite a quantidade de votos da sexta-feira: "))

votos = [votos_segunda, votos_terca, votos_quarta, votos_quinta, votos_sexta]

mais_votado = max(votos)

quantidade_empates = votos.count(mais_votado)

if quantidade_empates > 1:
    print("Houve um empate entre", quantidade_empates, "dias da semana.")

else:
    indice_vencedor = votos.index(mais_votado)
    dias_semana = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
    dia_escolhido = dias_semana[indice_vencedor]
    print("O dia escolhido para as lives é", dia_escolhido, "com", mais_votado, "votos.")
