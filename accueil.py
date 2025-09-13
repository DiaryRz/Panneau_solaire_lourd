import tkinter as tk
from variable import color
from page_ajout import create_page_ajout
from data import data

# Exemple de data par section
data = data

ITEMS_PER_PAGE = 3

def create_accueil(parent, switch_page):
    page_accueil = tk.Frame(parent, bg=color.get("accueil"))

    # =================== HEADER ===================
    header_frame = tk.Frame(page_accueil, bg=color.get("accueil"))
    header_frame.pack(fill="x", padx=30, pady=(20, 10))

    # Titre principal
    tk.Label(
        header_frame,
        text="📦 Gestion des Produits",
        font=("Segoe UI", 20, "bold"),
        bg=color.get("accueil"),
        fg="white"
    ).pack(side="left")

    # Bouton Ajouter avec style moderne
    btn_ajouter = tk.Button(
        header_frame, 
        text="➕ Nouveau Produit",
        font=("Segoe UI", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        relief="flat",
        cursor="hand2",
        padx=20,
        pady=10,
        borderwidth=0,
        command=lambda: switch_page("ajout")
    )
    btn_ajouter.pack(side="right")

    # Effet hover pour le bouton ajouter
    def on_enter_add(e): btn_ajouter.configure(bg="#45a049")
    def on_leave_add(e): btn_ajouter.configure(bg="#4CAF50")
    btn_ajouter.bind("<Enter>", on_enter_add)
    btn_ajouter.bind("<Leave>", on_leave_add)

    # Séparateur
    separator = tk.Frame(page_accueil, height=2, bg="#444444")
    separator.pack(fill="x", padx=30, pady=10)

    # =================== CONTENU PRINCIPAL ===================
    # Adapter largeur du frame au canvas
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    # Canvas + Scrollbar
    canvas_frame = tk.Frame(page_accueil, bg=color.get("accueil"))
    canvas_frame.pack(fill="both", expand=True, padx=30, pady=10)

    canvas = tk.Canvas(canvas_frame, bg=color.get("accueil"), highlightthickness=0)
    scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    # Windows
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # Frame dans le canvas
    sections_frame = tk.Frame(canvas, bg=color.get("accueil"))
    frame_window = canvas.create_window((0,0), window=sections_frame, anchor="nw")

    

    def on_canvas_resize(event):
        canvas.itemconfig(frame_window, width=event.width)
    canvas.bind("<Configure>", on_canvas_resize)

    # Mettre à jour scroll
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    sections_frame.bind("<Configure>", on_frame_configure)

    current_pages = {section: 0 for section in data.keys()}

    # =================== FONCTIONS ===================
    def supprimer_item(section, ref_produit):
        data[section] = [item for item in data[section] if item["ref_produit"] != ref_produit]
        rafraichir_sections()

    def modifier_item(section, ref_produit):
        produit = next((item for item in data[section] if item["ref_produit"] == ref_produit), None)
        if produit:
            switch_page("modifier", section=section, produit=produit)


    def add_hover_effect(widget, hover_color, original_bg):
        def on_enter(event): 
            widget.configure(bg=hover_color)
        def on_leave(event): 
            widget.configure(bg=original_bg)
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def create_product_card(parent, section, item):
        card_container = tk.Frame(parent, bg=color.get("accueil"))
        card_container.pack(fill="x", pady=8, padx=5)

        card = tk.Frame(card_container, bg="#2d3748", relief="flat", borderwidth=0)
        card.pack(fill="x", padx=2, pady=2)

        content_frame = tk.Frame(card, bg="#2d3748")
        content_frame.pack(fill="x", padx=20, pady=15)

        info_frame = tk.Frame(content_frame, bg="#2d3748")
        info_frame.pack(side="left", fill="both", expand=True)

        tk.Label(
            info_frame, text=item['nom'],
            font=("Segoe UI", 14, "bold"),
            bg="#2d3748", fg="#ffffff", anchor="w"
        ).pack(anchor="w", pady=(0,5))

        tk.Label(
            info_frame, text=f"Référence: {item['ref_produit']}",
            font=("Segoe UI", 10), bg="#2d3748", fg="#a0aec0", anchor="w"
        ).pack(anchor="w", pady=(0,2))

        tk.Label(
            info_frame, text=f"Prix: {item['prix']} Ariary",
            font=("Segoe UI", 12, "bold"), bg="#2d3748", fg="#48bb78", anchor="w"
        ).pack(anchor="w", pady=(0,2))

        tk.Label(
            info_frame, text=f"{item['stock']} en stock ",
            font=("Segoe UI", 9), bg="#2d3748", fg="#718096", anchor="w"
        ).pack(anchor="w")

        actions_frame = tk.Frame(content_frame, bg="#2d3748")
        actions_frame.pack(side="right", padx=(20,0))

        btn_modifier = tk.Button(
            actions_frame, text="✏️ Modifier", font=("Segoe UI",10,"bold"),
            bg="#3182ce", fg="white", relief="flat", cursor="hand2",
            padx=15, pady=8, borderwidth=0,
            command=lambda: modifier_item(section, item["ref_produit"])
        )
        btn_modifier.pack(pady=(0,8), fill="x")
        add_hover_effect(btn_modifier, "#2c5282", "#3182ce")

        btn_supprimer = tk.Button(
            actions_frame, text="🗑️ Supprimer", font=("Segoe UI",10,"bold"),
            bg="#e53e3e", fg="white", relief="flat", cursor="hand2",
            padx=15, pady=8, borderwidth=0,
            command=lambda: supprimer_item(section, item["ref_produit"])
        )
        btn_supprimer.pack(fill="x")
        add_hover_effect(btn_supprimer, "#c53030", "#e53e3e")

    def rafraichir_sections():
        for widget in sections_frame.winfo_children():
            widget.destroy()

        total_produits = sum(len(items) for items in data.values())
        stats_frame = tk.Frame(sections_frame, bg=color.get("accueil"))
        stats_frame.pack(fill="x", pady=(0,20))

        tk.Label(
            stats_frame, text=f"📊 Total: {total_produits} produit{'s' if total_produits>1 else ''}",
            font=("Segoe UI",12,"bold"), bg=color.get("accueil"), fg="#a0aec0"
        ).pack()

        for section, items in data.items():
            if not items: continue

            section_header = tk.Frame(sections_frame, bg=color.get("accueil"))
            section_header.pack(fill="x", pady=(20,10))

            icon = "🔋" if "batterie" in section.lower() else "☀️"

            tk.Label(
                section_header, text=f"{icon} {section}",
                font=("Segoe UI",16,"bold"), bg=color.get("accueil"),
                fg="#ffd700", anchor="w"
            ).pack(side="left")

            tk.Label(
                section_header, text=f"({len(items)} produit{'s' if len(items)>1 else ''})",
                font=("Segoe UI",12), bg=color.get("accueil"), fg="#a0aec0"
            ).pack(side="right")

            products_container = tk.Frame(sections_frame, bg=color.get("accueil"))
            products_container.pack(fill="x", pady=(0,10))

            page = current_pages[section]
            start = page*ITEMS_PER_PAGE
            end = start+ITEMS_PER_PAGE
            paginated_items = items[start:end]

            for item in paginated_items:
                create_product_card(products_container, section, item)

            if len(items) > ITEMS_PER_PAGE:
                pagination_frame = tk.Frame(sections_frame, bg=color.get("accueil"))
                pagination_frame.pack(pady=10)

                if page>0:
                    btn_prev = tk.Button(
                        pagination_frame, text="⬅️ Précédent", font=("Segoe UI",10),
                        bg="#4a5568", fg="white", relief="flat", cursor="hand2",
                        padx=15, pady=5,
                        command=lambda s=section: (
                            current_pages.update({s: current_pages[s]-1}),
                            rafraichir_sections()
                        )
                    )
                    btn_prev.pack(side="left", padx=5)
                    add_hover_effect(btn_prev, "#2d3748", "#4a5568")

                tk.Label(
                    pagination_frame,
                    text=f"Page {page+1} sur {(len(items)-1)//ITEMS_PER_PAGE+1}",
                    font=("Segoe UI",10), bg=color.get("accueil"), fg="#a0aec0"
                ).pack(side="left", padx=15)

                if end<len(items):
                    btn_next = tk.Button(
                        pagination_frame, text="Suivant ➡️", font=("Segoe UI",10),
                        bg="#4a5568", fg="white", relief="flat", cursor="hand2",
                        padx=15, pady=5,
                        command=lambda s=section: (
                            current_pages.update({s: current_pages[s]+1}),
                            rafraichir_sections()
                        )
                    )
                    btn_next.pack(side="left", padx=5)
                    add_hover_effect(btn_next, "#2d3748", "#4a5568")

        if total_produits==0:
            empty_frame = tk.Frame(sections_frame, bg=color.get("accueil"))
            empty_frame.pack(expand=True, fill="both", pady=50)

            tk.Label(
                empty_frame, text="📭", font=("Segoe UI",48),
                bg=color.get("accueil"), fg="#4a5568"
            ).pack()

            tk.Label(
                empty_frame, text="Aucun produit disponible",
                font=("Segoe UI",16,"bold"), bg=color.get("accueil"), fg="#a0aec0"
            ).pack(pady=(10,5))

            tk.Label(
                empty_frame, text="Commencez par ajouter votre premier produit !",
                font=("Segoe UI",12), bg=color.get("accueil"), fg="#718096"
            ).pack()

    # Initialisation
    rafraichir_sections()
    return page_accueil
