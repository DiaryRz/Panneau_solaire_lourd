# app.py
import tkinter as tk
from ui_components import MainContent
from sidebar import Sidebar

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Panneau solaire")
        self.geometry("800x600")
        self.minsize(600, 400)

        # Ajouter la sidebar et le contenu principal
        self.main_content = MainContent(self)
        self.sidebar = Sidebar(self, self.main_content)

if __name__ == "__main__":
    app = App()
    app.mainloop()
