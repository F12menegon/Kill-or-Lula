import os
import sys
import time
import tkinter as tk
from tkinter import messagebox, ttk

class AplicativoInovador:
    def __init__(self, root):
        self.root = root
        self.root.title("Validador de Sistema v2.0")
        self.root.geometry("450x250")
        self.root.configure(bg="#1e1e1e") # Fundo escuro estilo VS Code
        self.root.resizable(False, False)

        # Centralizar a janela na tela
        self.root.eval('tk::PlaceWindow . center')

        # Título principal
        self.label = tk.Label(
            root, 
            text="🤖 PERGUNTA DE SEGURANÇA 🤖", 
            font=("Arial", 14, "bold"), 
            bg="#1e1e1e", 
            fg="#00ffcc"
        )
        self.label.pack(pady=20)

        # Pergunta
        self.pergunta_label = tk.Label(
            root, 
            text="O Lula é seu amigo?", 
            font=("Arial", 12), 
            bg="#1e1e1e", 
            fg="#ffffff"
        )
        self.pergunta_label.pack(pady=10)

        # Container para os botões
        self.btn_frame = tk.Frame(root, bg="#1e1e1e")
        self.btn_frame.pack(pady=20)

        # Botão SIM
        self.btn_sim = tk.Button(
            self.btn_frame, 
            text="S I M", 
            font=("Arial", 10, "bold"),
            bg="#28a745", 
            fg="white", 
            width=10, 
            command=self.resposta_sim
        )
        self.btn_sim.pack(side=tk.LEFT, padx=20)

        # Botão NÃO
        self.btn_nao = tk.Button(
            self.btn_frame, 
            text="N Ã O", 
            font=("Arial", 10, "bold"),
            bg="#dc3545", 
            fg="white", 
            width=10, 
            command=self.resposta_nao
        )
        self.btn_nao.pack(side=tk.RIGHT, padx=20)

    def resposta_sim(self):
        messagebox.showinfo("Sucesso", "Lula é seu amigo, parabéns, está certinho! 🎉")
        self.root.destroy()
        sys.exit()

    def resposta_nao(self):
        # Transforma a janela para a segunda etapa (Última chance)
        self.label.config(text="⚠️ ALERTA DE CRITICALIDADE ⚠️", fg="#ff3333")
        self.pergunta_label.config(text="ÚLTIMA CHANCE...\nVocê tem certeza absoluta disso?")
        
        # Altera os comandos dos botões para a decisão final
        self.btn_sim.config(command=self.confirmar_destruicao)
        self.btn_nao.config(command=self.salvo_pelo_gongo)

    def salvo_pelo_gongo(self):
        messagebox.showinfo("Ufa!", "Boa escolha! Ele é seu amigo sim. 😄")
        self.root.destroy()
        sys.exit()

    def confirmar_destruicao(self):
        # Remove os botões para o usuário não clicar de novo
        self.btn_frame.pack_forget()
        self.pergunta_label.config(text="Iniciando protocolo de autodestruição...")
        
        # Adiciona uma barra de progresso visual real
        progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=300, mode='determinate')
        progress.pack(pady=10)
        
        # Animação da barra de carregamento
        for i in range(1, 101):
            progress['value'] = i
            self.root.update()
            time.sleep(0.02)
            
        # Contagem regressiva pop-up
        for i in range(3, 0, -1):
            self.root.bell() # Emite o som do sistema
            self.pergunta_label.config(text=f"💥 Destruindo em {i}... 💥", fg="#ff3333", font=("Arial", 14, "bold"))
            self.root.update()
            time.sleep(1)

        # Executa as ações finais antes de fechar tudo
        os.system("taskkill /f /im Code.exe")
        os.remove(__file__)
        self.root.destroy()

# Inicializa a interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicativoInovador(root)
    root.mainloop()
