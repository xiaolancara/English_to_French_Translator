import os


def load_data(path):
    """
    Load dataset
    """
    input_file = os.path.join(path)
    with open(input_file, "r", encoding="utf8") as f:
            lines = f.read()

    return lines.split('\n')
