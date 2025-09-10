# Nouvelle structure de données
data = {
    "Panneau solaire": [
        {"nom": "PM", "ref_produit": "PS001", "prix": 1500, "date_creation": "2025-09-10"},
        {"nom": "GM", "ref_produit": "PS002", "prix": 1800, "date_creation": "2025-09-11"}
    ],
    "Batterie": [
        {"nom": "Standard", "ref_produit": "BAT001", "prix": 800, "date_creation": "2025-09-09"}
    ]
}

# Fonction pour générer une référence produit automatique
def generer_ref_produit(categorie):
    """Génère une référence produit unique basée sur la catégorie"""
    prefixes = {
        "Panneau solaire": "PS",
        "Batterie": "BAT",
        "Onduleur": "OND",
        "Câble": "CAB",
        "Accessoire": "ACC"
    }
    
    prefix = prefixes.get(categorie, "PRD")
    
    # Compter les éléments existants dans la catégorie
    count = len(data.get(categorie, [])) + 1
    
    return f"{prefix}{count:03d}"