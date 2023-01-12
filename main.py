from pathlib import Path
from pydantic import ValidationError

from parser.models import BaseInputPars

FILE = Path('parser/static/data.json')


def read():
    try:
        res1 = BaseInputPars.parse_file(FILE)
    except ValidationError as error:
        raise error.json()
    else:
        return res1.dict(by_alias=True)


if __name__ == '__main__':
    read()
