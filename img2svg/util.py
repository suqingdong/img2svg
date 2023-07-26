import base64
from typing import Generator, List


def parse_conf(file: str, sep: str = '\t') -> Generator[List[str], None, None]:
    """
    Parse the configuration file.

    :param file: Path to the configuration file.
    :param sep: Separator to split the lines in the file, default is '\t'.
    :yield: List of strings after splitting each line in the file.
    """
    with open(file) as f:
        for line in f:
            if line.strip():
                linelist = line.strip().split(sep)
                yield linelist


def img_to_b64(image: str) -> str:
    """
    Convert the image to base64 string.

    :param image: Path to the image file.
    :return: Base64 encoded string of the image.
    """
    return base64.b64encode(open(image, 'rb').read()).decode()
