tipo_assinatura = input("Qual é o tipo de assinatura do cliente? (Basic, Silver, Gold ou Platinum): ").lower()

while tipo_assinatura not in ["basic", "silver", "gold", "platinum"]:
    print("Tipo de assinatura inválida")
    tipo_assinatura = input("Qual é o tipo de assinatura do cliente? (Basic, Silver, Gold ou Platinum): ").lower()

faturamento_anual = float(input("Qual é o faturamento anual do cliente? : "))

if tipo_assinatura == "basic":
    taxa_bonus = 0.3
elif tipo_assinatura == "silver":
    taxa_bonus = 0.2
elif tipo_assinatura == "gold":
    taxa_bonus = 0.1
elif tipo_assinatura == "platinum":
    taxa_bonus = 0.05

valor_bonus = faturamento_anual * taxa_bonus

print("O valor do bônus a ser pago é de R$ {:.2f}".format(valor_bonus))
