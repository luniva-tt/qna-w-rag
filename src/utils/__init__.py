def load_yaml(file_path):
    import yaml
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def save_results(results, file_path):
    import json
    with open(file_path, 'w') as file:
        json.dump(results, file, indent=4)