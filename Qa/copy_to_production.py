import os
import shutil

def copy_to_production():
    qa_file_path = os.path.join('Qa', 'appSettings.json')
    production_folder = 'production'
    production_file_path = os.path.join(production_folder, 'appSettings.json')

    # Step 1: Check if the Qa file exists
    if not os.path.exists(qa_file_path):
        raise FileNotFoundError("Error: 'appSettings.json' not found in the 'Qa' folder.")

    # Step 2: Create production folder if it doesn't exist
    if not os.path.exists(production_folder):
        os.makedirs(production_folder)

    # Step 3: Copy file from Qa to production
    shutil.copy(qa_file_path, production_file_path)
    print(f"File successfully copied from {qa_file_path} to {production_file_path}")

# Run the function
copy_to_production()
