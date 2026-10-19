
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com os cinco níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

# Função que define a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Nível atual do reservatório
nivel_atual = 5

# Exibe a situação do reservatório
print("=== MONITORAMENTO DO RESERVATÓRIO ===")

mensagem = niveis[nivel_atual - 1]
cor = definir_cor(nivel_atual)

print(cor + mensagem + Style.RESET_ALL)

