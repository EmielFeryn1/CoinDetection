import os
import shutil

import os
# Specify the root directory where your datasets are located
root_directory = 'C:\\Users\\emiel\\OneDrive\\Documenten\\CoinDetection\\datasets'

for parent_dataset in os.listdir(root_directory):
    # Iterate through each subdirectory in the root directory
    parent_dataset_path = os.path.join(root_directory, parent_dataset)
    for subdir in os.listdir(parent_dataset_path):
        subdir_path = os.path.join(parent_dataset_path, subdir)

        if os.path.isdir(subdir_path):
            last_directory_name = os.path.basename(subdir_path)
            if last_directory_name in ["train", "test", "valid"]:
                shutil.copytree(os.path.join(subdir_path, "images"), os.path.join(parent_dataset_path, "images"), dirs_exist_ok=True)
                shutil.copytree(os.path.join(subdir_path, "labels"), os.path.join(parent_dataset_path, "labels"), dirs_exist_ok=True)

                shutil.rmtree(os.path.join(subdir_path, "images"))
                shutil.rmtree(os.path.join(subdir_path, "labels"))


print("Processing complete.")
