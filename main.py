from pathlib import Path
from pprint import pprint

from pydantic import ValidationError
from parser.models import BasePars


FILE = Path('parser/static/data.json')


def main():
    try:
        res = BasePars.parse_file(FILE)
    except ValidationError as error:
        raise error.json()
    else:
        pprint(res.dict(by_alias=True))


if __name__ == '__main__':
    main()
