import sys
import random
import tkinter as tk
from tkinter import messagebox

class JogoSemDownloads:
    def __init__(self, root):
        self.root = root
        self.root.title("⚡ CYBER QUIZ PROTOCOL 3000 ⚡")
        self.root.geometry("600x450")
        self.root.configure(bg="#050508")
        self.root.resizable(False, False)
        
        # Centralizar a janela na tela
        self.root.eval('tk::PlaceWindow . center')

        # Banco de perguntas
        self.perguntas = [
            {"texto": "O voto é secreto de verdade no Brasil?", "correta": "SIM"},
            {"texto": "O imposto sobre o WinRAR deveria ser obrigatório?", "correta": "NÃO"},
            {"texto": "Misto quente é tecnicamente um sanduíche?", "correta": "SIM"},
            {"texto": "O Lula é seu amigo oficial do peito?", "correta": "SIM"}
        ]
        
        self.fase_atual = 0
        self.pontos = 0
        self.tempo_restante = 15.0

        # Canvas para desenhar as partículas de fundo (Efeito Matrix/Espaço)
        self.canvas = tk.Canvas(root, bg="#050508", highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.particulas = []
        self.criar_particulas()

        # Interface - Elementos Visuais (HUD)
        self.score_label = tk.Label(root, text="", font=("Courier New", 11, "bold"), bg="#050508", fg="#00ffcc")
        self.score_label.place(x=30, y=25)

        self.timer_label = tk.Label(root, text="", font=("Courier New", 12, "bold"), bg="#050508", fg="#00ffc8")
        self.timer_label.place(x=450, y=25)

        self.titulo_label = tk.Label(root, text="", font=("Courier New", 16, "bold"), bg="#050508")
        self.titulo_label.place(x=50, y=100, width=500)

        self.pergunta_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#050508", fg="#ffffff", wraplength=500, justify="center")
        self.pergunta_label.place(x=50, y=200, width=500)

        # Barra de tempo visual
        self.canvas_barra = tk.Canvas(root, bg="#141423", highlightthickness=0, height=6)
        self.canvas_barra.place(x=100, y=280, width=400)
        # CORREÇÃO DA LINHA: Mudado de create_rect para create_rectangle
        self.barra_tempo = self.canvas_barra.create_rectangle(0, 0, 400, 6, fill="#00ffc8", width=0)

        # Botões Esportivos Customizados
        self.btn_sim = tk.Button(root, text="S I M", font=("Arial", 11, "bold"), bg="#107c41", fg="white", bd=1, relief="flat", width=12, height=2, command=lambda: self.processar_resposta("SIM"))
        self.btn_nao = tk.Button(root, text="N Ã O", font=("Arial", 11, "bold"), bg="#a80000", fg="white", bd=1, relief="flat", width=12, height=2, command=lambda: self.processar_resposta("NÃO"))
        
        # Vincula o movimento do mouse para fazer o botão fugir
        self.btn_nao.bind("<Enter>", self.aplicar_fuga_e_glitch)

        # Inicia o jogo
        self.carregar_fase()
        self.atualizar_motor()

    def criar_particulas(self):
        """Gera as partículas que vão flutuar no fundo."""
        for _ in range(40):
            x = random.randint(0, 600)
            y = random.randint(0, 450)
            v = random.uniform(0.5, 2.0)
            tamanho = random.randint(1, 3)
            id_particula = self.canvas.create_oval(x, y, x+tamanho, y+tamanho, fill="#005544", width=0)
            self.particulas.append({"id": id_particula, "x": x, "y": y, "v": v})

    def carregar_fase(self):
        """Configura os textos e cores de cada fase."""
        self.tempo_restante = 15.0
        self.score_label.config(text=f"DECK: SECURITY_QUIZ // STAGE: 0{self.fase_atual+1}_OF_04")
        
        # Posiciona os botões no lugar padrão inicial
        self.btn_sim.place(x=150, y=340)
        self.btn_nao.place(x=330, y=340)
        
        self.pergunta_label.config(text=self.perguntas[self.fase_atual]["texto"], fg="#ffffff")

        # Fase Final muda o tema para Alerta de Intrusão Vermelho
        if self.fase_atual == 3:
            self.titulo_label.config(text="☣️ ALERTA DE INTRUSÃO DETECTADO ☣️", fg="#ff3350")
            self.canvas_barra.itemconfig(self.barra_tempo, fill="#ff3350")
            for p in self.particulas:
                self.canvas.itemconfig(p["id"], fill="#550011")
        else:
            self.titulo_label.config(text="🔐 PROTOCOLO DE VALIDAÇÃO DE USUÁRIO", fg="#00ffc8")

    def atualizar_motor(self):
        """Gerencia o tempo e a animação do fundo a cada frame."""
        # 1. Move as partículas no fundo
        for p in self.particulas:
            p["y"] -= p["v"]
            if p["y"] < 0:
                p["y"] = 450
                p["x"] = random.randint(0, 600)
            self.canvas.coords(p["id"], p["x"], p["y"], p["x"]+2, p["y"]+2)

        # 2. Controla o Cronômetro
        if self.tempo_restante > 0:
            self.tempo_restante -= 0.05
            self.timer_label.config(text=f"TEMPO: {max(0.0, self.tempo_restante):.1f}s")
            
            # Atualiza a barra gráfica de tempo decrescente
            largura = int((self.tempo_restante / 15.0) * 400)
            self.canvas_barra.coords(self.barra_tempo, 0, 0, largura, 6)
        else:
            self.game_over("O TEMPO EXPIROU. SISTEMA BLOQUEADO.")
            return

        # Roda novamente em 50 milissegundos
        self.root.after(50, self.atualizar_motor)

    def processar_resposta(self, escolha):
        if escolha == self.perguntas[self.fase_atual]["correta"]:
            self.pontos += int(self.tempo_restante * 15)
            self.fase_atual += 1
            if self.fase_atual >= len(self.perguntas):
                messagebox.showinfo("VITÓRIA CIBERNÉTICA", f"Acesso liberado!\nPontuação final: {self.pontos} XP")
                self.root.destroy()
                sys.exit()
            self.carregar_fase()
        else:
            self.game_over("SISTEMA BLOQUEADO. GAME OVER.")

    def aplicar_fuga_e_glitch(self, event):
        """SABOTAGEM: Faz o botão saltar e treme a tela se tentar clicar no NÃO no final."""
        if self.fase_atual == 3:
            # Teleporta o botão NÃO pela janela
            self.btn_nao.place(x=random.randint(50, 480), y=random.randint(150, 380))
            
            # Altera o texto simulando um erro/invasão técnica
            self.pergunta_label.config(text="E L E  É  S E U  A M I G O !!!", fg="#ff3350")
            
            # Efeito físico: Treme a janela do Windows na sua área de trabalho
            x_original = self.root.winfo_x()
            y_original = self.root.winfo_y()
            for i in range(8):
                for deslocamento in [8, -8]:
                    self.root.geometry(f"+{x_original + deslocamento}+{y_original + deslocamento}")
                    self.root.update()
                    self.root.after(10)
            self.root.geometry(f"+{x_original}+{y_original}")

    def game_over(self, mensagem):
        messagebox.showerror("CRITICAL_ERROR", mensagem)
        self.root.destroy()
        sys.exit()

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoSemDownloads(root)
    root.mainloop()
