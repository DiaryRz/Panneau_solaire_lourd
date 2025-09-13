import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from variable import color

def create_stat(parent):
    main_container = tk.Frame(parent, bg=color.get("accueil"))
    main_container.pack(fill="both", expand=True, padx=20, pady=20)

    # Canvas + scrollbar
    canvas = tk.Canvas(main_container, bg=color.get("accueil"), highlightthickness=0)
    scrollbar = ttk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Frame scrollable
    scrollable_frame = tk.Frame(canvas, bg=color.get("accueil"))
    scrollable_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Ajuster la largeur du frame au canvas
    def on_canvas_configure(event):
        canvas.itemconfig(scrollable_window, width=event.width)
    canvas.bind("<Configure>", on_canvas_configure)

    # Scroll automatique
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    canvas.bind_all("<MouseWheel>", _on_mousewheel)

    # Section KPIs
    create_kpi_cards(scrollable_frame)

    # Graphiques principaux
    graphs_container = tk.Frame(scrollable_frame, bg=color.get("accueil"))
    graphs_container.pack(fill="x", pady=(20,0))

    left_frame = tk.Frame(graphs_container, bg=color.get("accueil"))
    left_frame.pack(side="left", fill="both", expand=True, padx=(0,10))
    create_revenue_chart(left_frame)

    right_frame = tk.Frame(graphs_container, bg=color.get("accueil"))
    right_frame.pack(side="right", fill="both", expand=True, padx=(10,0))
    create_top_products_chart(right_frame)

    # Graphiques secondaires
    secondary_container = tk.Frame(scrollable_frame, bg=color.get("accueil"))
    secondary_container.pack(fill="x", pady=(20,0))

    clients_frame = tk.Frame(secondary_container, bg=color.get("accueil"))
    clients_frame.pack(side="left", fill="both", expand=True, padx=(0,10))
    create_clients_evolution_chart(clients_frame)

    ca_frame = tk.Frame(secondary_container, bg=color.get("accueil"))
    ca_frame.pack(side="right", fill="both", expand=True, padx=(10,0))
    create_revenue_distribution_chart(ca_frame)

    return main_container



def create_kpi_cards(parent):
    """Créer les cartes KPI en haut"""
    kpi_frame = tk.Frame(parent, bg=color.get("accueil"))
    kpi_frame.pack(fill="x", pady=(0, 20))
    
    kpis = [
        {"title": "Chiffre d'affaires", "value": "Ar 80 000 000 ", "change": "+10.5%", "icon": "💰"},
        {"title": "Nombre de clients", "value": "8", "change": "+2.2%", "icon": "👥"},
        {"title": "Ventes totales", "value": "Ar 70 200 000", "change": "+11.3%", "icon": "📈"}
    ]
    
    for i, kpi in enumerate(kpis):
        create_kpi_card(kpi_frame, kpi, i)

def create_kpi_card(parent, kpi_data, index):
    """Créer une carte KPI individuelle"""
    card = tk.Frame(parent, bg=color.get("carte_bg", "#2c3e50"), relief="raised", bd=1)
    card.pack(side="left", fill="both", expand=True, padx=5, pady=5)
    
    # Icône
    icon_label = tk.Label(
        card, 
        text=kpi_data["icon"], 
        font=("Arial", 20),
        bg=color.get("carte_bg", "#2c3e50"),
        fg="white"
    )
    icon_label.pack(pady=(15, 5))
    
    # Titre
    title_label = tk.Label(
        card,
        text=kpi_data["title"],
        font=("Arial", 10),
        bg=color.get("carte_bg", "#2c3e50"),
        fg=color.get("texte_secondaire", "#bdc3c7")
    )
    title_label.pack()
    
    # Valeur
    value_label = tk.Label(
        card,
        text=kpi_data["value"],
        font=("Arial", 16, "bold"),
        bg=color.get("carte_bg", "#2c3e50"),
        fg="white"
    )
    value_label.pack(pady=(5, 2))
    
    # Changement
    change_color = "#27ae60" if "+" in kpi_data["change"] else "#e74c3c"
    change_label = tk.Label(
        card,
        text=kpi_data["change"],
        font=("Arial", 9),
        bg=color.get("carte_bg", "#2c3e50"),
        fg=change_color
    )
    change_label.pack(pady=(0, 15))

def create_revenue_chart(parent):
    """Créer le graphique de revenus par produit (barres)"""
    chart_frame = tk.Frame(parent, bg=color.get("carte_bg", "#2c3e50"), relief="raised", bd=1)
    chart_frame.pack(fill="both", expand=True, padx=5, pady=5)
    
    # Titre
    title_label = tk.Label(
        chart_frame,
        text="📊 Revenus par produit",
        font=("Arial", 12, "bold"),
        bg=color.get("carte_bg", "#2c3e50"),
        fg="white"
    )
    title_label.pack(pady=(15, 10))
    
    # Données
    produits = ["Batterie 100Ah","Batterie 50Ah","Batterie 200Ah","Panneau 250W","Panneau 50W","Panneau 300W","Panneau 400W"]
    revenus = [1500000,700000,4200000,4250000,2000000,4500000,26600000]

    
    # Graphique
    fig, ax = plt.subplots(figsize=(6, 4), facecolor=color.get("carte_bg", "#2c3e50"))
    
    bars = ax.bar(produits, revenus, color=color.get("barre", "#3498db"), 
                  edgecolor="white", linewidth=0.5, alpha=0.8)
    
    # Style
    ax.set_facecolor(color.get("carte_bg", "#2c3e50"))
    ax.tick_params(axis="x", colors="white", rotation=45)
    ax.tick_params(axis="y", colors="white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("white")
    ax.spines["bottom"].set_color("white")
    ax.grid(axis="y", linestyle="--", alpha=0.3, color="white")
    
    # Valeurs sur les barres
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 500,
                f'Ar{height:,.0f}', ha='center', va='bottom', color='white', fontsize=9)
    
    plt.tight_layout()
    
    # Intégration
    canvas_widget = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas_widget.draw()
    widget = canvas_widget.get_tk_widget()
    widget.pack(fill="both", expand=True, padx=10, pady=(0, 15))

def create_top_products_chart(parent):
    """Créer le graphique Top 3 produits"""
    chart_frame = tk.Frame(parent, bg=color.get("carte_bg", "#2c3e50"), relief="raised", bd=1)
    chart_frame.pack(fill="both", expand=True, padx=5, pady=5)
    
    # Titre
    title_label = tk.Label(
        chart_frame,
        text="🏆 Top 3 produits",
        font=("Arial", 12, "bold"),
        bg=color.get("carte_bg", "#2c3e50"),
        fg="white"
    )
    title_label.pack(pady=(15, 10))
    
    # Données
    produits = ["Batterie 100Ah" , "Premium 400W" , "Batterie Gel 200Ah"]
    ventes = [3, 4, 4]
    colors = ["#e74c3c", "#f39c12", "#f1c40f"]
    
    # Graphique horizontal
    fig, ax = plt.subplots(figsize=(6, 4), facecolor=color.get("carte_bg", "#2c3e50"))
    
    bars = ax.barh(produits, ventes, color=colors, alpha=0.8, edgecolor="white", linewidth=0.5)
    
    # Style
    ax.set_facecolor(color.get("carte_bg", "#2c3e50"))
    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white", labelsize=9)  # taille police ajustée
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("white")
    ax.spines["bottom"].set_color("white")
    ax.grid(axis="x", linestyle="--", alpha=0.3, color="white")
    
    # Valeurs sur les barres
    for i, (bar, value) in enumerate(zip(bars, ventes)):
        ax.text(value + 0.1, bar.get_y() + bar.get_height()/2,
                f'{value}', ha='left', va='center', color='white', fontsize=9)
    
    # Ajuster marges pour bien voir les labels
    plt.tight_layout()
    fig.subplots_adjust(left=0.35)  # espace à gauche augmenté
    
    # Intégration
    canvas_widget = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas_widget.draw()
    widget = canvas_widget.get_tk_widget()
    widget.pack(fill="both", expand=True, padx=10, pady=(0, 15))


def create_clients_evolution_chart(parent):
    """Créer le graphique d'évolution des clients"""
    chart_frame = tk.Frame(parent, bg=color.get("carte_bg", "#2c3e50"), relief="raised", bd=1)
    chart_frame.pack(fill="both", expand=True, padx=5, pady=5)
    
    # Titre
    title_label = tk.Label(
        chart_frame,
        text="📈 Souscriptions clients",
        font=("Arial", 12, "bold"),
        bg=color.get("carte_bg", "#2c3e50"),
        fg="white"
    )
    title_label.pack(pady=(15, 10))
    
    # Données
    mois = ["Jan", "Fév", "Mar", "Avr", "Mai", "Jun", "Juil", "Août"]
    clients = [0, 1, 1, 1, 2, 1, 1, 1]

    
    # Graphique avec taille compacte
    fig, ax = plt.subplots(figsize=(4.5, 2.5), facecolor=color.get("carte_bg", "#2c3e50"))
    
    ax.plot(mois, clients, color="#27ae60", linewidth=3, marker="o", 
            markersize=8, markerfacecolor="white", markeredgecolor="#27ae60", markeredgewidth=2)
    ax.fill_between(mois, clients, alpha=0.3, color="#27ae60")
    
    # Style
    ax.set_facecolor(color.get("carte_bg", "#2c3e50"))
    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("white")
    ax.spines["bottom"].set_color("white")
    ax.grid(True, linestyle="--", alpha=0.3, color="white")
    
    plt.tight_layout()
    
    # Intégration
    canvas_widget = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas_widget.draw()
    widget = canvas_widget.get_tk_widget()
    widget.pack(fill="both", expand=True, padx=10, pady=(0, 15))

def create_revenue_distribution_chart(parent):
    """Créer une liste colorée scrollable de consommation électrique (en Watt)"""
    chart_frame = tk.Frame(parent, bg=color.get("carte_bg", "#2c3e50"), relief="raised", bd=1)
    chart_frame.pack(fill="both", expand=True, padx=5, pady=5)

    # Titre
    title_label = tk.Label(
        chart_frame,
        text="⚡ Consommation Clients (W)",
        font=("Arial", 12, "bold"),
        bg=color.get("carte_bg", "#2c3e50"),
        fg="white"
    )
    title_label.pack(pady=(15, 10))

    # Données fictives (nom client + consommation en Watt)
    clients = [
        ("Client A", 1200, "#e74c3c"),
        ("Client B", 950, "#f39c12"),
        ("Client C", 780, "#3498db"),
        ("Client D", 500, "#9b59b6"),
        ("Client E", 300, "#1abc9c"),
        ("Client F", 220, "#d35400"),
        ("Client G", 180, "#8e44ad"),
        ("Client H", 150, "#2ecc71"),
    ]

    # Canvas + scrollbar
    canvas = tk.Canvas(chart_frame, bg=color.get("carte_bg", "#2c3e50"), highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = tk.Scrollbar(chart_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Frame interne scrollable
    scrollable_frame = tk.Frame(canvas, bg=color.get("carte_bg", "#2c3e50"))
    window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Adapter la largeur du frame à celle du canvas
    def resize_scrollable(event):
        canvas.itemconfig(window_id, width=event.width)
    canvas.bind("<Configure>", resize_scrollable)

    # Mettre à jour la zone scrollable
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Ajouter chaque client comme une ligne
    for nom, watt, couleur in clients:
        item_frame = tk.Frame(scrollable_frame, bg=couleur, padx=10, pady=8)
        item_frame.pack(fill="x", pady=4)

        tk.Label(
            item_frame,
            text=nom,
            font=("Arial", 10, "bold"),
            fg="white",
            bg=couleur
        ).pack(side="left")

        tk.Label(
            item_frame,
            text=f"{watt} W",
            font=("Arial", 10),
            fg="white",
            bg=couleur
        ).pack(side="right")
