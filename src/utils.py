# Fassinou Bile Master 2 DIT avril 23

import pandas as pd

class DataProcessor:
    def __init__(self, data_file):
        self.data = pd.read_csv(data_file)
    
    def clean_data(self):
        pass
        # Supprimez les lignes contenant des valeurs manquantes
        #self.data.dropna(inplace=True)

    def reduce_data(self, selected_columns):
        # Sélectionnez uniquement les colonnes spécifiées
        self.data = self.data[selected_columns]

    def feature_engineering(self, new_feature_name, col1, col2):
        # Créez une nouvelle colonne en effectuant une opération de feature engineering
        self.data[new_feature_name] = self.data[col1] + self.data[col2]

    def summarize_stats(self, output_file):
        # Calculez des statistiques sommaires et enregistrez-les dans un fichier
        summary_stats = self.data.describe()
        summary_stats.to_csv(output_file, index=False)
