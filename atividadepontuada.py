import os
os.system('cls')


codigos = [1, 2, 3, 4, 5, 6, 7]
nomes = [
    "Hemograma Completo",
    "Raio-X",
    "Ultrassonografia",
    "Eletrocardiograma",
    "Tomografia",
    "Ressonância Magnética",
    "Exame de Glicose"
]
precos = [50.00, 100.00, 150.00, 80.00, 300.00, 600.00, 30.00] 

exames_escolhidos_codigos = []
exames_escolhidos_nomes = []
subtotal = 0.0

print("Bem-vindo ao Sistema de Agendamento do Hospital Vida Plena!")


while True:
    print("\n--- Tabela de Exames ---")
    for i in range(7):
        print(f"Código {codigos[i]} | {nomes[i]} - R$ {precos[i]:.2f}")
    
    print("\nDigite o código do exame para agendar ou '0' para encerrar.")
    
    escolha = int(input("Código desejado: "))
    
    if escolha == 0:
        break
    
    if escolha in codigos:
        indice = codigos.index(escolha)
        
        exames_escolhidos_codigos.append(codigos[indice])
        exames_escolhidos_nomes.append(nomes[indice])
        subtotal = subtotal + precos[indice]
        
        print(f"--> {nomes[indice]} adicionado com sucesso!")
    else:
        print("--> CÓDIGO INVÁLIDO! Por favor, digite um código da lista.")
        continue 
    continuar = input("\nDeseja agendar outro exame? (S/N): ").upper()
    if continuar == "N":
        break

if subtotal > 0:
    print("\n--- Formas de Pagamento ---")
    print("1 - Convênio (Desconto de 15%)")
    print("2 - Particular (Sem desconto)")
    print("3 - Cartão de Crédito (Acréscimo de 8%)")
    
    forma_pagamento = int(input("Escolha a forma de pagamento (1/2/3): "))
    
    valor_modificado = 0.0 
    tipo_pagamento_nome = ""
    valor_final = 0.0
    
    if forma_pagamento == 1:
        tipo_pagamento_nome = "Convênio"
        valor_modificado = subtotal * 0.15 
        valor_final = subtotal - valor_modificado
    
    elif forma_pagamento == 2:
        tipo_pagamento_nome = "Particular"
        valor_modificado = 0.0
        valor_final = subtotal
        
    elif forma_pagamento == 3:
        tipo_pagamento_nome = "Cartão de Crédito"
        valor_modificado = subtotal * 0.08 
        valor_final = subtotal + valor_modificado
        
    else:
        print("Opção de pagamento inválida! Calculando como Particular por padrão.")
        tipo_pagamento_nome = "Particular"
        valor_final = subtotal

    
    print("\n================ RESUMO DO AGENDAMENTO ================")
    print("Exames escolhidos:")
    for i in range(len(exames_escolhidos_codigos)):
        print(f"- Código {exames_escolhidos_codigos[i]}: {exames_escolhidos_nomes[i]}")
        
    print("-------------------------------------------------------")
    print(f"Subtotal dos exames:      R$ {subtotal:.2f}")
    print(f"Forma de Pagamento:       {tipo_pagamento_nome}")
    
    if forma_pagamento == 1:
        print(f"Desconto aplicado (15%): -R$ {valor_modificado:.2f}")
    elif forma_pagamento == 3:
        print(f"Acréscimo aplicado (8%): +R$ {valor_modificado:.2f}")
    else:
        print("Desconto / Acréscimo:      R$ 0.00")
        
    print(f"VALOR FINAL A PAGAR:      R$ {valor_final:.2f}")
    print("=======================================================\n")
    print("O Hospital Vida Plena agradece a sua preferência!")

else:
    print("\nNenhum exame foi agendado. O sistema foi encerrado.")