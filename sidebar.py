import tkinter as tk
from tkinter import ttk
from variable import color

class Sidebar(tk.Frame):
    def __init__(self, parent, main_content):
        super().__init__(parent, width=250, bg=color.get("sidebar"))
        self.pack(side="left", fill="y")
        self.main_content = main_content
        self.pack_propagate(False)
        self.current_button = None
        self.buttons = {}
        
        self.create_header()
        self.create_separator()
        self.create_buttons()
        
    def create_header(self):
        """Créer un en-tête pour la sidebar"""
        header_frame = tk.Frame(self, bg=color.get("sidebar"), height=80)
        header_frame.pack(fill="x", pady=(10, 20))
        header_frame.pack_propagate(False)
        
        # Logo ou titre de l'application
        title_label = tk.Label(
            header_frame,
            text="☀️Solar App",
            font=("Arial", 16, "bold"),
            fg="white",
            bg=color.get("sidebar")
        )
        title_label.pack(pady=20)
        
    def create_separator(self):
        """Créer une ligne de séparation"""
        separator = tk.Frame(self, height=1, bg="gray30")
        separator.pack(fill="x", padx=10, pady=(0, 20))
        
    def create_buttons(self):
        """Créer les boutons de navigation avec style amélioré"""
        
        # Liste des boutons avec leurs icônes et pages
        button_data = [
            ("🏠 Accueil", "accueil"),
            ("📈 Statistiques", "statistiques"),
            ("⚙️ Paramètres", "parametres"),
            ("📝 Rapports", "rapports"),
            ("👤 Profil", "profil"),
            ("❓ Aide", "aide")
        ]
        
        for text, page in button_data:
            self.create_nav_button(text, page)
            
        # Espaceur pour pousser le bouton de déconnexion vers le bas
        spacer = tk.Frame(self, bg=color.get("sidebar"))
        spacer.pack(fill="both", expand=True)
        
        # Bouton de déconnexion en bas
        self.create_logout_button()
        
    def create_nav_button(self, text, page):
        """Créer un bouton de navigation stylisé"""
        
        # Frame conteneur pour le bouton
        button_frame = tk.Frame(self, bg=color.get("sidebar"))
        button_frame.pack(fill="x", padx=10, pady=2)
        
        button = tk.Button(
            button_frame,
            text=text,
            font=("Arial", 11),
            fg="white",
            bg=color.get("button_side_bar"),
            activebackground=color.get("button_side_bar_hover", "#4a5568"),
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2",
            anchor="w",
            padx=15,
            pady=12,
            command=lambda p=page, b=button_frame: self.on_button_click(p, b)
        )
        button.pack(fill="x")
        
        # Stocker la référence du bouton
        self.buttons[page] = button_frame
        
        # Effet hover
        self.add_hover_effect(button)
        
        # Sélectionner le premier bouton par défaut
        if page == "accueil":
            self.set_active_button(button_frame)
            
    def create_logout_button(self):
        """Créer le bouton de déconnexion"""
        logout_frame = tk.Frame(self, bg=color.get("sidebar"))
        logout_frame.pack(fill="x", padx=10, pady=(10, 20), side="bottom")
        
        logout_button = tk.Button(
            logout_frame,
            text="🚪 Déconnexion",
            font=("Arial", 11),
            fg="white",
            bg="#e53e3e",
            activebackground="#c53030",
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2",
            anchor="w",
            padx=15,
            pady=12,
            command=self.logout
        )
        logout_button.pack(fill="x")
        self.add_hover_effect(logout_button, hover_color="#c53030")
        
    def add_hover_effect(self, button, hover_color=None):
        """Ajouter un effet de survol au bouton"""
        original_bg = button.cget("bg")
        if hover_color is None:
            hover_color = color.get("button_side_bar_hover", "#4a5568")
            
        def on_enter(event):
            button.configure(bg=hover_color)
            
        def on_leave(event):
            button.configure(bg=original_bg)
            
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
    def on_button_click(self, page, button_frame):
        """Gérer le clic sur un bouton"""
        self.set_active_button(button_frame)
        self.main_content.show_page(page)
        
    def set_active_button(self, active_frame):
        """Mettre en surbrillance le bouton actif"""
        # Réinitialiser tous les boutons
        for frame in self.buttons.values():
            frame.configure(bg=color.get("sidebar"))
            for child in frame.winfo_children():
                if isinstance(child, tk.Button):
                    child.configure(bg=color.get("button_side_bar"))
                    
        # Activer le bouton sélectionné
        active_frame.configure(bg=color.get("active_button_bg", "#2d3748"))
        for child in active_frame.winfo_children():
            if isinstance(child, tk.Button):
                child.configure(bg=color.get("active_button_bg", "#2d3748"))
                
        self.current_button = active_frame
        
    def logout(self):
        """Fonction de déconnexion"""
        # Ici vous pouvez ajouter votre logique de déconnexion
        print("Déconnexion...")
        # Exemple: self.main_content.show_login_screen()
        
    def update_colors(self):
        """Méthode pour mettre à jour les couleurs si nécessaire"""
        self.configure(bg=color.get("sidebar"))
        # Mettre à jour les couleurs des boutons si les couleurs changent
        for page, frame in self.buttons.items():
            for child in frame.winfo_children():
                if isinstance(child, tk.Button):
                    child.configure(
                        bg=color.get("button_side_bar"),
                        activebackground=color.get("button_side_bar_hover", "#4a5568")
                    )