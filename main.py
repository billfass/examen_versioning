# Fassinou Bile Master 2 DIT avril 23

from src.utils import DataProcessor

# url du fichier
data_file = 'data/raw/owid-covid-data.csv'

# Créez une instance de DataProcessor en passant le chemin vers votre fichier de données
data_processor = DataProcessor(data_file)

# Appelez les méthodes pour effectuer les tâches
data_processor.clean_data()
data_processor.reduce_data(['iso_code', 'total_cases', 'new_cases'])
data_processor.feature_engineering('total_cases_now', 'total_cases', 'new_cases')
data_processor.summarize_stats('statistiques_sommaires.csv')
