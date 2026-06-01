import os
import sys
import time

def limpar_tela():
    """Limpa o terminal para manter o visual limpo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def digitar_efeito(texto, velocidade=0.04):
    """Faz o texto aparecer no terminal letra por letra."""
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def barra_carregamento(texto_status):
    """Gera uma animação de barra de progresso no terminal."""
    digitar_efeito(texto_status, 0.02)
    for i in range(21):
        barra = f"[{'█' * i}{'░' * (20 - i)}]"
        sys.stdout.write(f"\r{barra} {i*5}%")
        sys.stdout.flush()
        time.sleep(0.08)
    print("\n")

# Cores ANSI estilizadas
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AMARELO = "\033[93m"
CIANO = "\033[96m"
RESET = "\033[0m"

limpar_tela()

# --- PRIMEIRA ETAPA ---
digitar_efeito(f"{AMARELO}🤖 SISTEMA INICIALIZADO...{RESET}\n")
digitar_efeito(f"{CIANO}O Lula é seu amigo?{RESET}")
resposta_1 = input("👉 Responda (Sim ou Não): ").strip().upper()

if resposta_1 == "SIM":
    limpar_tela()
    barra_carregamento("🔄 Validando resposta no banco de dados...")
    digitar_efeito(f"{VERDE}✨ Lula é seu amigo, parabéns, está certinho! 🎉{RESET}")
    sys.exit()

# --- SEGUNDA ETAPA ---
limpar_tela()
digitar_efeito(f"{VERMELHO}❌ RESPOSTA INCORRETA.{RESET}\n")
print("-" * 40)
digitar_efeito(f"{VERMELHO}⚠️ ÚLTIMA CHANCE... Você tem certeza absoluta disso?{RESET}")
resposta_2 = input("👉 Responda (Sim ou Não): ").strip().upper()

if resposta_2 in ["NÃO", "NAO"]:
    limpar_tela()
    digitar_efeito(f"{VERDE}Ufa... boa escolha! Ele é seu amigo sim. 😄{RESET}")
else:
    limpar_tela()
    digitar_efeito(f"{VERMELHO}🚨 PROTOCOLO DE EXCLUSÃO ATIVADO!{RESET}")
    time.sleep(1)
    
    # Contagem regressiva dramática com bips do sistema (\a)
    for i in range(3, 0, -1):
        print(f"\r{VERMELHO}Destruindo arquivos em {i}... {RESET}", end="")
        sys.stdout.write('\a') # Emite um som de aviso no terminal do Windows
        sys.stdout.flush()
        time.sleep(1)
        
    print(f"\n\n{VERMELHO}💥 ADEUS!{RESET}")
    time.sleep(0.5)
    
    # 1. Fecha o VS Code (Se estiver no Windows)
    os.system("taskkill /f /im Code.exe")
    
    # 2. Deleta o próprio arquivo do script
    os.remove(__file__)
