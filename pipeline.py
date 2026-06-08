# Ligne 1-2 : On importe les bibliothèques standards pour manipuler les données et le temps.
import pandas as pd
import datetime

def clean_msat_data(input_file, output_file):
    """
    Fonction principale pour nettoyer les données de production des bioréacteurs
    tout en respectant les principes de Data Integrity (ALCOA+).
    """
    
    # 1. CHARGEMENT DES DONNÉES (INGESTION)
    # On lit le fichier CSV "sale" et on le charge dans un tableau virtuel (DataFrame) appelé 'df'.
    df = pd.read_csv(input_file)
    
    # On enregistre le nombre initial de lignes pour notre rapport d'audit (traçabilité QA).
    initial_rows = len(df)
    
    
    # 2. NETTOYAGE DES DONNÉES & TRAITEMENT DES ANOMALIES
    
    # Règle 1 : Remplir l'identifiant du lot (Batch_ID) s'il y a un blanc, 
    # en copiant la valeur de la ligne précédente (méthode 'ffill' pour Forward Fill).
    df['Batch_ID'] = df['Batch_ID'].ffill()
    
    # Règle 2 : Supprimer les valeurs aberrantes (Ex: Viabilité > 100M/mL impossible physiquement).
    # On ne garde que les lignes où la densité cellulaire est inférieure à 100.
    df = df[df['Viable_Cell_Density_M_mL'] < 100]
    
    # Règle 3 : Remplir les données manquantes du capteur d'oxygène (DO_Percent).
    # On utilise la moyenne de la colonne pour ne pas fausser les calculs globaux.
    mean_do = df['DO_Percent'].mean()
    df['DO_Percent'] = df['DO_Percent'].fillna(mean_do)
    
    
    # 3. CRÉATION DU LOG D'AUDIT TRAIL (CONFORMITÉ QA)
    # On calcule combien de lignes problématiques ont été supprimées ou modifiées.
    rows_removed = initial_rows - len(df)
    # On récupère l'heure exacte de l'exécution du script.
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # On affiche le log dans la console (preuve de traçabilité ALCOA+).
    print(f"--- GxP DATA INTEGRITY LOG [{current_time}] ---")
    print(f"Fichier analysé : {input_file}")
    print(f"Lignes d'anomalies critiques supprimées : {rows_removed}")
    
    
    # 4. EXPORTATION DES DONNÉES PROPRES
    # On sauvegarde le tableau nettoyé dans un nouveau fichier CSV.
    # 'index=False' évite de créer une colonne de numéros de lignes inutile.
    df.to_csv(output_file, index=False)
    print(f"Fichier nettoyé exporté avec succès : {output_file}\n")

# LIGNE D'EXÉCUTION
# On appelle la fonction avec nos deux fichiers (le brut et le propre).
clean_msat_data('data_example_raw.csv', 'data_example_clean.csv')
