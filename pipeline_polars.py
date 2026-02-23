import polars as pl

# 1. CRÉATION DES DONNÉES
donnees_brutes = [
    {"client_id": 1, "nom": "Alice", "achat": 150.0, "ville": "Paris"},
    {"client_id": 2, "nom": "Bob", "achat": 0.0, "ville": "Lyon"},
    {"client_id": 3, "nom": "Charlie", "achat": 230.5, "ville": None},
    {"client_id": 4, "nom": "Diana", "achat": -50.0, "ville": "Paris"},
    {"client_id": 5, "nom": "Eve", "achat": 89.0, "ville": "Marseille"}
]

# Conversion en DataFrame Polars [cite: 184, 186]
df = pl.DataFrame(donnees_brutes)

# 2. LE PIPELINE (Syntaxe enchaînée) [cite: 187]
df_clean = (
    df
    .filter(pl.col("achat") >= 0)
    .with_columns(pl.col("ville").fill_null("Inconnue"))
    .with_columns((pl.col("achat") * 1.20).alias("achat_ttc"))
)

# 3. AFFICHAGE ET EXPORT
print("Résultat avec Polars :")
print(df_clean)
df_clean.write_parquet("clients_nettoyes_polars.parquet")
print("\nExport Polars réussi !")