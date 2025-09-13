import tkinter as tk
from tkinter import ttk
from variable import color
from data import data
from datetime import datetime

def create_page_ajout(parent, switch_page, rafraichir_accueil):
    page_ajout = tk.Frame(parent, bg=color.get("accueil"))

    # ====== Titre principal ======
    tk.Label(
        page_ajout,
        text="➕ Ajouter un produit",
        font=("Segoe UI", 22, "bold"),
        bg=color.get("accueil"),
        fg="white"
    ).pack(pady=(25, 20))

    # ====== Card formulaire ======
    card_frame = tk.Frame(page_ajout, bg="#1f2937", bd=0, relief="flat")
    card_frame.pack(padx=50, pady=10, fill="x")

    # Padding interne
    card_frame_inner = tk.Frame(card_frame, bg="#1f2937")
    card_frame_inner.pack(padx=20, pady=20, fill="x")

    # Fonction pour créer champs avec style
    def create_field(parent, label_text, widget_type="entry", values=None):
        field_frame = tk.Frame(parent, bg="#1f2937")
        field_frame.pack(fill="x", pady=10)

        tk.Label(field_frame, text=label_text, font=("Segoe UI", 11, "bold"), bg="#1f2937", fg="#cbd5e1").pack(anchor="w", padx=5, pady=2)

        if widget_type == "entry":
            entry = tk.Entry(field_frame, font=("Segoe UI", 11), bg="#374151", fg="white", insertbackground="white", relief="flat")
            entry.pack(fill="x", padx=5, pady=2)
            return entry
        elif widget_type == "combo":
            combo = ttk.Combobox(field_frame, values=values, state="readonly", font=("Segoe UI", 11))
            combo.current(0)
            combo.pack(fill="x", padx=5, pady=2)
            return combo

    # Champs
    combo_categorie = create_field(card_frame_inner, "Catégorie :", widget_type="combo", values=list(data.keys()))
    entry_nom = create_field(card_frame_inner, "Nom :")
    entry_prix = create_field(card_frame_inner, "Prix (Ariary) :")
    entry_stock = create_field(card_frame_inner, "Stock :")

    # ====== Bouton Valider ======
    btn_frame = tk.Frame(page_ajout, bg=color.get("accueil"))
    btn_frame.pack(pady=20)

    def on_enter(e): btn_valider.configure(bg="#3aa44a")
    def on_leave(e): btn_valider.configure(bg="#4CAF50")

    def valider():
        nom = entry_nom.get()
        stock = entry_stock.get()
        prix = entry_prix.get()
        categorie = combo_categorie.get()

        if nom and stock.isdigit() and prix.replace('.', '', 1).isdigit() and categorie:
            # Générer ref_produit unique
            all_refs = []
            for cat_items in data.values():
                for item in cat_items:
                    ref = item.get("ref_produit", "0")
                    digits = ''.join(filter(str.isdigit, ref))
                    if digits:
                        all_refs.append(int(digits))
            max_ref_num = max(all_refs, default=0)
            new_ref = f"PS{max_ref_num + 1:03d}"

            date_creation = datetime.now().strftime("%Y-%m-%d %H:%M")

            new_item = {
                "ref_produit": new_ref,
                "nom": nom,
                "prix": float(prix),
                "stock": int(stock),
                "date_creation": date_creation
            }

            data[categorie].append(new_item)
            rafraichir_accueil()
            switch_page("accueil")

    btn_valider = tk.Button(
        btn_frame,
        text="Valider",
        font=("Segoe UI", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        relief="flat",
        padx=25, pady=10,
        cursor="hand2",
        command=valider
    )
    btn_valider.pack()
    btn_valider.bind("<Enter>", on_enter)
    btn_valider.bind("<Leave>", on_leave)

    return page_ajout
