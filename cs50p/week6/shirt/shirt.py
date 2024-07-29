
import argparse
from pathlib import Path, PurePath
from typing import NoReturn

from PIL import Image, ImageOps

OUT_HEADERS = ("first", "last", "house")
EXTENSIONS = (".jpg", ".jpeg", ".png")
CURRENT_PATH = Path(__file__).parent.resolve()
SHIRT = "shirt.png"


def convert(in_file_name: str, out_file_name: str) -> None:
    with Image.open(in_file_name, "r", ("JPEG", "PNG")) as in_file, Image.open(
        PurePath(CURRENT_PATH, SHIRT), "r", ("JPEG", "PNG")
    ) as shirt:
        in_file = ImageOps.fit(in_file, shirt.size)
        in_file.paste(shirt, (0, 0), shirt)
        in_file.save(out_file_name)


def validate(in_file_name: str, out_file_name: str) -> NoReturn:
    in_file = Path(in_file_name)
    out_file = Path(out_file_name)
    if not in_file.is_file():
        raise FileNotFoundError(in_file_name)

    if in_file.suffix.lower() not in EXTENSIONS:
        raise ValueError("Invalid input")

    if in_file.suffix.lower() != out_file.suffix.lower():
        raise ValueError("Input and output have different extensions")

    if in_file.stat().st_size <= 0:
        raise ValueError(f"{in_file_name} is empty")


def main() -> None:
    # initialise an argparser object with one positional argument to receive
    # a file name from user
    parser = argparse.ArgumentParser(prog="python shirt.py",
                                     description="Count lines in a file")
    parser.add_argument("in_file")
    parser.add_argument("out_file")

    args = parser.parse_args()
    validate(args.in_file, args.out_file)
    convert(args.in_file, args.out_file)


if __name__ == "__main__":
    main()
