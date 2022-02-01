import os
from sys import path
import json

input_dir = os.path.join(os.sep, "data", "inputs")
output_dir = os.path.join(os.sep, "data", "outputs")


def read_algorithm_custom_input():
    custom_path = os.path.join(os.sep, "data", "transformations", "algorithm")
    if os.path.exists(custom_path):
        with open(custom_path, "r") as file:
            return json.load(file)
    else:
        print(f"No such file: {custom_path}")


algorithm_did = os.getenv("TRANSFORMATION_DID", None)
print(f"Algorithm did {algorithm_did}")

algo_input = read_algorithm_custom_input()
print(f"Algo input: {algo_input}")

with open(os.path.join(output_dir, "result"), "w") as f:
    f.write(f"Running algo for DIDs: {os.getenv('DIDS', None)}.\n")
    f.write(f"Running algo with input parameters: [{algo_input}].\n")

print("Finishing algorithm")
