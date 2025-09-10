# Palette de couleurs pour l'application
color = {
    # Fond général
    "accueil": "#2c3e50",   # gris-bleu sombre (background principal)
    "contenu": "#3b4b5c",   # un peu plus clair pour les zones de contenu
    "sidebar": "#34495e",
    "button_side_bar": "#34495e",

    # Texte
    "texte": "#ecf0f1",     # texte clair (blanc cassé)
    "texte_secondaire": "#bdc3c7",  # gris clair pour sous-titres

    # Accents
    "barre": "#3498db",     # bleu vif pour graphiques
    "titre": "#e74c3c",     # rouge/orangé pour attirer l'attention
    "success": "#2ecc71",   # vert (succès)
    "warning": "#f39c12",   # orange (avertissements)
    "danger": "#c0392b",    # rouge foncé (erreurs)

    # Boutons / UI
    "button_bg": "#2980b9",
    "button_hover": "#1abc9c",
    "button_text": "#ffffff",

    "content": "#3b4b5c",   # un peu plus clair pour les zones de contenu
    
    # Couleurs ajoutées pour compatibilité
    "button_side_bar_hover": "#2c3e50",  # Hover des boutons sidebar
    "primary": "#3498db",                # Bleu principal (utilise barre)
    "primary_hover": "#2980b9",          # Bleu foncé
    "success_hover": "#27ae60",          # Vert foncé
    "danger_hover": "#a93226",           # Rouge plus foncé
    "warning_hover": "#d68910",          # Orange foncé
    "info": "#3498db",                   # Bleu info (même que barre)
    
    # Couleurs de texte supplémentaires
    "text_primary": "#ecf0f1",           # Texte principal (même que texte)
    "text_secondary": "#bdc3c7",         # Texte secondaire
    "text_muted": "#95a5a6",            # Texte atténué
    "text_accent": "#f1c40f",           # Texte accent (jaune)
    
    # Couleurs de fond supplémentaires
    "card_bg": "#34495e",               # Fond des cartes (même que sidebar)
    "input_bg": "#3b4b5c",              # Fond des inputs (même que contenu)
    "border": "#4a6070",                # Bordures
    
    # États
    "hover": "#4a6070",                 # État hover général
    "active": "#2c3e50",                # État actif
    "disabled": "#7f8c8d",              # État désactivé
}

# Fonction utilitaire pour récupérer les couleurs avec fallback
def get_color(key, fallback="#ffffff"):
    """Récupère une couleur avec une valeur de fallback"""
    return color.get(key, fallback)

# Thèmes alternatifs (pour usage futur)
themes = {
    "dark": color,  # Thème actuel
    "light": {
        "accueil": "#f7fafc",
        "barre": "#edf2f7",
        "button_side_bar": "#e2e8f0",
        "text_primary": "#1a202c",
        # ... autres couleurs pour thème clair
    }
}