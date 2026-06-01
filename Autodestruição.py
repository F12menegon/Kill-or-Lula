import os
import sys
import time

def digitar_efeito(texto, velocidade=0.04):
    """Faz o texto aparecer no terminal letra por letra."""
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

# Cores ANSI para deixar o terminal estilizado
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
RESET = "\033[0m"

# --- PRIMEIRA ETAPA ---
digitar_efeito(f"{AMARELO}O Lula é seu amigo?{RESET}")
resposta_1 = input("Sim ou Não? ").strip().upper()

if resposta_1 == "SIM":
    digitar_efeito(f"{VERDE}Lula é seu amigo, parabéns, está certinho! 🎉{RESET}")
    sys.exit()  # Encerra o programa com sucesso aqui

# --- SEGUNDA ETAPA (SÓ DEPOIS DE ERRAR A PRIMEIRA) ---
print("-" * 40)
digitar_efeito(f"{VERMELHO}⚠️ ÚLTIMA CHANCE... Você tem certeza disso?{RESET}")
resposta_2 = input("Sim ou Não? ").strip().upper()

if resposta_2 == "NÃO" or resposta_2 == "NAO":
    digitar_efeito(f"{VERDE}Ufa... boa escolha! Ele é seu amigo sim. 😄{RESET}")
else:
    digitar_efeito(f"{VERMELHO}Resposta errada. Iniciando autodestruição...{RESET}")
    time.sleep(1)
    
    # 1. Fecha o VS Code (Se estiver no Windows)
    os.system("taskkill /f /im Code.exe")
    
    # 2. Deleta o próprio arquivo do script
    os.remove(__file__)
