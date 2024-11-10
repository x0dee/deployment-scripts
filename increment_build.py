import os
import json
import sys

def increment_build_in_qa(base_path):
    # Define paths
    qa_folder = os.path.join(base_path, "HardCoded")  
    json_file_path = os.path.join(qa_folder, "appSettings.json")

    # Step 1: Create Qa folder if it does not exist
    if not os.path.exists(qa_folder):
        os.makedirs(qa_folder)

    # Step 2: Check if JSON file exists and load data if it does
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
    else:
        # Initialize an empty dictionary if file doesn't exist
        data = {}

    # Step 3: Update or insert deploymentVersion
    if 'deploymentVersion' in data:
        data['deploymentVersion'] += 1  # Increment existing version
    else:
        data['deploymentVersion'] = 1   # Insert initial version

    # Step 4: Save the updated data back to the JSON file
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

    print(f"{json_file_path} updated with deploymentVersion: {data['deploymentVersion']}")

# Run the function

# Arguments passed
path = sys.argv[1]
increment_build_in_qa(base_path=path)