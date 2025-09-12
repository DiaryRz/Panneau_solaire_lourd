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

    # Nom
    tk.Label(form_frame, text="Nom :", font=("Segoe UI", 12), bg=color.get("accueil"), fg="white").grid(row=0, column=0, sticky="w", pady=5, padx=10)
    entry_nom = tk.Entry(form_frame, font=("Segoe UI", 12))
    entry_nom.grid(row=0, column=1, pady=5, padx=10)
    entry_nom.insert(0, produit["nom"])

    # Référence (non modifiable)
    tk.Label(form_frame, text="Référence :", font=("Segoe UI", 12), bg=color.get("accueil"), fg="white").grid(row=1, column=0, sticky="w", pady=5, padx=10)
    entry_ref = tk.Entry(form_frame, font=("Segoe UI", 12), state="readonly")
    entry_ref.grid(row=1, column=1, pady=5, padx=10)
    entry_ref.insert(0, produit["ref_produit"])

    # Prix
    tk.Label(form_frame, text="Prix (€):", font=("Segoe UI", 12), bg=color.get("accueil"), fg="white").grid(row=2, column=0, sticky="w", pady=5, padx=10)
    entry_prix = tk.Entry(form_frame, font=("Segoe UI", 12))
    entry_prix.grid(row=2, column=1, pady=5, padx=10)
    entry_prix.insert(0, produit["prix"])

    # Date création (non modifiable)
    tk.Label(form_frame, text="Date de création :", font=("Segoe UI", 12), bg=color.get("accueil"), fg="white").grid(row=3, column=0, sticky="w", pady=5, padx=10)
    entry_date = tk.Entry(form_frame, font=("Segoe UI", 12), state="readonly")
    entry_date.grid(row=3, column=1, pady=5, padx=10)
    entry_date.insert(0, produit["date_creation"])

    # Boutons
    btn_frame = tk.Frame(page_modifier, bg=color.get("accueil"))
    btn_frame.pack(pady=30)

    def enregistrer_modification():
        produit["nom"] = entry_nom.get()
        produit["prix"] = entry_prix.get()
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
