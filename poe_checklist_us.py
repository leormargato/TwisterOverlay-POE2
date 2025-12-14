## Twister Overlay POE 2
## Developed by: Léo Ramalho - TwisterPOE
## Feel free to contribute to this project, I only ask that you credit me as the original author.
## Thanks everyone, have a good game!

import tkinter as tk
from tkinter import ttk
import json
import os


# --- SAVE FILE ---
SAVE_FILE = "poe2_save_data.json"

# --- ACTS DATA ---
ACTS_DATA = {
    "Info": [
        ("About the APP", "header", "#e8c366"),
        ("Twister Overlay™ POE 2", "text", "#ffffff"),
        ("Developed by: Léo Ramalho (TwisterPOE)", "text", "#ffffff"),
        ("Version: 2.0", "text", "#ffffff"),
        
        ("★ Auto-Save & Focus Mode!", "header", "#e8c366"),

        ("✓ Color Legend", "header", "#e8c366"),
        ("Gray: Normal / Standard Objective", "text", "#cccccc"),
        ("Red: Important / Critical", "text", "#ff5555"),
        ("Green: Optional / Side Quest", "text", "#55ff55"),
        ("Blue: Unique Objective (Permanent per league)", "text", "#55bbff"),
        
        ("⚔︎ Focus Mode", "header", "#e8c366"),
        ("Click the [▣] button at the top to enable.", "text", "#ffffff"),
        ("Use 'SKIP' to move the mission to the end of the Act.", "text", "#ffffff"),
        ("Works on Act and Interlude tabs", "text", "#ffffff"),

        ("⚠︎ Notes:", "header", "#e8c366"),
        ("Unique objectives only need to be done once per league.", "text", "#ffffff"),
        ("In your first league campaign, it is essential to do ALL objectives!", "text" , "#ffffff"),
        ("If you like the app, consider supporting me by leaving a like on YouTube and GitHub! ♥", "text", "#ffffff"),

        ("❤ Thanks for using Twister Overlay™!", "header", "#e8c366"),
        ("Good game, good luck and have a great league! (•◡•)/", "header", "#e8c366")
    ],
    "Act 1": [
        ("ACT 1 - CLEARFELL ENCAMPMENT", "header", "#e8c366"),
        ("Riverbank: Kill Miller", "item", "#cccccc"),
        ("Clearfell Encampment: Talk to NPCs", "item", "#cccccc"),
        ("Clearfell: Kill Beira (+10% Cold Res)", "item", "#ff5555"), 
        ("Clearfell: Abandoned Stash (Skill Gem)", "item", "#55ff55"),
        ("Mud Burrow: Kill Devourer", "item", "#cccccc"),
        ("Grelwood: Kill Areagne (Skill Gem)", "item", "#55ff55"),
        ("Optional: Waypoint (Grim Tangle)", "item", "#55ff55"), 
        ("Talk to Una -> Red Vale", "item", "#cccccc"),
        ("Red Vale: Kill Rust King", "item", "#cccccc"),
        ("Return Clearfell: Blacksmith (Runes)", "item", "#cccccc"),
        ("Grelwood: Free Sin", "item", "#cccccc"),
        ("Return Clearfell: Talk to Una", "item", "#cccccc"),
        ("Grim Tangle: Kill Boss", "item", "#cccccc"),
        ("Cemetery of Eternals: Talk to Lachlann", "item", "#cccccc"),
        ("Tomb of Consort: Haunted Treasure (Skill Gem)", "item", "#55ff55"),
        ("Tomb of Consort: Kill Asinia", "item", "#cccccc"),
        ("Mausoleum: Kill Draven", "item", "#cccccc"),
        ("Cemetery of Eternals: Kill Lachlann", "item", "#cccccc"),
        ("Hunting Grounds: Grab Waypoint", "item", "#cccccc"),
        ("Return Clearfell (Turn in Quests)", "item", "#cccccc"),
        ("ACT 1 - HUNTING GROUNDS", "header", "#e8c366"),
        ("Freythorn: King of the Mists (+30 Spirit)", "item", "#ff5555"),
        ("Hunting Grounds: Kill Crowbell (+2 Passive Pts)", "item", "#ff5555"),
        ("Hunting Grounds: Dryadic Ritual (Skill Gem)", "item", "#55ff55"),
        ("Ogham Farmlands: Una's Lute (+2 Passive Pts)", "item", "#ff5555"),
        ("Ogham Village: Renly's Workshop (Salvage Bench)", "item", "#55bbff"),
        ("Ogham Village: Kill Executor", "item", "#cccccc"),
        ("Manor Ramparts: Grab Waypoint", "item", "#cccccc"),
        ("Return Clearfell (Turn in Quests)", "item", "#cccccc"),
        ("Ogham Manor: Candlemass (+Life)", "item", "#ff5555"),
        ("Ogham Manor: Kill Geonor", "item", "#ff5555"),
        ("Clearfell: Talk to Sin -> Act 2", "item", "#cccccc"),
    ],
    "Act 2": [
        ("ACT 2 - ARDURA CARAVAN", "header", "#e8c366"),
        ("Vastiri Outskirts: Talk to Zarka", "item", "#cccccc"),
        ("Vastiri Outskirts: Kill Rathbreaker", "item", "#cccccc"),
        ("Ardura Caravan: Talk to NPCs", "item", "#cccccc"),
        ("Mawdun Quarry: Kill Rudja", "item", "#cccccc"),
        ("Halani Gates: Talk to NPC & Return", "item", "#cccccc"),
        ("Traitor's Passage: Kill Balbala", "item", "#cccccc"),
        ("Halani Gates: Kill Jamanra", "item", "#cccccc"),
        ("Mastodon Badlands: Lightless Passage (Abyss)", "item", "#55ff55"),
        ("Mastodon Badlands: Effigy Secret (Support Gem)", "item", "#55ff55"),
        ("The Bone Pits: Sun Clan Relic", "item", "#cccccc"),
        ("The Bone Pits: Kill Iktab & Ekbab", "item", "#cccccc"),
        ("Return to Ardura Caravan", "item", "#cccccc"),
        ("Trial of the Sekhemas: First Ascendancy", "item", "#55ff55"),
        ("KETH & TITANS", "header", "#e8c366"),
        ("Keth: Kill Kabala (+2 Passive Pts)", "item", "#ff5555"),
        ("The Lost City: Kabala Clan Relic", "item", "#cccccc"),
        ("Buried Shrines: Kill Azarian (Essence of Water)", "item", "#cccccc"),
        ("Valley of the Titans: Relic Altar (+Charm eff/dur)", "item", "#cccccc"),
        ("Titan Grotto: Kill Zalmarath", "item", "#cccccc"),
        ("Ardura: Blow Horn", "item", "#cccccc"),
        ("DESHAR & FINALE", "header", "#e8c366"),
        ("Deshar: Fallen Dekhara (+2 Passive Pts)", "item", "#ff5555"),
        ("Path of Mourning: Hushed Urn (Support Gem)", "item", "#55ff55"),
        ("Spires of Deshar: Sisters (+10% Light. Res)", "item", "#ff5555"),
        ("Spires of Deshar: Kill Tor Gul", "item", "#cccccc"),
        ("Dreadnought: Kill Jamanra", "item", "#ff5555"),
        ("Ardura: Talk to Sin & Asala -> Act 3", "item", "#cccccc"),
    ],
    "Act 3": [
        ("ACT 3 - ZIGGURAT ENCAMPMENT", "header", "#e8c366"),
        ("Sandswept Marsh: Kill Rootdredge (Skill Gem)", "item", "#55ff55"),
        ("Orok Campfire: Lesser Jeweller's Orb", "item", "#55ff55"),
        ("Ziggurat Encampment -> Talk to NPCs", "item", "#cccccc"),
        ("Jungle Ruins: Kill Silverfist (+2 Passive Pts)", "item", "#ff5555"),
        ("Venom Crypts: Get Poisons (Buffs)", "item", "#55ff55"),
        ("Infested Barrens: Find Waypoint", "item", "#cccccc"),
        ("Azak Bog: Kill Ignagduk (+30 Spirit)", "item", "#ff5555"),
        ("Chimeral Wetlands: Kill Xyclucian", "item", "#cccccc"),
        ("Temple of Chaos: 2nd Ascendancy", "item", "#55ff55"),
        ("JIQUANI & CITY", "header", "#e8c366"),
        ("Jiquani's Machinarium: Blackjaw (+Fire Res)", "item", "#ff5555"),
        ("Jiquani's Sanctum: Kill Zicoatl", "item", "#cccccc"),
        ("Matlan Waterways: Drain the Water", "item", "#cccccc"),
        ("The Drowned City -> Molten Vault", "item", "#55ff55"),
        ("Molten Vault: Kill Mektul (Reforge Bench)", "item", "#55bbff"),
        ("DO NOT PICK THE MUSHROOMS", "header", "#e8c366"),
        ("Apex of Filth: Kill Queen of Filth", "item", "#cccccc"),
        ("Temple of Kopec: Kill Ketzuli", "item", "#cccccc"),
        ("ACT 3 FINALE", "header", "#e8c366"),
        ("Utzaal: Kill Viper Napuatzi & Get Heart", "item", "#ff5555"),
        ("Aggorat -> Heart Altar (+2 Passive Pts)", "item", "#ff5555"),
        ("Black Chambers: Kill Doryani", "item", "#cccccc"),
        ("Ziggurat: Talk to Alva -> Act 4", "item", "#cccccc"),
    ],
    "Act 4": [
        ("ACT 4 - KINGSMARCH", "header", "#e8c366"),
        ("Kingsmarch: Talk to NPCs", "item", "#cccccc"),
        ("Isle of Kin: Map Piece", "item", "#ff5555"),
        ("Isle of Kin: Beast Pen (Support Gem)", "item", "#55ff55"),
        ("Isle of Kin: Fossilised Formation (Lesser Jeweller's)", "item", "#55ff55"),
        ("Volcanic Warrens: Kill Krutog", "item", "#cccccc"),
        ("Kedge Bay: Map Piece", "item", "#ff5555"),
        ("Kedge Bay: Abandoned Ship (Lesser Jeweller's)", "item", "#55ff55"),
        ("Journey's End: Kill Captain Hartlin", "item", "#cccccc"),
        ("Abandoned Prison: Key/Chapel (+Life)", "item", "#ff5555"),
        ("Solitary Confinement: Kill The Prisoner", "item", "#cccccc"),
        ("Shrike Island: Map Piece", "item", "#ff5555"),
        ("Shrike Island: Free Matiki -> Hinekora", "item", "#ff5555"),
        ("Eye of Hinekora -> Halls of the Dead", "item", "#cccccc"),
        ("Halls of the Dead: +5% Mana/Stats/Passive", "item", "#ff5555"),
        ("Whakapanu: Great White One (Shark Fin)", "item", "#ff5555"),
        ("Whakapanu: Map Piece", "item", "#ff5555"),
        ("Singing Caverns: Kill Diamora", "item", "#cccccc"),
        ("Singing Caverns: Pearlescent Amulet", "item", "#55ff55"),
        ("FINALE AFTER COLLECTING MAPS", "header", "#e8c366"),
        ("Arastas: Kill Torvian", "item", "#cccccc"),
        ("The Excavation: Kill Benedictus", "item", "#cccccc"),
        ("Ngakanu -> Heart of the Tribe", "item", "#cccccc"),
        ("Heart of the Tribe: Kill Tavakai", "item", "#cccccc"),
    ],
    "Interlude": [
        ("INTERLUDE", "header", "#e8c366"),
        ("CURSE OF HOLTEN", "header", "#e8c366"),
        ("Scorched Farmlands: Kill Isolde & Heldra", "item", "#cccccc"),
        ("Stones of Serle: Kill Siora", "item", "#cccccc"),
        ("The BlackWood -> Holten", "item", "#cccccc"),
        ("Holten: Ferryman (Sells Runes for Gold!)", "item", "#55bbff"),
        ("Wolvenhold: Kill Oswin (+2 Passive Pts)", "item", "#ff5555"),
        ("Holten Estate: Thane Wulfric & Lady Elyswyth", "item", "#cccccc"),
        ("THE STOLEN BARYA", "header", "#e8c366"),
        ("The Khari Crossing: Skullmaw (+5% Life)", "item", "#ff5555"),
        ("The Khari Crossing: Kill Atkhi & Anundr", "item", "#cccccc"),
        ("Pools of Khatal -> Sel Khari", "item", "#cccccc"),
        ("Sel Khari Sanctuary: Kill Elzarah", "item", "#cccccc"),
        ("The Galai Gates: Kill Vornas", "item", "#cccccc"),
        ("Qimah: Orbala's Pillar (Buffs)", "item", "#ff5555"),
        ("Qimah Reservoir: Kill Azmadi", "item", "#cccccc"),
        ("DORYANI'S CONTINGENCY", "header", "#e8c366"),
        ("Ashen Forest: Ancient Monument (Skill Gem)", "item", "#55ff55"),
        ("Kriar Village: Kill Lythara (+40 Spirit)", "item", "#ff5555"),
        ("Glacial Tarn: Kill Rakkar", "item", "#cccccc"),
        ("Howling Caves: Kill Yeti (+2 Passive Pts)", "item", "#ff5555"),
        ("Kriar Peaks: Elder (Unique Item)", "item", "#55ff55"),
        ("Etched Ravine: Kill Stormgore", "item", "#cccccc"),
        ("The Cuachic Vault: Kill Zelina & Zolin", "item", "#cccccc"),
        ("Kingsmarch: Turn in Quests (+2 Pts)", "item", "#ff5555"),
        ("REACHED ENDGAME! GL & HF!", "header", "#e8c366"),
    ]
}

class PoEOverlay:
    def __init__(self, root):
        self.root = root
        self.root.title("TwisterPOE Overlay 2.0")
        
        # State Variables
        self.is_collapsed = False
        self.is_focus_mode = False
        self.current_act = "Info"
        self.expanded_height = 500
        self.focus_height = 170
        self.skipped_indices = set() # Stores skipped indices temporarily
        
        # Window Configuration
        self.root.attributes('-topmost', True)
        self.root.attributes('-alpha', 0.85)
        self.root.overrideredirect(True)
        self.root.configure(bg='#0f0f0f')
        self.root.geometry(f"325x{self.expanded_height}+20+100")
        
        # Styles
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
        
        # --- TITLE BAR ---
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

        # Drag Events
        self.title_bar.bind('<Button-1>', self.start_move)
        self.title_bar.bind('<B1-Motion>', self.do_move)
        self.lbl_title.bind('<Button-1>', self.start_move)
        self.lbl_title.bind('<B1-Motion>', self.do_move)

        # --- LIST CONTENT AREA ---
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

        # --- FOCUS CONTENT AREA ---
        self.focus_frame = tk.Frame(root, bg='#0f0f0f')
        self.lbl_focus_header = tk.Label(self.focus_frame, text="", bg='#0f0f0f', fg='#e8c366', font=('Arial Black', 9))
        self.lbl_focus_header.pack(pady=(5,0))
        
        self.lbl_focus_task = tk.Label(self.focus_frame, text="", bg='#0f0f0f', fg='#cccccc', font=('Segoe UI', 10), wraplength=300)
        self.lbl_focus_task.pack(pady=5, expand=True)

        # Action Buttons Container
        self.focus_btns_frame = tk.Frame(self.focus_frame, bg='#0f0f0f')
        self.focus_btns_frame.pack(fill=tk.X, padx=10, pady=10)

        # Skip Button
        self.btn_focus_skip = tk.Button(self.focus_btns_frame, text="SKIP ⏭", command=self.skip_focus_task, 
                                        bg='#333333', fg='#e8c366', font=('Segoe UI', 8, 'bold'), relief='flat')
        # Complete Button
        self.btn_focus_complete = tk.Button(self.focus_btns_frame, text="COMPLETE ✓", command=self.complete_focus_task, 
                                            bg='#228822', fg='white', font=('Segoe UI', 8, 'bold'), relief='flat')


        # --- NAVIGATION BAR ---
        self.nav_frame = tk.Frame(root, bg='#1a1a1a', height=30)
        self.nav_frame.pack(side="bottom", fill=tk.X)

        acts = list(ACTS_DATA.keys())
        for act_name in acts:
            btn_text = act_name.replace("Act ", "A").replace("Interlude", "Int")
            if act_name == "Info": btn_text = "Info"

            btn = tk.Button(self.nav_frame, text=btn_text, 
                            command=lambda a=act_name: self.load_act(a),
                            bg='#333', fg='white', bd=1, relief="flat", font=('Segoe UI', 8))
            btn.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=1, pady=1)

        # --- LOADING ---
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

    # --- GENERAL FUNCTIONS ---
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

    # --- FOCUS MODE LOGIC ---
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
        """Skip current task (add to temporary skip list)"""
        if hasattr(self, 'current_focus_index'):
            self.skipped_indices.add(self.current_focus_index)
            self.update_focus_view()

    def update_focus_view(self):
        """Finds next incomplete (and not skipped) task"""
        tasks = ACTS_DATA[self.current_act]
        states = self.task_states[self.current_act]
        
        # Helper function to search
        def find_next(skip_list):
            header = self.current_act
            for i, task_data in enumerate(tasks):
                text, type_ = task_data[0], task_data[1]
                color = task_data[2] if len(task_data) > 2 else "#cccccc"
                
                if type_ == "header":
                    header = text
                elif type_ == "item":
                    # If not checked AND not in skip list
                    if not states[i].get() and i not in skip_list:
                         return i, header, text, color
            return None

        # 1. Try finding task ignoring skipped ones
        result = find_next(self.skipped_indices)
        
        # 2. If nothing found, but there are skipped items, RESET skipped list and search again (Cycle)
        if result is None and len(self.skipped_indices) > 0:
            self.skipped_indices.clear()
            result = find_next(self.skipped_indices)

        if result:
            i, header, text, color = result
            self.lbl_focus_header.config(text=header)
            self.lbl_focus_task.config(text=text, fg=color)
            self.current_focus_index = i
            
            # Update complete button
            if color == "#ff5555": 
                 self.btn_focus_complete.config(bg='#aa2222', text="COMPLETE (IMPORTANT)")
            else:
                 self.btn_focus_complete.config(bg='#228822', text="COMPLETE ✓")
            
            # Show buttons
            self.btn_focus_skip.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
            self.btn_focus_complete.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 0))
            
        else:
            # Everything done
            self.lbl_focus_header.config(text=self.current_act)
            self.lbl_focus_task.config(text="All tasks in this Act are complete!", fg='#55ff55')
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
        self.skipped_indices.clear() # Clear skipped list when changing act
        
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



