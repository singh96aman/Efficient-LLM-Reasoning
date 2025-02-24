import argparse
from utils.preprocessing import read_experimental_config, read_benchmark, print_all_questions

def preprocessing(config):
    print("Executing preprocessing step...")
    datasets = config.get("dataset", [])
    if not datasets or len(datasets) == 0 or datasets == [''] or datasets == [""]:
        print("No datasets specified in the config.")
        return

    for dataset_name in datasets:
        dataset = read_benchmark(dataset_name)
        if dataset:
            print_all_questions(dataset)


def run():
    print("Executing run step...")


def main():
    parser = argparse.ArgumentParser(description="Run experiment based on config.")
    parser.add_argument("--configid", type=str, help="ID of the experiment configuration file")
    args = parser.parse_args()

    # Load experimental configuration
    config = read_experimental_config(f"{args.configid}.json")
    if config is None:
        raise Exception(f"Error loading experimental configuration. - {args.configid}")

    # Execute steps from config
    execution_steps = config.get("executionsteps", "").split(",")
    for step in execution_steps:
        step = step.strip()
        if step == "preprocessing":
            preprocessing(config)
        elif step == "run":
            run()
        else:
            raise Exception(f"Unknown execution step: {step}")


if __name__ == "__main__":
    main()