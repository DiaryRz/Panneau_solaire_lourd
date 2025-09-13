import tkinter as tk
from tkinter import ttk
from variable import color
from data import data
from datetime import datetime

def create_page_ajout(parent, switch_page, rafraichir_accueil):
    page_ajout = tk.Frame(parent, bg=color.get("accueil"))
    page_ajout.pack(fill="both", expand=True)

    # Canvas + scrollbar
    canvas = tk.Canvas(page_ajout, bg=color.get("accueil"), highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = tk.Scrollbar(page_ajout, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame interne scrollable
    scrollable_frame = tk.Frame(canvas, bg=color.get("accueil"))
    window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Adapter la largeur du scrollable_frame à celle du canvas
    def resize_scrollable(event):
        canvas.itemconfig(window_id, width=event.width)
    canvas.bind("<Configure>", resize_scrollable)

    # Mettre à jour la zone scrollable
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # ====== Scroll avec la molette ======
    def _on_mousewheel(event):
        # Windows et Mac
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def _on_mousewheel_linux(event):
        # Linux
        if event.num == 4:
            canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            canvas.yview_scroll(1, "units")

    # Bind pour toutes les plateformes
    canvas.bind_all("<MouseWheel>", _on_mousewheel)  # Windows / Mac
    canvas.bind_all("<Button-4>", _on_mousewheel_linux)  # Linux scroll up
    canvas.bind_all("<Button-5>", _on_mousewheel_linux)  # Linux scroll down

    # ====== Titre principal ======
    tk.Label(
        scrollable_frame,
        text="➕ Ajouter un produit",
        font=("Segoe UI", 22, "bold"),
        bg=color.get("accueil"),
        fg="white"
    ).pack(pady=(25, 20))

    # ====== Card formulaire ======
    card_frame = tk.Frame(scrollable_frame, bg="#1f2937", bd=0, relief="flat")
    card_frame.pack(padx=50, pady=10, fill="x")

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

    # Champs principaux
    combo_categorie = create_field(card_frame_inner, "Catégorie :", widget_type="combo", values=list(data.keys()))
    entry_nom = create_field(card_frame_inner, "Nom :")
    entry_prix = create_field(card_frame_inner, "Prix (Ariary) :")
    entry_stock = create_field(card_frame_inner, "Stock :")

    # Champs supplémentaires
    entry_couleur = create_field(card_frame_inner, "Couleur :")
    entry_puissance = create_field(card_frame_inner, "Puissance (W) :")
    entry_longueur = create_field(card_frame_inner, "Longueur (cm) :")

    # ====== Bouton Valider ======
    btn_frame = tk.Frame(scrollable_frame, bg=color.get("accueil"))
    btn_frame.pack(pady=20)

    def on_enter(e): btn_valider.configure(bg="#3aa44a")
    def on_leave(e): btn_valider.configure(bg="#4CAF50")

    def valider():
        nom = entry_nom.get()
        stock = entry_stock.get()
        prix = entry_prix.get()
        categorie = combo_categorie.get()
        couleur = entry_couleur.get()
        puissance = entry_puissance.get()
        longueur = entry_longueur.get()

        if nom and stock.isdigit() and prix.replace('.', '', 1).isdigit() and categorie:
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
                "date_creation": date_creation,
                "couleur": couleur,
                "puissance": float(puissance) if puissance.replace('.', '', 1).isdigit() else 0,
                "longueur": float(longueur) if longueur.replace('.', '', 1).isdigit() else 0
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
