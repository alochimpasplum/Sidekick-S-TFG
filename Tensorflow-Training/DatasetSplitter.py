import os
import shutil

train_percent: float = 0.8
validation_percent: float = 1 - train_percent

datasets_folder: str = "./Datasets"
input_dataset_folder: str = datasets_folder + "/handwritten_math_symbols"
output_dataset_folder: str = datasets_folder + "/handwritten_math_symbols_ready"

if not os.path.exists(output_dataset_folder):
    os.makedirs(output_dataset_folder)

symbols: [str] = ["-", "(", ")", "+", "=", "div", "geq", "gt", "lt", "leq", "neq"]

directories = [f for f in os.scandir(input_dataset_folder) if f.name in symbols]

for d in directories:
    print("copying {}...".format(d.name))

    files: [str] = [x for x in os.listdir(d.path) if os.path.isfile(os.path.join(d, x))]

    length: int = int(len(files))
    train: int = int(length * train_percent)
    validation: int = int(length * validation_percent)

    if not os.path.exists("{}/train/{}".format(output_dataset_folder, d.name)):
        os.makedirs("{}/train/{}".format(output_dataset_folder, d.name))
    if not os.path.exists("{}/validation/{}".format(output_dataset_folder, d.name)):
        os.makedirs("{}/validation/{}".format(output_dataset_folder, d.name))

    for i, f in enumerate(files):
        original_file: str = "{}/{}".format(d.path, f)

        if i < train:
            shutil.copyfile(original_file, "{}/train/{}/{}".format(output_dataset_folder, d.name, f))
        else:
            shutil.copyfile(original_file, "{}/validation/{}/{}".format(output_dataset_folder, d.name, f))
