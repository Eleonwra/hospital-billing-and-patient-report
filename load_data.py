import kagglehub
import os
import shutil

cache_path = kagglehub.dataset_download("prasad22/healthcare-dataset")
destination_folder = "data"
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(cache_path):
    if filename.endswith(".csv"):
        source_file = os.path.join(cache_path, filename)
        destination_file = os.path.join(destination_folder, 'raw_data.csv')
        shutil.copy(source_file, destination_file)