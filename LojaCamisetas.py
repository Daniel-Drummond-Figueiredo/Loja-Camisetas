print("Bem vindo a Fábrica de Camisetas de Daniel Drummond Figueiredo")
#Função para escolha da camiseta
def modelo_camiseta ():
    while True:
        modelo_camiseta = input('Escolha o modelo de camiseta (MCS/MLS/MCE/MLE): ').upper()
        if modelo_camiseta == 'MCS':
            return 1.80
        elif modelo_camiseta == 'MLS':
            return 2.10
        elif modelo_camiseta == 'MCE':
            return 2.90
        elif modelo_camiseta == 'MLE':
            return 3.20
        else: print('Não temos esta opção no momento. Escolha entre (MCS/MLS/MCE/MLE)')
#Função para quantidade de camisetas
def quantidade_camisetas():
    while True:
        try:
            quant_camisetas = int(input('Insira a quantidade de camisetas desejadas: '))
            if quant_camisetas <20:
                return quant_camisetas
            elif quant_camisetas <200:
                return quant_camisetas * 0.95
            elif quant_camisetas <2000:
                return quant_camisetas * 0.93
            elif quant_camisetas <20000:
                return quant_camisetas * 0.88
            else: print('Não aceitamos pedidos acima de 20000 camisetas.')
        except ValueError:
            print('Insira um número válido para quantidade de camisetas.')
#Função para o frete
def frete():
    while True:
        try:
            frete = int(input('Para o frete: Escolha entre 1 (Transportadora - R$100,00) - 2 (Sedex - R$200,00) ou 0 (Retirar na fábrica - Grátis): '))
            if frete == 1:
                return 100
            elif frete == 2:
                return 200
            elif frete == 0:
                return 0
            else: print('Opção de frete inválida. Escolha entre 1 (Transportadora), 2 (Sedex) ou 0 (Retirar na fábrica).')
        except ValueError:
            print('Insira uma opção válida para o frete')
preco = modelo_camiseta()
camisetas_desconto = quantidade_camisetas()
valor_frete = frete()
total = (preco * camisetas_desconto) + valor_frete
print(f"Modelo escolhido: R${preco:.2f}")
print(f"Valor camisetas com desconto: R${camisetas_desconto:.2f}")
print(f"Valor do frete: R${valor_frete:.2f}")
print(f"Total a pagar: R${total:.2f}")
