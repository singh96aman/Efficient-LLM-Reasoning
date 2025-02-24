import os
import json
from datasets import load_dataset


def read_benchmark(dataset_name):
    """Read benchmark dataset from Hugging Face."""
    try:
        dataset = load_dataset(dataset_name)
        print(f"Loaded dataset: {dataset_name}")
        return dataset
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


def print_all_questions(dataset, question_key="question"):
    """Print all the questions in the dataset."""
    if dataset is None:
        print("Dataset not loaded.")
        return

    print("\n--- Questions in Dataset ---\n")
    for idx, sample in enumerate(dataset):
        question = sample.get(question_key, "No question found")
        print(f"{idx + 1}. {question}")



def read_experimental_config(config_name, config_folder="configs"):
    """Read experimental config from the configs/ folder."""
    script_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(script_dir)  # Go up one level to reach src

    # Construct the path relative to src
    config_path = os.path.join(parent_dir, config_folder, config_name)

    if not os.path.exists(config_path):
        print(f"Config file {config_path} not found.")
        return None

    try:
        with open(config_path, 'r') as file:
            config = json.load(file)
        print(f"Loaded config: {config_name}")
        return config
    except json.JSONDecodeError as e:
        print(f"Error reading config file: {e}")
        return None
