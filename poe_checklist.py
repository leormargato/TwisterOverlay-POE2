## Twister Overlay POE 2
## Desenvolvido por: Léo Ramalho - TwisterPOE
## Sinta-se livre para contribuir com este projeto, peço apenas que me credite como autor original.
##Obrigado à todos, bom jogo!

import tkinter as tk
from tkinter import ttk
import json
import os


# --- ARQUIVO DE SALVAMENTO ---
SAVE_FILE = "poe2_save_data.json"

# --- DADOS DOS ATOS ---
ACTS_DATA = {
    "Info": [
        ("Sobre o APP", "header", "#e8c366"),
        ("Twister Overlay™ POE 2", "text", "#ffffff"),
        ("Desenvolvido por: Léo Ramalho (TwisterPOE)", "text", "#ffffff"),
        ("Versão: 2.0", "text", "#ffffff"),
        
        ("★ Salvamento automático & Modo Foco!", "header", "#e8c366"),

        ("✓ Legenda de Cores", "header", "#e8c366"),
        ("Cinza: Objetivo Normal / Padrão", "text", "#cccccc"),
        ("Vermelho: Importante / Crítico", "text", "#ff5555"),
        ("Verde: Opcional / Side Quest", "text", "#55ff55"),
        ("Azul: Objetivo Único (Permanentes por liga)", "text", "#55bbff"),
        
        ("⚔︎ Modo Foco", "header", "#e8c366"),
        ("Clique no botão [▣] no topo para ativar.", "text", "#ffffff"),
        ("Use 'PULAR' para deixar a missão para o final do Ato.", "text", "#ffffff"),
        ("Funciona nas abas de ato e interlúdio", "text", "#ffffff"),

        ("⚠︎ Observações:", "header", "#e8c366"),
        ("Os objetivos únicos devem ser feitos apenas uma vez por liga.", "text", "#ffffff"),
        ("Na sua primeira campanha da liga, é essencial fazer TODOS os objetivos!", "text" , "#ffffff"),
        ("Se gostou do aplicativo, considere me apoiar deixando um like no YouTube e GitHub! ♥", "text", "#ffffff"),

        ("❤ Obrigado por usar o Twister Overlay™!", "header", "#e8c366"),
        ("Bom jogo, boa sorte e boa liga! (•◡•)/", "header", "#e8c366")
    ],
    "Ato 1": [
        ("ATO 1 - ACAMPAMENTO CLEARFELL", "header", "#e8c366"),
        ("Margem do Rio: Mate o Miller", "item", "#cccccc"),
        ("Acampamento Clearfell: Falar com NPCs", "item", "#cccccc"),
        ("Clearfell: Mate Beira (+10% Res. Gelo)", "item", "#ff5555"), 
        ("Clearfell: Baú Abandonado (Gema Hab.)", "item", "#55ff55"),
        ("Toca da Lama: Mate o Devorador", "item", "#cccccc"),
        ("Grelwood: Mate Areagne (Gema Hab.)", "item", "#55ff55"),
        ("Opcional: Ponto de Passagem (Grim Tangle)", "item", "#55ff55"), 
        ("Falar com Una -> Vale Vermelho", "item", "#cccccc"),
        ("Vale Vermelho: Mate o Rei da Ferrugem", "item", "#cccccc"),
        ("Voltar Clearfell: Ferreiro (Runas)", "item", "#cccccc"),
        ("Grelwood: Libertar Sin", "item", "#cccccc"),
        ("Voltar Clearfell: Fale com Una", "item", "#cccccc"),
        ("Emaranhado Sombrio: Matar Chefe", "item", "#cccccc"),
        ("Cemitério dos Eternos: Fale com Lachlann", "item", "#cccccc"),
        ("Tumba do Consorte: Tesouro (Gema Hab.)", "item", "#55ff55"),
        ("Tumba do Consorte: Mate Asinia", "item", "#cccccc"),
        ("Mausoléu: Mate Draven", "item", "#cccccc"),
        ("Cemitério dos Eternos: Mate Lachlann", "item", "#cccccc"),
        ("Campos de Caça: Pegue o Ponto de Passagem", "item", "#cccccc"),
        ("Voltar Clearfell (Entregar Missões)", "item", "#cccccc"),
        ("ATO 1 - CAMPOS DE CAÇA", "header", "#e8c366"),
        ("Freythorn: Rei das Brumas (+30 Espírito)", "item", "#ff5555"),
        ("Campos de Caça: Mate Crowbell (+2 Pontos)", "item", "#ff5555"),
        ("Campos de Caça: Ritual Driádico (Gema Hab.)", "item", "#55ff55"),
        ("Fazendas Ogham: Alaúde da Una (+2 Pontos)", "item", "#ff5555"),
        ("Vila Ogham: Oficina do Renly (Bancada de Reciclagem)", "item", "#55bbff"),
        ("Vila Ogham: Mate o Executor", "item", "#cccccc"),
        ("Muralhas da Mansão: Ponto de Passagem", "item", "#cccccc"),
        ("Voltar Clearfell (Entregar Missões)", "item", "#cccccc"),
        ("Mansão Ogham: Candlemass (+Vida)", "item", "#ff5555"),
        ("Mansão Ogham: Mate Geonor", "item", "#ff5555"),
        ("Clearfell: Fale com Sin -> Ato 2", "item", "#cccccc"),
    ],
    "Ato 2": [
        ("ATO 2 - CARAVANA ARDURA", "header", "#e8c366"),
        ("Arredores de Vastiri: Falar com Zarka", "item", "#cccccc"),
        ("Arredores de Vastiri: Mate o Rathbreaker", "item", "#cccccc"),
        ("Caravana Ardura: Falar com NPCs", "item", "#cccccc"),
        ("Pedreira Mawdun: Mate Rudja", "item", "#cccccc"),
        ("Portões Halani: Fale com NPC e volte", "item", "#cccccc"),
        ("Passagem do Traidor: Mate Balbala", "item", "#cccccc"),
        ("Portões Halani: Mate Jamanra", "item", "#cccccc"),
        ("Terras Baldias: Passagem Sem Luz (Abyss)", "item", "#55ff55"),
        ("Terras Baldias: Segredo da Efígie (Gema Sup)", "item", "#55ff55"),
        ("Poços de Ossos: Relíquia do Clã do Sol", "item", "#cccccc"),
        ("Poços de Ossos: Mate Iktab e Ekbab", "item", "#cccccc"),
        ("Volte para a Caravana Ardura", "item", "#cccccc"),
        ("Provação dos Sekhemas: Primeira ascendência", "item", "#55ff55"),
        ("KETH & TITÃS", "header", "#e8c366"),
        ("Keth: Mate Kabala (+2 Pontos)", "item", "#ff5555"),
        ("Cidade Perdida: Relíquia do Clã Kabala", "item", "#cccccc"),
        ("Santuários Enterrados: Mate Azarian (Essência Água)", "item", "#cccccc"),
        ("Vale dos Titãs: Altar da Relíquia (+Charm efe/dur)", "item", "#cccccc"),
        ("Gruta do Titã: Mate Zalmarath", "item", "#cccccc"),
        ("Ardura: Soar Trombeta", "item", "#cccccc"),
        ("DESHAR & FINAL", "header", "#e8c366"),
        ("Deshar: Dekhara Caído (+2 Pontos)", "item", "#ff5555"),
        ("Caminho do Luto: Urna Silenciosa (Gema Sup)", "item", "#55ff55"),
        ("Torres de Deshar: Irmãs (+10% Res. Raio)", "item", "#ff5555"),
        ("Torres de Deshar: Mate Tor Gul", "item", "#cccccc"),
        ("Encouraçado: Mate Jamanra", "item", "#ff5555"),
        ("Ardura: Fale com Sin & Asala -> Ato 3", "item", "#cccccc"),
    ],
    "Ato 3": [
        ("ATO 3 - ACAMPAMENTO ZIGURATE", "header", "#e8c366"),
        ("Pântano das Areias: Mate Rootdredge (Gema Hab.)", "item", "#55ff55"),
        ("Fogueira Orok: Orbe de Joalheiro Menor", "item", "#55ff55"),
        ("Acampamento Zigurate -> Falar com NPCs", "item", "#cccccc"),
        ("Ruínas da Selva: Mate Punho de Prata (+2 pts)", "item", "#ff5555"),
        ("Criptas de Veneno: Pegue os Venenos (Buffs)", "item", "#55ff55"),
        ("Terras Infestadas: Achar Ponto de Passagem", "item", "#cccccc"),
        ("Pântano Azak: Mate Ignagduk (+30 Espírito)", "item", "#ff5555"),
        ("Pântanos Quiméricos: Mate Xyclucian", "item", "#cccccc"),
        ("Templo do Caos: 2ª Ascendência", "item", "#55ff55"),
        ("JIQUANI & CIDADE", "header", "#e8c366"),
        ("Maquinário de Jiquani: Mandíbula Negra (Res. Fogo)", "item", "#ff5555"),
        ("Santuário de Jiquani: Mate Zicoatl", "item", "#cccccc"),
        ("Canais de Matlan: Drene a água", "item", "#cccccc"),
        ("Cidade Afogada -> Cofre Derretido", "item", "#55ff55"),
        ("Cofre Derretido: Mate Mektul (Bancada Reforja)", "item", "#55bbff"),
        ("NÃO PEGUE OS COGUMELOS", "header", "#e8c366"),
        ("Ápice da Imundície: Mate Rainha da Imundície", "item", "#cccccc"),
        ("Templo de Kopec: Mate Ketzuli", "item", "#cccccc"),
        ("FINAL ATO 3", "header", "#e8c366"),
        ("Utzaal: Mate Viper Napuatzi & Pegue Coração", "item", "#ff5555"),
        ("Aggorat -> Altar do Coração (+2 Pontos)", "item", "#ff5555"),
        ("Câmaras Negras: Mate Doryani", "item", "#cccccc"),
        ("Zigurate: Fale com Alva -> Ato 4", "item", "#cccccc"),
    ],
    "Ato 4": [
        ("ATO 4 - KINGSMARCH", "header", "#e8c366"),
        ("Kingsmarch: Falar com NPCs", "item", "#cccccc"),
        ("Ilha de Kin: Besta Cega (+2 Pontos)", "item", "#ff5555"),
        ("Ilha de Kin: Fragmento de Mapa", "item", "#ff5555"),
        ("Ilha de Kin: Cercado das Bestas (Gema Sup)", "item", "#55ff55"),
        ("Ilha de Kin: Fóssil (Joalheiro Menor)", "item", "#55ff55"),
        ("Tocas Vulcânicas: Mate Krutog", "item", "#cccccc"),
        ("Baía de Kedge: Fragmento de Mapa", "item", "#ff5555"),
        ("Baía de Kedge: Navio Abandonado (Joalheiro)", "item", "#55ff55"),
        ("Fim da Jornada: Mate Capitão Hartlin", "item", "#cccccc"),
        ("Prisão Abandonada: Chave/Capela (+Vida)", "item", "#ff5555"),
        ("Confinamento Solitário: Mate o Prisioneiro", "item", "#cccccc"),
        ("Olho de Hinekora -> Salões dos Mortos", "item", "#cccccc"),
        ("Salões dos Mortos: +5% Mana/Status/Passiva", "item", "#ff5555"),
        ("Whakapanu: Grande Branco (Barbatana)", "item", "#ff5555"),
        ("Whakapanu: Fragmento de Mapa", "item", "#ff5555"),
        ("Cavernas Cantantes: Mate Diamora", "item", "#cccccc"),
        ("Cavernas Cantantes: Amuleto Perolado", "item", "#55ff55"),
        ("Ilha Shrike: Fragmento de Mapa", "item", "#ff5555"),
        ("FINAL APÓS JUNTAR OS MAPAS", "header", "#e8c366"),
        ("Arastas: Mate Torvian", "item", "#cccccc"),
        ("A Escavação: Mate Benedictus", "item", "#cccccc"),
        ("Ngakanu -> Coração da Tribo", "item", "#cccccc"),
        ("Coração da Tribo: Mate Tavakai", "item", "#cccccc"),
    ],
    "Interlúdio": [
        ("INTERLÚDIO", "header", "#e8c366"),
        ("MALDIÇÃO DE HOLTEN", "header", "#e8c366"),
        ("Fazendas Queimadas: Mate Isolde e Heldra", "item", "#cccccc"),
        ("Pedras de Serle: Mate Siora", "item", "#cccccc"),
        ("Holten: Barqueiro (Vende Runas por Ouro!)", "item", "#55bbff"),
        ("Wolvenhold: Mate Oswin (+2 Pontos)", "item", "#ff5555"),
        ("Propriedade Holten: Thane Wulfric e Lady Elyswyth", "item", "#cccccc"),
        ("A BARYA ROUBADA", "header", "#e8c366"),
        ("Cruzamento Khari: Skullmaw (+5% Vida)", "item", "#ff5555"),
        ("Cruzamento Khari: Mate Atkhi e Anundr", "item", "#cccccc"),
        ("Santuário Sel Khari: Mate Elzarah", "item", "#cccccc"),
        ("Portões Galai: Mate Vornas", "item", "#cccccc"),
        ("Qimah: Pilar de Orbala (Buffs)", "item", "#ff5555"),
        ("Reservatório Qimah: Mate Azmadi", "item", "#cccccc"),
        ("CONTINGÊNCIA DE DORYANI", "header", "#e8c366"),
        ("Floresta das Cinzas: Monumento (Habilidade)", "item", "#55ff55"),
        ("Vila Kriar: Mate Lythara (+40 Espírito)", "item", "#ff5555"),
        ("Lago Glacial: Mate Rakkar", "item", "#cccccc"),
        ("Cavernas Uivantes: Mate Yeti (+2 Pontos)", "item", "#ff5555"),
        ("Picos Kriar: Ancião (Item Único)", "item", "#55ff55"),
        ("Ravina Gravada: Mate Stormgore", "item", "#cccccc"),
        ("Cofre Cuachic: Mate Zelina e Zolin", "item", "#cccccc"),
        ("Kingsmarch: Entregue missões (+2 pts)", "item", "#ff5555"),
        ("CHEGOU NO ENDGAME! BOA SORTE!", "header", "#e8c366"),
    ]
}

class PoEOverlay:
    def __init__(self, root):
        self.root = root
        self.root.title("Fluxograma POE 2 by: TwisterPOE")
        
        # Variáveis de Estado
        self.is_collapsed = False
        self.is_focus_mode = False
        self.current_act = "Info"
        self.expanded_height = 500
        self.focus_height = 170
        self.skipped_indices = set() # Armazena índices pulados temporariamente
        
        # Configurações da Janela
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.85)
        self.root.overrideredirect(True)
        self.root.configure(bg='#0f0f0f')
        self.root.geometry(f"325x{self.expanded_height}+20+100")
        
        # Estilos
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure("Normal.TCheckbutton", background='#0f0f0f', foreground='#cccccc', font=('Segoe UI', 9))
        style.configure("Critico.TCheckbutton", background='#0f0f0f', foreground='#ff6666', font=('Segoe UI', 9, 'bold'))
        style.configure("Opcional.TCheckbutton", background='#0f0f0f', foreground='#66ff66', font=('Segoe UI', 9, 'bold'))
        style.configure("Unique.TCheckbutton", background='#0f0f0f', foreground='#55bbff', font=('Segoe UI', 9, 'bold'))
        
        self.style_map = {
            "#cccccc": "Normal.TCheckbutton",
            "#ff5555": "Critico.TCheckbutton",
            "#55ff55": "Opcional.TCheckbutton",
            "#55bbff": "Unique.TCheckbutton"
        }
        
        # --- BARRA DE TÍTULO ---
        self.title_bar = tk.Frame(root, bg='#1a1a1a', height=30)
        self.title_bar.pack(fill=tk.X, side=tk.TOP)
        
        self.lbl_title = tk.Label(self.title_bar, text=":: Twister Overlay ::", bg='#1a1a1a', fg='white', font=('Arial Black', 9, 'bold'))
        self.lbl_title.pack(side=tk.LEFT, padx=5)
        
        btn_close = tk.Button(self.title_bar, text="X", command=root.quit, bg='#880000', fg='white', bd=0, width=3)
        btn_close.pack(side=tk.RIGHT)

        self.btn_min = tk.Button(self.title_bar, text="_", command=self.toggle_collapse, bg='#333333', fg='white', bd=0, width=3)
        self.btn_min.pack(side=tk.RIGHT, padx=1)

        self.btn_focus = tk.Button(self.title_bar, text="▣", command=self.toggle_focus_mode, bg='#333333', fg='#55ff55', bd=0, width=3)
        self.btn_focus.pack(side=tk.RIGHT, padx=1)

        # Eventos de Arrastar
        self.title_bar.bind('<Button-1>', self.start_move)
        self.title_bar.bind('<B1-Motion>', self.do_move)
        self.lbl_title.bind('<Button-1>', self.start_move)
        self.lbl_title.bind('<B1-Motion>', self.do_move)

        # --- ÁREA DE CONTEÚDO LISTA ---
        self.list_container = tk.Frame(root, bg='#0f0f0f')
        self.list_container.pack(side="top", fill="both", expand=True)

        self.canvas = tk.Canvas(self.list_container, bg='#0f0f0f', highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.list_container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg='#0f0f0f')

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True, padx=5)
        self.scrollbar.pack(side="right", fill="y")
        self.root.bind_all("<MouseWheel>", self._on_mousewheel)

        # --- ÁREA DE CONTEÚDO FOCO ---
        self.focus_frame = tk.Frame(root, bg='#0f0f0f')
        self.lbl_focus_header = tk.Label(self.focus_frame, text="", bg='#0f0f0f', fg='#e8c366', font=('Arial Black', 9))
        self.lbl_focus_header.pack(pady=(5,0))
        
        self.lbl_focus_task = tk.Label(self.focus_frame, text="", bg='#0f0f0f', fg='#cccccc', font=('Segoe UI', 10), wraplength=300)
        self.lbl_focus_task.pack(pady=5, expand=True)

        # Container dos botões de ação
        self.focus_btns_frame = tk.Frame(self.focus_frame, bg='#0f0f0f')
        self.focus_btns_frame.pack(fill=tk.X, padx=10, pady=10)

        # Botão Pular
        self.btn_focus_skip = tk.Button(self.focus_btns_frame, text="PULAR ⏭", command=self.skip_focus_task, 
                                        bg='#333333', fg='#e8c366', font=('Segoe UI', 8, 'bold'), relief='flat')
        # Botão Concluir
        self.btn_focus_complete = tk.Button(self.focus_btns_frame, text="CONCLUIR ✓", command=self.complete_focus_task, 
                                            bg='#228822', fg='white', font=('Segoe UI', 8, 'bold'), relief='flat')


        # --- BARRA DE NAVEGAÇÃO ---
        self.nav_frame = tk.Frame(root, bg='#1a1a1a', height=30)
        self.nav_frame.pack(side="bottom", fill=tk.X)

        acts = list(ACTS_DATA.keys())
        for act_name in acts:
            btn_text = act_name.replace("Ato ", "A").replace("Interlúdio", "Int")
            if act_name == "Info": btn_text = "Info"

            btn = tk.Button(self.nav_frame, text=btn_text, 
                            command=lambda a=act_name: self.load_act(a),
                            bg='#333', fg='white', bd=1, relief="flat", font=('Segoe UI', 8))
            btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=1, pady=1)

        # --- CARREGAMENTO ---
        self.saved_data = self.load_progress()
        self.task_states = {}
        for act in ACTS_DATA:
            self.task_states[act] = []
            for i, item in enumerate(ACTS_DATA[act]):
                 var = tk.BooleanVar()
                 if act in self.saved_data and i < len(self.saved_data[act]):
                     var.set(self.saved_data[act][i])
                 self.task_states[act].append(var)

        self.load_act("Info")

    # --- FUNÇÕES GERAIS ---
    def load_progress(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as f:
                    return json.load(f)
            except:
                return {}
        return {}

    def auto_save(self):
        data_to_save = {}
        for act, vars_list in self.task_states.items():
            data_to_save[act] = [v.get() for v in vars_list]
        with open(SAVE_FILE, "w") as f:
            json.dump(data_to_save, f)
        
        if self.is_focus_mode:
            self.update_focus_view()

    # --- LÓGICA DE MODO FOCO ---
    def toggle_focus_mode(self):
        if self.current_act == "Info": return 

        if not self.is_focus_mode:
            self.is_focus_mode = True
            self.list_container.pack_forget()
            self.focus_frame.pack(side="top", fill="both", expand=True)
            
            x = self.root.winfo_x()
            y = self.root.winfo_y()
            self.root.geometry(f"325x{self.focus_height}+{x}+{y}")
            self.btn_focus.config(bg='#55ff55', fg='#000000')
            self.update_focus_view()
        else:
            self.is_focus_mode = False
            self.focus_frame.pack_forget()
            self.list_container.pack(side="top", fill="both", expand=True)
            
            x = self.root.winfo_x()
            y = self.root.winfo_y()
            self.root.geometry(f"325x{self.expanded_height}+{x}+{y}")
            self.btn_focus.config(bg='#333333', fg='#55ff55')

    def skip_focus_task(self):
        """Pula a tarefa atual (adiciona à lista de ignorados temporários)"""
        if hasattr(self, 'current_focus_index'):
            self.skipped_indices.add(self.current_focus_index)
            self.update_focus_view()

    def update_focus_view(self):
        """Encontra a próxima tarefa não concluída (e não pulada)"""
        tasks = ACTS_DATA[self.current_act]
        states = self.task_states[self.current_act]
        
        # Função auxiliar para buscar
        def find_next(skip_list):
            header = self.current_act
            for i, task_data in enumerate(tasks):
                text, type_ = task_data[0], task_data[1]
                color = task_data[2] if len(task_data) > 2 else "#cccccc"
                
                if type_ == "header":
                    header = text
                elif type_ == "item":
                    # Se não estiver marcado E não estiver na lista de pulados
                    if not states[i].get() and i not in skip_list:
                         return i, header, text, color
            return None

        # 1. Tenta achar tarefa ignorando os pulados
        result = find_next(self.skipped_indices)
        
        # 2. Se não achou nada, mas tem coisas puladas, RESETA os pulados e busca de novo (Ciclo)
        if result is None and len(self.skipped_indices) > 0:
            self.skipped_indices.clear()
            result = find_next(self.skipped_indices)

        if result:
            i, header, text, color = result
            self.lbl_focus_header.config(text=header)
            self.lbl_focus_task.config(text=text, fg=color)
            self.current_focus_index = i
            
            # Atualiza botão completar
            if color == "#ff5555": 
                 self.btn_focus_complete.config(bg='#aa2222', text="CONCLUIR (IMPORTANTE)")
            else:
                 self.btn_focus_complete.config(bg='#228822', text="CONCLUIR ✓")
            
            # Mostra botões
            self.btn_focus_skip.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
            self.btn_focus_complete.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
            
        else:
            # Acabou tudo
            self.lbl_focus_header.config(text=self.current_act)
            self.lbl_focus_task.config(text="Todas as tarefas deste Ato foram concluídas!", fg='#55ff55')
            self.btn_focus_complete.pack_forget()
            self.btn_focus_skip.pack_forget()

    def complete_focus_task(self):
        if hasattr(self, 'current_focus_index'):
            self.task_states[self.current_act][self.current_focus_index].set(True)
            self.auto_save()

    # --- UI LAYOUT ---
    def toggle_collapse(self):
        target_frame = self.focus_frame if self.is_focus_mode else self.list_container
        target_height = self.focus_height if self.is_focus_mode else self.expanded_height

        if self.is_collapsed:
            x = self.root.winfo_x()
            y = self.root.winfo_y()
            self.root.geometry(f"325x{target_height}+{x}+{y}")
            
            target_frame.pack(side="top", fill="both", expand=True)
            if not self.is_focus_mode: 
                self.scrollbar.pack(side="right", fill="y")
            
            self.nav_frame.pack(side="bottom", fill=tk.X)
            self.btn_min.config(text="_", bg='#333333')
            self.is_collapsed = False
        else:
            x = self.root.winfo_x()
            y = self.root.winfo_y()
            target_frame.pack_forget()
            if not self.is_focus_mode:
                self.scrollbar.pack_forget()
            self.nav_frame.pack_forget()
            self.root.geometry(f"325x30+{x}+{y}")
            self.btn_min.config(text="+", bg='#555555')
            self.is_collapsed = True

    def load_act(self, act_name):
        self.current_act = act_name
        self.skipped_indices.clear() # Limpa pulos ao mudar de ato
        
        if self.is_focus_mode:
            if act_name == "Info":
                self.toggle_focus_mode()
            else:
                self.update_focus_view()
            self.lbl_title.config(text=f" {act_name} - TwisterOverlay™ ⚔︎")
            return

        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        self.lbl_title.config(text=f" {act_name} - TwisterOverlay™ ⚔︎")

        tasks = ACTS_DATA[act_name]
        states = self.task_states[act_name]

        for i, task_data in enumerate(tasks):
            text = task_data[0]
            type_ = task_data[1]
            color_code = task_data[2] if len(task_data) > 2 else "#cccccc"

            if type_ == "header":
                lbl = tk.Label(self.scrollable_frame, text=text, bg='#0f0f0f', fg='#e8c366', 
                               font=('Arial Black', 9), anchor='w', wraplength=280)
                lbl.pack(fill=tk.X, pady=(10, 2))
            elif type_ == "text":
                lbl = tk.Label(self.scrollable_frame, text=text, bg='#0f0f0f', fg=color_code, 
                               font=('Segoe UI', 9), anchor='w', justify='left', wraplength=280)
                lbl.pack(fill=tk.X, pady=(1, 1), padx=5)
            else:
                style_name = self.style_map.get(color_code, "Normal.TCheckbutton")
                chk = ttk.Checkbutton(self.scrollable_frame, text=text, variable=states[i], 
                                      onvalue=True, offvalue=False, style=style_name,
                                      command=self.auto_save) 
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
        if not self.is_collapsed and not self.is_focus_mode:
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

if __name__ == "__main__":
    root = tk.Tk()
    app = PoEOverlay(root)
    root.mainloop()
