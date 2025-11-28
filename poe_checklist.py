import tkinter as tk
from tkinter import ttk

# --- DADOS DOS ATOS ---
ACTS_DATA = {
    "Ato 1": [
        ("ATO 1 - CLEARFELL ENCAMPMENT", "header"),
        ("Riverbank: Mate Miller", "item"),
        ("Clearfell encampment: Falar com NPCs", "item"),
        ("Clearfell: Mate Beira (+10% Cold Res)", "item"),
        ("Clearfell: Abandoned Stash (Skill)", "item"),
        ("Mud Burrow: Mate Devourer", "item"),
        ("Grelwood: Mate Areagne (Skill)", "item"),
        ("Opcional: Waypoint Grim Tangle", "item"),
        ("Falar com Una -> Red Vale", "item"),
        ("Red Vale: Mate Rust King", "item"),
        ("Voltar Clearfell: Ferreiro (Runas)", "item"),
        ("Grelwood: Libertar Sin", "item"),
        ("Voltar Clearfell: Fale com Una", "item"),
        ("Grim Tangle: Matar Boss", "item"),
        ("Cemetery of Eternals: Fale com Lachlann", "item"),
        ("Tomb of Consort: Haunted Treasure (Skill)", "item"),
        ("Tomb of Consort: Mate Asinia", "item"),
        ("Mausoleum: Mate Draven", "item"),
        ("Cemetery of Eternals: Mate Lachlann", "item"),
        ("Hunting Grounds: Pegue o Waypoint", "item"),
        ("Voltar Clearfell (Entregar Quests)", "item"),
        ("ATO 1 - HUNTING GROUNDS", "header"),
        ("Freythorn: King of Mists (+30 Spirit)", "item"),
        ("Hunting Grounds: Mate Crowbell (+2 pontos)", "item"),
        ("Hunting Grounds: Dryadic Ritual (Skill)", "item"),
        ("Ogham Farmlands: Una's Lute (+2 pontos)", "item"),
        ("IMPORTANTE: Liberar Salvage Bench", "header"),
        ("Ogham Village: Renly's Workshop (SB)", "item"),
        ("Ogham Village: Mate Executor", "item"),
        ("Manor Ramparts: Pegue o Waypoint", "item"),
        ("Voltar Clearfell (Entregar Quests)", "item"),
        ("Ogham Manor: Candlemass (+Life)", "item"),
        ("Ogham Manor: Mate Geonor", "item"),
        ("Clearfell: Fale com Sin -> Ato 2", "item"),
    ],
    "Ato 2": [
        ("ATO 2 - ARDURA CARAVAN", "header"),
        ("Vastiri Outskirts: Falar com Zarka", "item"),
        ("Vastiri Outskirts: Mate o Rathbreaker", "item"),
        ("Ardura Caravan: Falar com NPCs", "item"),
        ("Mawdun Quarry: Mate Rudja", "item"),
        ("Halani Gates: Fale NPC e volte", "item"),
        ("Traitor's Passage: Mate Balbala", "item"),
        ("Halani Gates: Mate L'im the Impaler (Skill)", "item"),
        ("Halani Gates: Mate Jamanra", "item"),
        ("Mastodon Badlands: Lightless Passage (Abyss)", "item"),
        ("Mastodon Badlands: Effigy Secret (Sup gem)", "item"),
        ("Bone Pits: Sun Clan Relic", "item"),
        ("Bone Pits: Mate Iktab e Ekbab", "item"),
        ("Volte para o Ardura", "item"),
        ("KETH & TITANS", "header"),
        ("Keth: Mate Kabala (+2 Pontos)", "item"),
        ("Lost City: Kabala Clan Relic", "item"),
        ("Buried Shrines: Azarian (Essence Water)", "item"),
        ("Valley of Titans: Relic Altar (+Mana)", "item"),
        ("Titan Grotto: Mate Zalmarath", "item"),
        ("DESHAR & FINAL", "header"),
        ("Deshar: Fallen Dekhara (+2 Pontos)", "item"),
        ("Path of Mourning: Hushed Urn (Sup Gem)", "item"),
        ("Spires of Deshar: Sisters (+10% L. Res)", "item"),
        ("Ardura: Soar Trombeta -> Dreadnought", "item"),
        ("Dreadnought: Mate Jamanra", "item"),
        ("Ardura: Fale com Sin & Asala -> Ato 3", "item"),
    ],
    "Ato 3": [
        ("ATO 3 - ZIGGURAT ENCAMPMENT", "header"),
        ("Sandswept Marsh: Rootdredge (Skill Gem)", "item"),
        ("Orok Campfire: Lesser Jewellers Orb", "item"),
        ("Ziggurat Encampment -> Falar com NPCs", "item"),
        ("Jungle Ruins: Mate Silverfist (+2 pontos)", "item"),
        ("Venom Crypts: Pegue o Veneno", "item"),
        ("Infested Barrens: Achar Waypoint", "item"),
        ("Azak Bog: Mate Ignagduk (+30 Spirit)", "item"),
        ("Chimeral Wetlands: Mate Xyclucian", "item"),
        ("Temple of Chaos: 2ª Ascendencia", "item"),
        ("JIQUANI & CITY", "header"),
        ("Jiquani's Machinarium: Blackjaw (+Fire Res)", "item"),
        ("Jiquani's Sanctum: Mate Zicoatl", "item"),
        ("Matlan Waterways: Drene a água", "item"),
        ("Drowned City -> Molten Vault", "item"),
        ("Molten Vault: Mate Mektul (Reforge Bench)", "item"),
        ("NÃO PEGUE OS COGUMELOS", "header"),
        ("Apex of Filth: Mate Queen of Filth", "item"),
        ("Temple of Kopec: Mate Ketzuli", "item"),
        ("FINAL ATO 3", "header"),
        ("Utzaal: Mate Viper Napuatzi & Pegar Coração", "item"),
        ("Aggorat -> Altar do Coração", "item"),
        ("Black Chambers: Mate Doryani", "item"),
        ("Ziggurat: Fale com Alva -> Ato 4", "item"),
    ],
    "Ato 4": [
        ("ATO 4 - KINGSMARCH", "header"),
        ("Kingsmarch: Falar com NPCs", "item"),
        ("Isle of Kin: Blind Beast (+2 Pontos)", "item"),
        ("Isle of Kin: Map Piece", "item"),
        ("Isle of Kin: Beast Pen (Sup gem)", "item"),
        ("Isle of Kin: Fossilised Formation (Lesser Jeweller's)", "item"),
        ("Volcanic Warrens: Mate Krutog", "item"),
        ("Kedge Bay: Map Piece", "item"),
        ("Kedge Bay: Abandoned Ship (Lesser Jeweller's)", "item"),
        ("Journey's End: Mate Captain Hartlin", "item"),
        ("Abandoned Prison: Chave/Capela (+Life)", "item"),
        ("Solitary Confinement: Mate Prisioneiro", "item"),
        ("Eye of Hinekora -> Halls of the Dead", "item"),
        ("Halls of Dead: +5% Mana/Status/Passiva", "item"),
        ("Whakapanu: Great White One (Shark Fin)", "item"),
        ("Whakapanu: Map Piece", "item"),
        ("Singing Caverns: Mate Diamora", "item"),
        ("Singing Caverns: Pearl Amulet", "item"),
        ("Shrike Island: Map Piece", "item"),
        ("FINAL APÓS JUNTAR OS MAPAS", "header"),
        ("Arastas: Mate Torvian", "item"),
        ("The Excavation: Mate Benedictus", "item"),
        ("Ngakanu -> Heart of the Tribe", "item"),
        ("Heart of the Tribe: Mate Tavakai", "item"),
    ],
    "Interlúdio": [
        ("INTERLÚDIO", "header"),
        ("CURSE OF HOLTEN", "header"),
        ("Scorched Farmlands: Mate Isolde e Heldra", "item"),
        ("Stones of Serle: Mate Siora", "item"),
        ("Holten: Ferryman (Vende Runas por Gold!)", "item"),
        ("Wolvenhold: Mate Oswin (+2 Pontos)", "item"),
        ("Holten State: Thane Wulfric e Lady Elyswyth", "item"),
        ("THE STOLEN BARYA", "header"),
        ("Khari Crossing: Skullmaw (+5% Life)", "item"),
        ("Khari Crossing: Mate Atkhi e Anundr", "item"),
        ("Sel Khari Sanctuary: Mate Elzarah", "item"),
        ("Galai Gates: Mate Vornas", "item"),
        ("Qimah: Orbala's Pillar (Buff)", "item"),
        ("Qimah Reservoir: Mate Azmadi", "item"),
        ("DORYANI CONTINGENCY", "header"),
        ("Ashen Forest: Ancient Monument (Skill)", "item"),
        ("Kriar Village: Mate Lythara (+40 Spirit)", "item"),
        ("Glacial Tarn: Mate Rakkar", "item"),
        ("Howling Caves: Mate Yeti (+2 Pontos)", "item"),
        ("Kriar Peaks: Elder (Unique Item)", "item"),
        ("Etched Ravine: Mate Stormgore", "item"),
        ("Cuachic Vault: Mate Zelina e Zolin", "item"),
        ("Kingsmarch: Entregue quests (+2 pts)", "item"),
        ("CHEGOU NO ENDGAME! GL & HF!", "header"),
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
