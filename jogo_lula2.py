import sys
import random
import tkinter as tk
from tkinter import messagebox

class JogoUltimateCyber:
    def __init__(self, root):
        self.root = root
        self.root.title("S.I.S.T.E.M.A. - Cyber Quiz 2026")
        self.root.geometry("600x450")
        self.root.configure(bg="#050505")
        self.root.resizable(False, False)
        
        # Centralizar janela
        self.root.eval('tk::PlaceWindow . center')

        # Banco de perguntas
        self.perguntas = [
            {"texto": "O voto é secreto de verdade?", "correta": "SIM"},
            {"texto": "O imposto sobre o WinRAR deveria ser obrigatório?", "correta": "NÃO"},
            {"texto": "Misto quente é tecnicamente um sanduíche?", "correta": "SIM"},
            {"texto": "O Lula é seu amigo oficial do peito?", "correta": "SIM"}
        ]
        
        self.pergunta_atual = 0
        self.pontos = 0
        self.tempo_restante = 15.0 # Segundos por fase
        
        # Canvas para animação de fundo (Matrix de Partículas)
        self.canvas = tk.Canvas(root, bg="#050505", highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.particulas = []
        self.criar_particulas()

        # Elementos Visuais flutuando sobre o Canvas
        self.score_label = tk.Label(root, text="", font=("Courier New", 11, "bold"), bg="#050505", fg="#00ffcc")
        self.score_label.place(x=20, y=10)

        self.timer_label = tk.Label(root, text="", font=("Courier New", 12, "bold"), bg="#050505", fg="#ff3333")
        self.timer_label.place(x=450, y=10)

        self.pergunta_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#050505", fg="#ffffff", wraplength=500, justify="center")
        self.pergunta_label.place(x=50, y=150, width=500)

        # Botões estilizados
        self.btn_sim = tk.Button(root, text="S I M", font=("Arial", 11, "bold"), bg="#107c41", fg="white", bd=0, width=12, height=2, activebackground="#169c53", command=lambda: self.verificar_resposta("SIM"))
        self.btn_nao = tk.Button(root, text="N Ã O", font=("Arial", 11, "bold"), bg="#a80000", fg="white", bd=0, width=12, height=2, activebackground="#d80000", command=lambda: self.verificar_resposta("NÃO"))
        
        self.btn_nao.bind("<Enter>", self.fuga_e_tremor)

        # Inicializa os Loops do Motor do Jogo
        self.carregar_pergunta()
        self.update_game_loop()

    def criar_particulas(self):
        """Gera os pontos luminosos iniciais do fundo."""
        for _ in range(30):
            x = random.randint(0, 600)
            y = random.randint(0, 450)
            velocidade = random.uniform(1, 3)
            tamanho = random.randint(1, 3)
            obj = self.canvas.create_oval(x, y, x+tamanho, y+tamanho, fill="#003311")
            self.particulas.append({"id": obj, "x": x, "y": y, "v": velocidade})

    def carregar_pergunta(self):
        """Prepara o estado da nova fase."""
        self.tempo_restante = 15.0
        self.score_label.config(text=f"SCORE: {self.pontos:04d} | FASE: {self.pergunta_atual + 1}/{len(self.perguntas)}")
        
        # Reposiciona os botões no centro
        self.btn_sim.place(x=150, y=320)
        self.btn_nao.place(x=330, y=320)
        
        self.pergunta_label.config(text=self.perguntas[self.pergunta_atual]["texto"], fg="#ffffff")

    def update_game_loop(self):
        """O coração do jogo: roda 30 vezes por segundo controlando animações e tempo."""
        # 1. Animação das partículas de fundo
        for p in self.particulas:
            p["y"] += p["v"]
            if p["y"] > 450:
                p["y"] = 0
                p["x"] = random.randint(0, 600)
            self.canvas.coords(p["id"], p["x"], p["y"], p["x"]+2, p["y"]+2)
            
            # Se for a fase final, deixa o fundo vermelho agressivo
            if self.pergunta_atual == len(self.perguntas) - 1:
                self.canvas.itemconfig(p["id"], fill="#330000")
            else:
                self.canvas.itemconfig(p["id"], fill="#00ff55")

        # 2. Controle do Cronômetro Ativo
        if self.tempo_restante > 0:
            self.tempo_restante -= 0.033 # Deduz o tempo baseado no frame rate (~30fps)
            self.timer_label.config(text=f"TEMPO: {max(0.0, self.tempo_restante):.1f}s")
            
            # Alerta visual de tempo acabando
            if self.tempo_restante < 5:
                self.timer_label.config(fg="#ff0000" if int(self.tempo_restante * 5) % 2 == 0 else "#ffffff")
        else:
            self.game_over("O tempo acabou! O sistema colapsou. 💥")
            return

        # Agenda o próximo frame do loop
        self.root.after(33, self.update_game_loop)

    def verificar_resposta(self, escolha):
        """Valida a escolha do jogador."""
        correta = self.perguntas[self.pergunta_atual]["correta"]
        if escolha == correta:
            self.pontos += int(self.tempo_restante * 10) # Bônus por velocidade!
            self.pergunta_atual += 1
            
            if self.pergunta_atual < len(self.perguntas):
                self.carregar_pergunta()
            else:
                messagebox.showinfo("CYBER VITÓRIA", f"INCRÍVEL!\nVocê hackeou o quiz com {self.pontos} pontos! 🏆")
                self.root.destroy()
                sys.exit()
        else:
            self.game_over("RESPOSTA INCORRETA. Acesso negado. ❌")

    def fuga_e_tremor(self, event):
        """Gera pânico visual se o usuário tentar clicar no 'Não' na fase final."""
        if self.pergunta_atual == len(self.perguntas) - 1:
            # Efeito Glitch no texto temporariamente
            self.pergunta_label.config(text="E L E  É  S E U  A M I G O !!!", fg="#ff0033")
            
            # Move o botão para um lugar totalmente novo
            self.btn_nao.place(x=random.randint(50, 450), y=random.randint(200, 380))
            
            # Faz a janela do Windows tremer fisicamente sabotando o mouse
            geometria_original = self.root.geometry()
            x_atual = self.root.winfo_x()
            y_atual = self.root.winfo_y()
            
            for i in range(10):
                deslocamento = 10 if i % 2 == 0 else -10
                self.root.geometry(f"+{x_atual + deslocamento}+{y_atual + deslocamento}")
                self.root.update()
                self.root.after(15)
                
            # Restaura a posição da janela
            self.root.geometry(f"+{x_atual}+{y_atual}")

    def game_over(self, mensagem):
        messagebox.showerror("SISTEMA CORROMPIDO", mensagem)
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoUltimateCyber(root)
    root.mainloop()
