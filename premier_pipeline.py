import pandas as pd

# 1. CRÉATION DE DONNÉES BRUTES (simulation)
donnees_brutes = [
    {"client_id": 1, "nom": "Alice", "achat": 150.0, "ville": "Paris"},
    {"client_id": 2, "nom": "Bob", "achat": 0.0, "ville": "Lyon"},
    {"client_id": 3, "nom": "Charlie", "achat": 230.5, "ville": None},      # None = donnée manquante
    {"client_id": 4, "nom": "Diana", "achat": -50.0, "ville": "Paris"},     # Négatif = erreur
    {"client_id": 5, "nom": "Eve", "achat": 89.0, "ville": "Marseille"}
]

# 2. CRÉATION DU DATAFRAME
df = pd.DataFrame(donnees_brutes)

print("=" * 50)
print("DONNÉES BRUTES")
print("=" * 50)
print(df)

# 3. NETTOYAGE DES DONNÉES
# On garde uniquement les achats positifs ou nuls
df_clean = df[df['achat'] >= 0].copy()

# On remplit les villes manquantes par "Inconnue"
df_clean['ville'] = df_clean['ville'].fillna("Inconnue")

# 4. FEATURE ENGINEERING (Ajout colonne TVA)
df_clean['achat_ttc'] = df_clean['achat'] * 1.20

print("\n" + "=" * 50)
print("DONNÉES NETTOYÉES")
print("=" * 50)
print(df_clean)

# 5. EXPORT
df_clean.to_parquet("clients_nettoyes.parquet", index=False)
print("\nFichier sauvegardé : clients_nettoyes.parquet")