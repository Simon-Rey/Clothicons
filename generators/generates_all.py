from pathlib import Path

import os

from generators.tshirt import tshirt_svg


def generate_all_svg():
    svg_dir_path = os.path.join(Path(__file__).parent.parent, "svg")
    os.makedirs(svg_dir_path, exist_ok=True)

    tshirt_svg(os.path.join(svg_dir_path, "tshirt.svg"))


if __name__ == "__main__":
    generate_all_svg()
