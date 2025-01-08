from typing import Union
from pathlib import Path

def format_filename(filepath: Union[str, Path], ext: str) -> str:
    """
    Helper method: Generate suitable filename/extension

    :param str | Path filename:
            The filename the user entered, either as text or
            as a Path object

    :param str ext:
            The desired extension to be appended (e.g. ".jpg")

    :return str filename:
            The formatted filename
    """

def possible_controls(reverse_kv: bool=False): ...