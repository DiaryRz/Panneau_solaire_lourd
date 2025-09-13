import tkinter as tk
from tkinter import ttk
from variable import color
from PIL import Image, ImageTk  # Pillow pour gérer les images

def create_page_profil(parent, switch_page, rafraichir_accueil):
    page_profil = tk.Frame(parent, bg=color.get("accueil"))

    # ====== HEADER ======
    header = tk.Frame(page_profil, bg=color.get("accueil"))
    header.pack(fill="x", pady=20)

    tk.Label(
        header,
        text="👤 Mon Profil",
        font=("Segoe UI", 20, "bold"),
        bg=color.get("accueil"),
        fg="white"
    ).pack(side="left", padx=30)

    # ====== CONTENU ======
    content = tk.Frame(page_profil, bg=color.get("accueil"))
    content.pack(expand=True)

    # --- Avatar rond ---
    try:
        # Charge une vraie image si disponible
        img = Image.open("assets/admin.png")  # chemin vers ton image
        img = img.resize((120, 120), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
    except:
        # Placeholder si pas d'image
        photo = None

    avatar_frame = tk.Frame(content, bg=color.get("accueil"))
    avatar_frame.pack(pady=20)

    if photo:
        avatar_label = tk.Label(avatar_frame, image=photo, bg=color.get("accueil"))
        avatar_label.image = photo  # éviter le garbage collector
        avatar_label.pack()
    else:
        # Cercle avec initiales si pas de photo
        canvas = tk.Canvas(avatar_frame, width=120, height=120, bg=color.get("accueil"), highlightthickness=0)
        canvas.create_oval(10, 10, 110, 110, fill="#4a5568", outline="")
        canvas.create_text(60, 60, text="AD", font=("Segoe UI", 28, "bold"), fill="white")
        canvas.pack()

    # --- Nom de l’admin ---
    tk.Label(
        content,
        text="Admin Principal",
        font=("Segoe UI", 18, "bold"),
        bg=color.get("accueil"),
        fg="#ffd700"
    ).pack(pady=(10, 5))

    # --- Infos supplémentaires ---
    info_frame = tk.Frame(content, bg="#2d3748", padx=30, pady=20)
    info_frame.pack(pady=20, ipadx=10, ipady=10)

    infos = {
        "Nom complet": "Jean Dupont",
        "Email": "admin@example.com",
        "Rôle": "Super Administrateur",
        "Depuis": "Janvier 2023"
    }

    for i, (label, value) in enumerate(infos.items()):
        tk.Label(info_frame, text=label + " :", font=("Segoe UI", 11, "bold"), 
                 bg="#2d3748", fg="#a0aec0", anchor="w").grid(row=i, column=0, sticky="w", pady=5, padx=10)
        tk.Label(info_frame, text=value, font=("Segoe UI", 11), 
                 bg="#2d3748", fg="white", anchor="w").grid(row=i, column=1, sticky="w", pady=5, padx=10)

    return page_profil
