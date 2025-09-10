import tkinter as tk
from tkinter import ttk
from variable import color
from data import data
from datetime import datetime

def create_page_ajout(parent, switch_page, rafraichir_accueil):
    page_ajout = tk.Frame(parent, bg=color.get("accueil"))

    # Titre
    tk.Label(
        page_ajout,
        text="➕ Ajouter un produit",
        font=("Arial", 16, "bold"),
        bg=color.get("accueil"),
        fg="white"
    ).pack(pady=(15, 10))

    # Sélection de la catégorie
    tk.Label(page_ajout, text="Catégorie :", bg=color.get("accueil"), fg="white").pack(pady=5)
    categorie_var = tk.StringVar()
    combo_categorie = ttk.Combobox(page_ajout, textvariable=categorie_var, state="readonly")
    combo_categorie["values"] = list(data.keys())
    combo_categorie.current(0)
    combo_categorie.pack(pady=5)

    # Nom
    tk.Label(page_ajout, text="Nom :", bg=color.get("accueil"), fg="white").pack(pady=5)
    entry_nom = tk.Entry(page_ajout, width=30)
    entry_nom.pack(pady=5)

    # Prix
    tk.Label(page_ajout, text="Prix (€) :", bg=color.get("accueil"), fg="white").pack(pady=5)
    entry_prix = tk.Entry(page_ajout, width=30)
    entry_prix.pack(pady=5)

    # Stock
    tk.Label(page_ajout, text="Stock :", bg=color.get("accueil"), fg="white").pack(pady=5)
    entry_stock = tk.Entry(page_ajout, width=30)
    entry_stock.pack(pady=5)

    # Fonction de validation
    def valider():
        nom = entry_nom.get()
        stock = entry_stock.get()
        prix = entry_prix.get()
        categorie = categorie_var.get()

        if nom and stock.isdigit() and prix.replace('.', '', 1).isdigit() and categorie:
            # Générer ref_produit unique
            all_refs = []
            for cat_items in data.values():
                for item in cat_items:
                    ref = item.get("ref_produit", "0")
                    # Extraire les chiffres à la fin
                    digits = ''.join(filter(str.isdigit, ref))
                    if digits:
                        all_refs.append(int(digits))
            max_ref_num = max(all_refs, default=0)
            new_ref = f"PS{max_ref_num + 1:03d}"  # ex: PS001, PS002...

            # Date de création automatique
            date_creation = datetime.now().strftime("%Y-%m-%d %H:%M")

            new_item = {
                "ref_produit": new_ref,
                "nom": nom,
                "prix": float(prix),
                "stock": int(stock),
                "date_creation": date_creation
            }

            # Ajouter dans la bonne catégorie
            data[categorie].append(new_item)

            # Rafraîchir l'accueil
            rafraichir_accueil()

            # Retour à l'accueil
            switch_page("accueil")


    # Bouton Valider
    tk.Button(
        page_ajout,
        text="Valider",
        font=("Arial", 12),
        bg=color.get("barre"),
        fg="white",
        relief="flat",
        padx=10, pady=5,
        command=valider
    ).pack(pady=15)

    return page_ajout
