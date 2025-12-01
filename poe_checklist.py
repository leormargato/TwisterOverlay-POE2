## Twister Overlay POE 2
## Desenvolvido por: Léo Ramalho - TwisterPOE
## Sinta-se livre para contribuir com este projeto, peço apenas que me credite como autor original.
##Obrigado à todos, bom jogo!

import tkinter as tk
from tkinter import ttk

# --- DADOS DOS ATOS ---
ACTS_DATA = {
    "Ato 1": [
        ("ATO 1 - ACAMPAMENTO CLEARFELL", "header"),
        ("Margem do Rio: Mate o Miller", "item"),
        ("Acampamento Clearfell: Falar com NPCs", "item"),
        ("Clearfell: Mate Beira (+10% Res. Gelo)", "item"),
        ("Clearfell: Baú Abandonado (Habilidade)", "item"),
        ("Toca da Lama: Mate o Devorador", "item"),
        ("Grelwood: Mate Areagne (Habilidade)", "item"),
        ("Opcional: Ponto de Passagem (Grim Tangle)", "item"),
        ("Falar com Una -> Vale Vermelho", "item"),
        ("Vale Vermelho: Mate o Rei da Ferrugem", "item"),
        ("Voltar Clearfell: Ferreiro (Runas)", "item"),
        ("Grelwood: Libertar Sin", "item"),
        ("Voltar Clearfell: Fale com Una", "item"),
        ("Emaranhado Sombrio: Matar Chefe", "item"),
        ("Cemitério dos Eternos: Fale com Lachlann", "item"),
        ("Tumba do Consorte: Tesouro (Habilidade)", "item"),
        ("Tumba do Consorte: Mate Asinia", "item"),
        ("Mausoléu: Mate Draven", "item"),
        ("Cemitério dos Eternos: Mate Lachlann", "item"),
        ("Campos de Caça: Pegue o Ponto de Passagem", "item"),
        ("Voltar Clearfell (Entregar Missões)", "item"),
        ("ATO 1 - CAMPOS DE CAÇA", "header"),
        ("Freythorn: Rei das Brumas (+30 Espírito)", "item"),
        ("Campos de Caça: Mate Crowbell (+2 Pontos)", "item"),
        ("Campos de Caça: Ritual Driádico (Habilidade)", "item"),
        ("Fazendas Ogham: Alaúde da Una (+2 Pontos)", "item"),
        ("IMPORTANTE: Liberar Bancada de Reciclagem", "header"),
        ("Vila Ogham: Oficina do Renly (Bancada)", "item"),
        ("Vila Ogham: Mate o Executor", "item"),
        ("Muralhas da Mansão: Ponto de Passagem", "item"),
        ("Voltar Clearfell (Entregar Missões)", "item"),
        ("Mansão Ogham: Candlemass (+Vida)", "item"),
        ("Mansão Ogham: Mate Geonor", "item"),
        ("Clearfell: Fale com Sin -> Ato 2", "item"),
    ],
    "Ato 2": [
        ("ATO 2 - CARAVANA ARDURA", "header"),
        ("Arredores de Vastiri: Falar com Zarka", "item"),
        ("Arredores de Vastiri: Mate o Rathbreaker", "item"),
        ("Caravana Ardura: Falar com NPCs", "item"),
        ("Pedreira Mawdun: Mate Rudja", "item"),
        ("Portões Halani: Fale com NPC e volte", "item"),
        ("Passagem do Traidor: Mate Balbala", "item"),
        ("Portões Halani: Mate Jamanra", "item"),
        ("Provação dos Sekhemas: 1ª Ascendência", "item"),
        ("Terras Baldias: Passagem Sem Luz (Abyss)", "item"),
        ("Terras Baldias: Segredo da Efígie (Gema Sup)", "item"),
        ("Poços de Ossos: Relíquia do Clã do Sol", "item"),
        ("Poços de Ossos: Mate Iktab e Ekbab", "item"),
        ("Volte para a Caravana Ardura", "item"),
        ("KETH & TITÃS", "header"),
        ("Keth: Mate Kabala (+2 Pontos)", "item"),
        ("Cidade Perdida: Relíquia do Clã Kabala", "item"),
        ("Santuários Enterrados: Azarian (Essência Água)", "item"),
        ("Vale dos Titãs: Altar da Relíquia (Charm effect)", "item"),
        ("Gruta do Titã: Mate Zalmarath", "item"),
        ("Ardura: Soar Trombeta -> Deshar", "item"),
        ("DESHAR & FINAL", "header"),
        ("Deshar: Dekhara Caído (+2 Pontos)", "item"),
        ("Caminho do Luto: Urna Silenciosa (Gema Sup)", "item"),
        ("Torres de Deshar: Irmãs Garukhan (+10% Res. Raio)", "item"),
        ("Torres de Deshar: Mate Tor Gul", "item"),
        ("Encouraçado: Mate Jamanra", "item"),
        ("Ardura: Fale com Sin & Asala -> Ato 3", "item"),
    ],
    "Ato 3": [
        ("ATO 3 - ACAMPAMENTO ZIGURATE", "header"),
        ("Pântano das Areias: Mate Rootdredge (Gema Hab.)", "item"),
        ("Fogueira Orok: Orbe de Joalheiro Menor", "item"),
        ("Acampamento Zigurate -> Falar com NPCs", "item"),
        ("Ruínas da Selva: Mate Punho de Prata (+2 pts)", "item"),
        ("Criptas de Veneno: Pegue os Venenos", "item"),
        ("Terras Infestadas: Achar Ponto de Passagem", "item"),
        ("Pântano Azak: Mate Ignagduk (+30 Espírito)", "item"),
        ("Pântanos Quiméricos: Mate Xyclucian", "item"),
        ("Templo do Caos: 2ª Ascendência", "item"),
        ("JIQUANI & CIDADE", "header"),
        ("Maquinário de Jiquani: Mandíbula Negra (Res. Fogo)", "item"),
        ("Santuário de Jiquani: Mate Zicoatl", "item"),
        ("Canais de Matlan: Drene a água", "item"),
        ("Cidade Afogada -> Cofre Derretido", "item"),
        ("Cofre Derretido: Mate Mektul (Bancada Reforja)", "item"),
        ("NÃO PEGUE OS COGUMELOS", "header"),
        ("Ápice da Imundície: Mate Rainha da Imundície", "item"),
        ("Templo de Kopec: Mate Ketzuli", "item"),
        ("FINAL ATO 3", "header"),
        ("Utzaal: Mate Viper Napuatzi & Pegue Coração", "item"),
        ("Aggorat -> Altar do Coração", "item"),
        ("Câmaras Negras: Mate Doryani", "item"),
        ("Zigurate: Fale com Alva -> Ato 4", "item"),
    ],
    "Ato 4": [
        ("ATO 4 - KINGSMARCH", "header"),
        ("Kingsmarch: Falar com NPCs", "item"),
        ("Ilha de Kin: Besta Cega (+2 Pontos)", "item"),
        ("Ilha de Kin: Fragmento de Mapa", "item"),
        ("Ilha de Kin: Cercado das Bestas (Gema Sup)", "item"),
        ("Ilha de Kin: Fóssil (Joalheiro Menor)", "item"),
        ("Tocas Vulcânicas: Mate Krutog", "item"),
        ("Baía de Kedge: Fragmento de Mapa", "item"),
        ("Baía de Kedge: Navio Abandonado (Joalheiro)", "item"),
        ("Fim da Jornada: Mate Capitão Hartlin", "item"),
        ("Prisão Abandonada: Chave/Capela (+Vida)", "item"),
        ("Confinamento Solitário: Mate o Prisioneiro", "item"),
        ("Olho de Hinekora -> Salões dos Mortos", "item"),
        ("Salões dos Mortos: +5% Mana/Status/Passiva", "item"),
        ("Whakapanu: Grande Branco (Barbatana)", "item"),
        ("Whakapanu: Fragmento de Mapa", "item"),
        ("Cavernas Cantantes: Mate Diamora", "item"),
        ("Cavernas Cantantes: Amuleto Perolado", "item"),
        ("Ilha Shrike: Fragmento de Mapa", "item"),
        ("FINAL APÓS JUNTAR OS MAPAS", "header"),
        ("Arastas: Mate Torvian", "item"),
        ("A Escavação: Mate Benedictus", "item"),
        ("Ngakanu -> Coração da Tribo", "item"),
        ("Coração da Tribo: Mate Tavakai", "item"),
    ],
    "Interlúdio": [
        ("INTERLÚDIO", "header"),
        ("MALDIÇÃO DE HOLTEN", "header"),
        ("Fazendas Queimadas: Mate Isolde e Heldra", "item"),
        ("Pedras de Serle: Mate Siora", "item"),
        ("Holten: Barqueiro (Vende Runas por Ouro!)", "item"),
        ("Wolvenhold: Mate Oswin (+2 Pontos)", "item"),
        ("Propriedade Holten: Thane Wulfric e Lady Elyswyth", "item"),
        ("A BARYA ROUBADA", "header"),
        ("Cruzamento Khari: Skullmaw (+5% Vida)", "item"),
        ("Cruzamento Khari: Mate Atkhi e Anundr", "item"),
        ("Santuário Sel Khari: Mate Elzarah", "item"),
        ("Portões Galai: Mate Vornas", "item"),
        ("Qimah: Pilar de Orbala (Buff)", "item"),
        ("Reservatório Qimah: Mate Azmadi", "item"),
        ("CONTINGÊNCIA DE DORYANI", "header"),
        ("Floresta das Cinzas: Monumento (Habilidade)", "item"),
        ("Vila Kriar: Mate Lythara (+40 Espírito)", "item"),
        ("Lago Glacial: Mate Rakkar", "item"),
        ("Cavernas Uivantes: Mate Yeti (+2 Pontos)", "item"),
        ("Picos Kriar: Ancião (Item Único)", "item"),
        ("Ravina Gravada: Mate Stormgore", "item"),
        ("Cofre Cuachic: Mate Zelina e Zolin", "item"),
        ("Kingsmarch: Entregue missões (+2 pts)", "item"),
        ("CHEGOU NO ENDGAME! BOA SORTE!", "header"),
    ]
}

class PoEOverlay:
    def __init__(self, root):
        self.root = root
        self.root.title("Fluxograma POE 2 by: TwisterPOE")
        
        # Variáveis de Estado
        self.is_collapsed = False
        self.expanded_height = 500  # Altura padrão
        
        # Configurações da Janela
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.85)
        self.root.overrideredirect(True)
        self.root.configure(bg='#0f0f0f')
        self.root.geometry(f"300x{self.expanded_height}+20+100")
        
        # Estilos
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCheckbutton", background='#0f0f0f', foreground='#cccccc', font=('Segoe UI', 9))
        
        # --- BARRA DE TÍTULO (Arrastar e Controles) ---
        self.title_bar = tk.Frame(root, bg='#1a1a1a', height=30)
        self.title_bar.pack(fill=tk.X, side=tk.TOP)
        
        # Título
        self.lbl_title = tk.Label(self.title_bar, text=":: Fluxograma POE2 ::", bg='#1a1a1a', fg='orange', font=('Arial', 9, 'bold'))
        self.lbl_title.pack(side=tk.LEFT, padx=5)
        
        # Botão Fechar (X)
        btn_close = tk.Button(self.title_bar, text="X", command=root.quit, bg='#880000', fg='white', bd=0, width=3)
        btn_close.pack(side=tk.RIGHT)

        # Botão Minimizar/Recolher (_)
        self.btn_min = tk.Button(self.title_bar, text="_", command=self.toggle_collapse, bg='#333333', fg='white', bd=0, width=3)
        self.btn_min.pack(side=tk.RIGHT, padx=1)

        # Eventos de Arrastar
        self.title_bar.bind('<Button-1>', self.start_move)
        self.title_bar.bind('<B1-Motion>', self.do_move)
        self.lbl_title.bind('<Button-1>', self.start_move)
        self.lbl_title.bind('<B1-Motion>', self.do_move)

        # --- ÁREA DE CONTEÚDO (Scroll) ---
        self.canvas = tk.Canvas(root, bg='#0f0f0f', highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg='#0f0f0f')

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Empacota conteúdo inicial
        self.canvas.pack(side="top", fill="both", expand=True, padx=5)
        self.scrollbar.pack(side="right", fill="y")
        
        # Habilitar scroll com roda do mouse
        self.root.bind_all("<MouseWheel>", self._on_mousewheel)

        # --- BARRA DE NAVEGAÇÃO (Abas) ---
        self.nav_frame = tk.Frame(root, bg='#1a1a1a', height=30)
        self.nav_frame.pack(side="bottom", fill=tk.X)

        acts = list(ACTS_DATA.keys())
        for act_name in acts:
            btn = tk.Button(self.nav_frame, text=act_name.replace("Ato ", "A").replace("Interlúdio", "Int"), 
                            command=lambda a=act_name: self.load_act(a),
                            bg='#333', fg='white', bd=1, relief="flat", font=('Segoe UI', 8))
            btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=1, pady=1)

        # --- LÓGICA DE ESTADO ---
        self.task_states = {}
        for act in ACTS_DATA:
            self.task_states[act] = []
            for item in ACTS_DATA[act]:
                 self.task_states[act].append(tk.BooleanVar())

        # Carregar o primeiro ato
        self.load_act("Ato 1")

    def toggle_collapse(self):
        """Alterna entre mostrar apenas o título ou a janela toda."""
        if self.is_collapsed:
            # RESTAURAR
            # Recupera a altura e posição atuais
            x = self.root.winfo_x()
            y = self.root.winfo_y()
            self.root.geometry(f"300x{self.expanded_height}+{x}+{y}")
            
            # Re-exibir widgets
            self.canvas.pack(side="top", fill="both", expand=True, padx=5)
            self.scrollbar.pack(side="right", fill="y")
            self.nav_frame.pack(side="bottom", fill=tk.X)
            
            # Mudar ícone do botão
            self.btn_min.config(text="_", bg='#333333')
            self.is_collapsed = False
        else:
            # RECOLHER (MINIMIZAR)
            x = self.root.winfo_x()
            y = self.root.winfo_y()
            
            # Esconder widgets
            self.canvas.pack_forget()
            self.scrollbar.pack_forget()
            self.nav_frame.pack_forget()
            
            # Reduzir altura para apenas a barra (aprox 30px)
            self.root.geometry(f"300x30+{x}+{y}")
            
            # Mudar ícone do botão
            self.btn_min.config(text="+", bg='#555555')
            self.is_collapsed = True

    def load_act(self, act_name):
        # Limpar tela atual
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        # Atualizar título
        self.lbl_title.config(text=f":: {act_name} - TwisterOverlay ::")

        # Recriar lista
        tasks = ACTS_DATA[act_name]
        states = self.task_states[act_name]

        for i, (text, type_) in enumerate(tasks):
            if type_ == "header":
                lbl = tk.Label(self.scrollable_frame, text=text, bg='#0f0f0f', fg='#e8c366', 
                               font=('Segoe UI', 9, 'bold'), anchor='w', wraplength=260)
                lbl.pack(fill=tk.X, pady=(10, 2))
            else:
                chk = ttk.Checkbutton(self.scrollable_frame, text=text, variable=states[i], 
                                      onvalue=True, offvalue=False)
                chk.pack(anchor='w', padx=5, pady=1)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")

    def _on_mousewheel(self, event):
        if not self.is_collapsed:
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

if __name__ == "__main__":
    root = tk.Tk()
    app = PoEOverlay(root)
    root.mainloop()



