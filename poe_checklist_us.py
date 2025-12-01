## Twister Overlay POE 2 - Versão Inglês
## Desenvolvido por: Léo Ramalho - TwisterPOE
## Sinta-se livre para contribuir com este projeto, peço apenas que me credite como autor original.
##Obrigado à todos, bom jogo!

import tkinter as tk
from tkinter import ttk

# --- DADOS DOS ATOS ---
ACTS_DATA = {
    "Act 1": [
        ("ACT 1 - CLEARFELL ENCAMPMENT", "header"),
        ("Riverbank: Kill Miller", "item"),
        ("Clearfell Encampment: Talk to NPCs", "item"),
        ("Clearfell: Kill Beira (+10% Cold Res)", "item"),
        ("Clearfell: Abandoned Stash (Skill)", "item"),
        ("Mud Burrow: Kill Devourer", "item"),
        ("Grelwood: Kill Areagne (Skill)", "item"),
        ("Optional: Waypoint (Grim Tangle)", "item"),
        ("Talk to Una -> Red Vale", "item"),
        ("Red Vale: Kill Rust King", "item"),
        ("Return Clearfell: Blacksmith (Runes)", "item"),
        ("Grelwood: Free Sin", "item"),
        ("Return Clearfell: Talk to Una", "item"),
        ("Grim Tangle: Kill Boss", "item"),
        ("Cemetery of Eternals: Talk to Lachlann", "item"),
        ("Tomb of Consort: Haunted Treasure (Skill)", "item"),
        ("Tomb of Consort: Kill Asinia", "item"),
        ("Mausoleum: Kill Draven", "item"),
        ("Cemetery of Eternals: Kill Lachlann", "item"),
        ("Hunting Grounds: Grab Waypoint", "item"),
        ("Return Clearfell (Turn in Quests)", "item"),
        ("ACT 1 - HUNTING GROUNDS", "header"),
        ("Freythorn: King of the Mists (+30 Spirit)", "item"),
        ("Hunting Grounds: Kill Crowbell (+2 Passive Pts)", "item"),
        ("Hunting Grounds: Dryadic Ritual (Skill)", "item"),
        ("Ogham Farmlands: Una's Lute (+2 Passive Pts)", "item"),
        ("IMPORTANT: Unlock Salvage Bench", "header"),
        ("Ogham Village: Renly's Workshop (Salvage)", "item"),
        ("Ogham Village: Kill Executor", "item"),
        ("Manor Ramparts: Grab Waypoint", "item"),
        ("Return Clearfell (Turn in Quests)", "item"),
        ("Ogham Manor: Candlemass (+Life)", "item"),
        ("Ogham Manor: Kill Geonor", "item"),
        ("Clearfell: Talk to Sin -> Act 2", "item"),
    ],
    "Act 2": [
        ("ACT 2 - ARDURA CARAVAN", "header"),
        ("Vastiri Outskirts: Talk to Zarka", "item"),
        ("Vastiri Outskirts: Kill Rathbreaker", "item"),
        ("Ardura Caravan: Talk to NPCs", "item"),
        ("Mawdun Quarry: Kill Rudja", "item"),
        ("Halani Gates: Talk to NPC & Return", "item"),
        ("Traitor's Passage: Kill Balbala", "item"),
        ("Halani Gates: Kill L'im (Skill)", "item"),
        ("Halani Gates: Kill Jamanra", "item"),
        ("Mastodon Badlands: Lightless Passage (Abyss)", "item"),
        ("Mastodon Badlands: Effigy Secret (Support Gem)", "item"),
        ("The Bone Pits: Sun Clan Relic", "item"),
        ("The Bone Pits: Kill Iktab & Ekbab", "item"),
        ("Return to Ardura Caravan", "item"),
        ("KETH & TITANS", "header"),
        ("Keth: Kill Kabala (+2 Passive Pts)", "item"),
        ("The Lost City: Kabala Clan Relic", "item"),
        ("Buried Shrines: Azarian (Essence of Water)", "item"),
        ("Valley of the Titans: Relic Altar (+Mana)", "item"),
        ("Titan Grotto: Kill Zalmarath", "item"),
        ("DESHAR & FINALE", "header"),
        ("Deshar: Fallen Dekhara (+2 Passive Pts)", "item"),
        ("Path of Mourning: Hushed Urn (Support Gem)", "item"),
        ("Spires of Deshar: Sisters (+10% Light. Res)", "item"),
        ("Ardura: Blow Horn -> Dreadnought", "item"),
        ("Dreadnought: Kill Jamanra", "item"),
        ("Ardura: Talk to Sin & Asala -> Act 3", "item"),
    ],
    "Act 3": [
        ("ACT 3 - ZIGGURAT ENCAMPMENT", "header"),
        ("Sandswept Marsh: Rootdredge (Skill Gem)", "item"),
        ("Orok Campfire: Lesser Jeweller's Orb", "item"),
        ("Ziggurat Encampment -> Talk to NPCs", "item"),
        ("Jungle Ruins: Kill Silverfist (+2 Passive Pts)", "item"),
        ("Venom Crypts: Get Poison", "item"),
        ("Infested Barrens: Find Waypoint", "item"),
        ("Azak Bog: Kill Ignagduk (+30 Spirit)", "item"),
        ("Chimeral Wetlands: Kill Xyclucian", "item"),
        ("Temple of Chaos: 2nd Ascendancy", "item"),
        ("JIQUANI & CITY", "header"),
        ("Jiquani's Machinarium: Blackjaw (+Fire Res)", "item"),
        ("Jiquani's Sanctum: Kill Zicoatl", "item"),
        ("Matlan Waterways: Drain the Water", "item"),
        ("The Drowned City -> Molten Vault", "item"),
        ("Molten Vault: Kill Mektul (Reforge Bench)", "item"),
        ("DO NOT PICK THE MUSHROOMS", "header"),
        ("Apex of Filth: Kill Queen of Filth", "item"),
        ("Temple of Kopec: Kill Ketzuli", "item"),
        ("ACT 3 FINALE", "header"),
        ("Utzaal: Kill Viper Napuatzi & Get Heart", "item"),
        ("Aggorat -> Heart Altar", "item"),
        ("Black Chambers: Kill Doryani", "item"),
        ("Ziggurat: Talk to Alva -> Act 4", "item"),
    ],
    "Act 4": [
        ("ACT 4 - KINGSMARCH", "header"),
        ("Kingsmarch: Talk to NPCs", "item"),
        ("Isle of Kin: Blind Beast (+2 Passive Pts)", "item"),
        ("Isle of Kin: Map Piece", "item"),
        ("Isle of Kin: Beast Pen (Support Gem)", "item"),
        ("Isle of Kin: Fossilised Formation (Lesser Jeweller's)", "item"),
        ("Volcanic Warrens: Kill Krutog", "item"),
        ("Kedge Bay: Map Piece", "item"),
        ("Kedge Bay: Abandoned Ship (Lesser Jeweller's)", "item"),
        ("Journey's End: Kill Captain Hartlin", "item"),
        ("Abandoned Prison: Key/Chapel (+Life)", "item"),
        ("Solitary Confinement: Kill The Prisoner", "item"),
        ("Eye of Hinekora -> Halls of the Dead", "item"),
        ("Halls of the Dead: +5% Mana/Stats/Passive", "item"),
        ("Whakapanu: Great White One (Shark Fin)", "item"),
        ("Whakapanu: Map Piece", "item"),
        ("Singing Caverns: Kill Diamora", "item"),
        ("Singing Caverns: Pearlescent Amulet", "item"),
        ("Shrike Island: Map Piece", "item"),
        ("FINALE AFTER COLLECTING MAPS", "header"),
        ("Arastas: Kill Torvian", "item"),
        ("The Excavation: Kill Benedictus", "item"),
        ("Ngakanu -> Heart of the Tribe", "item"),
        ("Heart of the Tribe: Kill Tavakai", "item"),
    ],
    "Interlude": [
        ("INTERLUDE", "header"),
        ("CURSE OF HOLTEN", "header"),
        ("Scorched Farmlands: Kill Isolde & Heldra", "item"),
        ("Stones of Serle: Kill Siora", "item"),
        ("Holten: Ferryman (Sells Runes for Gold!)", "item"),
        ("Wolvenhold: Kill Oswin (+2 Passive Pts)", "item"),
        ("Holten Estate: Thane Wulfric & Lady Elyswyth", "item"),
        ("THE STOLEN BARYA", "header"),
        ("The Khari Crossing: Skullmaw (+5% Life)", "item"),
        ("The Khari Crossing: Kill Atkhi & Anundr", "item"),
        ("Sel Khari Sanctuary: Kill Elzarah", "item"),
        ("The Galai Gates: Kill Vornas", "item"),
        ("Qimah: Orbala's Pillar (Buff)", "item"),
        ("Qimah Reservoir: Kill Azmadi", "item"),
        ("DORYANI'S CONTINGENCY", "header"),
        ("Ashen Forest: Ancient Monument (Skill)", "item"),
        ("Kriar Village: Kill Lythara (+40 Spirit)", "item"),
        ("Glacial Tarn: Kill Rakkar", "item"),
        ("Howling Caves: Kill Yeti (+2 Passive Pts)", "item"),
        ("Kriar Peaks: Elder (Unique Item)", "item"),
        ("Etched Ravine: Kill Stormgore", "item"),
        ("The Cuachic Vault: Kill Zelina & Zolin", "item"),
        ("Kingsmarch: Turn in Quests (+2 Pts)", "item"),
        ("REACHED ENDGAME! GL & HF!", "header"),
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
            btn = tk.Button(self.nav_frame, text=act_name.replace("Act ", "A").replace("Interlude", "Int"), 
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
