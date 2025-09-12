# ui_components_clean.py
import tkinter as tk
from accueil import create_accueil
from page_stat import create_stat
from variable import color
from page_ajout import create_page_ajout
from page_modifier import create_page_modifier

class MainContent(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=color.get("accueil"))
        self.pack_propagate(False)

        self.sidebar_width = 250  # Largeur sidebar
        self.parent = parent

        # Pack principal
        self.pack(side="right", fill="both", expand=True)

        # Container interne
        self.content_container = tk.Frame(self, bg=color.get("accueil"))
        self.content_container.pack(fill="both", expand=True)
        self.content_container.pack_propagate(False)

        # Pages
        self.pages = {}
        self.current_page = None
        self.page_creators = {
            "accueil": self.create_accueil_wrapper,
            "statistiques": self.create_stat_wrapper,
            "ajout": self.create_ajout_wrapper,
            "modifier": self.create_modifier_wrapper,
        }

        # Redimensionnement
        self.bind('<Configure>', lambda e: self.update_size_constraints())

        # Initialisation
        self.update_size_constraints()
        self.show_page("accueil")

    def update_size_constraints(self):
        """Mettre à jour la taille du container en fonction de la fenêtre"""
        root = self.winfo_toplevel()
        width = max(300, root.winfo_width() - self.sidebar_width - 40)
        height = max(200, root.winfo_height() - 40)
        self.content_container.configure(width=width, height=height)

    def rafraichir_accueil(self):
        """Force le rafraîchissement de la page d'accueil"""
        if "accueil" in self.pages:
            self.pages["accueil"].destroy()
            del self.pages["accueil"]
        self.show_page("accueil")


    # Wrappers
    def create_accueil_wrapper(self, parent):
        return create_accueil(parent, self.show_page)

    def create_modifier_wrapper(self, parent, section=None, produit=None):
        return create_page_modifier(parent, self.show_page, self.rafraichir_accueil, section, produit)


    def create_ajout_wrapper(self, parent):
        return create_page_ajout(parent, self.show_page, self.rafraichir_accueil)

    def create_stat_wrapper(self, parent):
        """Wrapper pour la page de statistiques responsive"""
        wrapper_frame = tk.Frame(parent, bg=color.get("accueil"))
        wrapper_frame.pack(fill="both", expand=True)

        # Appel à create_stat sans paramètres height/width
        create_stat(wrapper_frame)

        return wrapper_frame


    # Gestion des pages
    def show_page(self, page_name, **kwargs):
        if page_name not in self.page_creators:
            print(f"Erreur: Page '{page_name}' non trouvée!")
            return

        # Cacher la page actuelle
        if self.current_page:
            self.current_page.pack_forget()

        # Recréer la page si besoin
        if page_name not in self.pages or kwargs:
            if page_name in self.pages:
                self.pages[page_name].destroy()
                del self.pages[page_name]
            self.pages[page_name] = self.page_creators[page_name](self.content_container, **kwargs)

        # Afficher
        page = self.pages[page_name]
        page.pack(expand=True, fill="both")
        self.current_page = page


    def refresh_page(self, page_name):
        """Recrée et affiche une page existante"""
        if page_name in self.pages:
            self.pages[page_name].destroy()
            del self.pages[page_name]
        if self.current_page == self.pages.get(page_name):
            self.show_page(page_name)

    def get_current_page_name(self):
        for name, page in self.pages.items():
            if page == self.current_page:
                return name
        return None

    def get_available_size(self):
        self.update_idletasks()
        return self.content_container.winfo_width(), self.content_container.winfo_height()
