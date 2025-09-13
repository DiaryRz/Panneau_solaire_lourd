import tkinter as tk
from variable import color
from datetime import datetime
from data import data

def create_page_modifier(parent, switch_page, rafraichir_accueil, section, produit):
    page_modifier = tk.Frame(parent, bg=color.get("accueil"))

    # ===== Titre =====
    tk.Label(
        page_modifier,
        text="✏️ Modifier le Produit",
        font=("Segoe UI", 20, "bold"),
        bg=color.get("accueil"),
        fg="white"
    ).pack(pady=20)

    form_frame = tk.Frame(page_modifier, bg=color.get("accueil"))
    form_frame.pack(pady=20)

    def create_field(label_text, value="", row=0):
        tk.Label(form_frame, text=label_text, font=("Segoe UI", 12), bg=color.get("accueil"), fg="white")\
            .grid(row=row, column=0, sticky="w", pady=5, padx=10)
        entry = tk.Entry(form_frame, font=("Segoe UI", 12))
        entry.grid(row=row, column=1, pady=5, padx=10)
        entry.insert(0, value)
        return entry

    # Champs
    entry_nom = create_field("Nom :", produit.get("nom", ""), 0)
    entry_ref = create_field("Référence :", produit.get("ref_produit", ""), 1)
    entry_ref.configure(state="readonly")
    entry_prix = create_field("Prix (Ariary):", produit.get("prix", ""), 2)
    entry_date = create_field("Date de création :", produit.get("date_creation", ""), 3)
    entry_date.configure(state="readonly")

    # Nouveaux champs
    entry_couleur = create_field("Couleur :", produit.get("couleur", ""), 4)
    entry_puissance = create_field("Puissance :", produit.get("puissance", ""), 5)
    entry_longueur = create_field("Longueur :", produit.get("longueur", ""), 6)

    # Boutons
    btn_frame = tk.Frame(page_modifier, bg=color.get("accueil"))
    btn_frame.pack(pady=30)

    def enregistrer_modification():
        produit["nom"] = entry_nom.get()
        produit["prix"] = entry_prix.get()
        produit["couleur"] = entry_couleur.get()
        produit["puissance"] = entry_puissance.get()
        produit["longueur"] = entry_longueur.get()
        # retour accueil
        rafraichir_accueil()
        switch_page("accueil")

    tk.Button(
        btn_frame, text="💾 Enregistrer", font=("Segoe UI", 12, "bold"),
        bg="#3182ce", fg="white", relief="flat", padx=20, pady=10,
        cursor="hand2", command=enregistrer_modification
    ).pack(side="left", padx=10)

    tk.Button(
        btn_frame, text="❌ Annuler", font=("Segoe UI", 12, "bold"),
        bg="#e53e3e", fg="white", relief="flat", padx=20, pady=10,
        cursor="hand2", command=lambda: switch_page("accueil")
    ).pack(side="left", padx=10)

    return page_modifier
