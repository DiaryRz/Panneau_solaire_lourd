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
        {"title": "Chiffre d'affaires", "value": "€45,678", "change": "+12.5%", "icon": "💰"},
        {"title": "Nombre de clients", "value": "1,234", "change": "+8.2%", "icon": "👥"},
        {"title": "Ventes totales", "value": "€78,901", "change": "+15.3%", "icon": "📈"}
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
    produits = ["Produit A", "Produit B", "Produit C", "Produit D", "Produit E"]
    revenus = [25000, 18000, 32000, 15000, 22000]
    
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
                f'€{height:,.0f}', ha='center', va='bottom', color='white', fontsize=9)
    
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
    produits = ["Produit A", "Produit B", "Produit C"]
    ventes = [450, 380, 320]
    colors = ["#e74c3c", "#f39c12", "#f1c40f"]
    
    # Graphique horizontal
    fig, ax = plt.subplots(figsize=(6, 4), facecolor=color.get("carte_bg", "#2c3e50"))
    
    bars = ax.barh(produits, ventes, color=colors, alpha=0.8, edgecolor="white", linewidth=0.5)
    
    # Style
    ax.set_facecolor(color.get("carte_bg", "#2c3e50"))
    ax.tick_params(axis="x", colors="white")
    ax.tick_params(axis="y", colors="white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("white")
    ax.spines["bottom"].set_color("white")
    ax.grid(axis="x", linestyle="--", alpha=0.3, color="white")
    
    # Valeurs sur les barres
    for i, (bar, value) in enumerate(zip(bars, ventes)):
        ax.text(value + 10, bar.get_y() + bar.get_height()/2,
                f'{value}', ha='left', va='center', color='white', fontsize=9)
    
    plt.tight_layout()
    
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
    mois = ["Jan", "Fév", "Mar", "Avr", "Mai", "Jun"]
    clients = [100, 120, 140, 135, 160, 180]
    
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
    """Créer le graphique de répartition CA/client"""
    chart_frame = tk.Frame(parent, bg=color.get("carte_bg", "#2c3e50"), relief="raised", bd=1)
    chart_frame.pack(fill="both", expand=True, padx=5, pady=5)
    
    # Titre
    title_label = tk.Label(
        chart_frame,
        text="🥧 Répartition CA/Client",
        font=("Arial", 12, "bold"),
        bg=color.get("carte_bg", "#2c3e50"),
        fg="white"
    )
    title_label.pack(pady=(15, 10))
    
    # Données
    segments = ["Gros clients", "Clients moyens", "Petits clients", "Nouveaux"]
    pourcentages = [45, 25, 20, 10]
    colors = ["#e74c3c", "#f39c12", "#3498db", "#9b59b6"]
    
    # Graphique
    fig, ax = plt.subplots(figsize=(6, 3), facecolor=color.get("carte_bg", "#2c3e50"))
    
    wedges, texts, autotexts = ax.pie(pourcentages, labels=segments, colors=colors, 
                                     autopct='%1.1f%%', startangle=90, 
                                     textprops={'color': 'white', 'fontsize': 9})
    
    # Style
    ax.set_facecolor(color.get("carte_bg", "#2c3e50"))
    
    plt.tight_layout()
    
    # Intégration
    canvas_widget = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas_widget.draw()
    widget = canvas_widget.get_tk_widget()
    widget.pack(fill="both", expand=True, padx=10, pady=(0, 15))