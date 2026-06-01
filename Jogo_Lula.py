import sys
import random
import tkinter as tk
from tkinter import messagebox, ttk

class JogoDasPerguntas:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Gamer Ultimate v1.0")
        self.root.geometry("500x350")
        self.root.configure(bg="#121212")
        self.root.resizable(False, False)

        # Centralizar janela
        self.root.eval('tk::PlaceWindow . center')

        # Banco de perguntas do jogo
        self.perguntas = [
            {"texto": "O voto é secreto de verdade?", "correta": "SIM"},
            {"texto": "O imposto sobre o WinRAR deveria ser obrigatório?", "correta": "NÃO"},
            {"texto": "Misto quente é tecnicamente um sanduíche?", "correta": "SIM"},
            {"texto": "O Lula é seu amigo oficial do peito?", "correta": "SIM"} # Pergunta final troll
        ]
        
        self.pergunta_atual = 0
        self.pontos = 0

        # Interface Visual - Cabeçalho de Pontos
        self.score_label = tk.Label(
            root, text="Pontos: 0 | Fase: 1/4", font=("Courier New", 11, "bold"), bg="#121212", fg="#00ffcc"
        )
        self.score_label.pack(pady=10)

        # Título da Fase
        self.titulo_label = tk.Label(
            root, text="PERGUNTA DE SEGURANÇA", font=("Arial", 14, "bold"), bg="#121212", fg="#ffffff"
        )
        self.titulo_label.pack(pady=10)

        # Texto da Pergunta
        self.pergunta_label = tk.Label(
            root, text="", font=("Arial", 12, "italic"), bg="#121212", fg="#ffffff", wraplength=400, justify="center"
        )
        self.pergunta_label.pack(pady=20)

        # Botão SIM
        self.btn_sim = tk.Button(
            root, text="S I M", font=("Arial", 10, "bold"), bg="#28a745", fg="white", width=10, command=lambda: self.verificar_resposta("SIM")
        )
        
        # Botão NÃO
        self.btn_nao = tk.Button(
            root, text="N Ã O", font=("Arial", 10, "bold"), bg="#dc3545", fg="white", width=10, command=lambda: self.verificar_resposta("NÃO")
        )

        # Vincula o evento do mouse passar por cima do botão NÃO
        self.btn_nao.bind("<Enter>", self.fuga_do_botao)

        # Inicializa a primeira pergunta
        self.carregar_pergunta()

    def carregar_pergunta(self):
        """Atualiza a tela com os dados da nova pergunta."""
        self.score_label.config(text=f"Pontos: {self.pontos} | Fase: {self.pergunta_atual + 1}/{len(self.perguntas)}")
        
        # Reseta os botões para a posição padrão centralizada antes de exibir a pergunta
        self.btn_sim.place(x=130, y=220)
        self.btn_nao.place(x=270, y=220)

        pergunta_texto = self.perguntas[self.pergunta_atual]["texto"]
        self.pergunta_label.config(text=pergunta_texto)

        # Se for a pergunta final (do Lula), ativa o modo troll visual
        if self.pergunta_atual == len(self.perguntas) - 1:
            self.titulo_label.config(text="⚠️ FASE CRÍTICA FINAL ⚠️", fg="#ff3333")
            self.root.configure(bg="#1a0d0d")
            self.pergunta_label.config(bg="#1a0d0d")
            self.titulo_label.config(bg="#1a0d0d")
            self.score_label.config(bg="#1a0d0d")

    def verificar_resposta(self, escolha_usuario):
        """Valida a resposta do jogador e decide o rumo do jogo."""
        resposta_correta = self.perguntas[self.pergunta_atual]["correta"]

        if escolha_usuario == resposta_correta:
            self.pontos += 100
            messagebox.showinfo("Acertou!", "Boa! Resposta perfeitamente correta. 🎉")
            
            self.pergunta_atual += 1
            if self.pergunta_atual < len(self.perguntas):
                self.carregar_pergunta()
            else:
                # Fim de jogo com vitória total
                messagebox.showinfo("VITÓRIA!", f"Parabéns! Você fechou o jogo!\nPontuação Final: {self.pontos} pontos! 🏆")
                self.root.destroy()
                sys.exit()
        else:
            # Errou a resposta (Nas primeiras fases)
            messagebox.showerror("GAME OVER", "Resposta errada! O sistema fechou seu jogo. ❌")
            self.root.destroy()
            sys.exit()

    def fuga_do_botao(self, event):
        """Faz o botão NÃO fugir de forma randômica se for a pergunta final do Lula."""
        if self.pergunta_atual == len(self.perguntas) - 1:
            # Gera novas coordenadas dentro da janela para o botão mudar de lugar instantaneamente
            novo_x = random.randint(50, 380)
            novo_y = random.randint(150, 280)
            self.btn_nao.place(x=novo_x, y=novo_y)

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoDasPerguntas(root)
    root.mainloop()
