import json

def load_matches(file_path):
    """
    Load matches from a JSON file.

    parameters: file_path: Path to the JSON file
    return: List of matches or an empty list if an error occurs
    """
    try:
        with open(file_path, 'r') as file:
            matches = json.load(file)
        return matches
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}.")
        return []

def save_matches(file_path, matches): # No need to retun as we are saving JSON file
    try:
        with open(file_path, 'w') as file:
            json.dump(matches, file, indent=4)
        print(f"Matches successfully saved to {file_path}.")
    except PermissionError:
        print(f"Error: Permission denied to write.")
    except Exception as e:
        print("An unexpected error occurred: e.")