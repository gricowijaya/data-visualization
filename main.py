import src.functions as func
import src.api as url
import sys


def main():
    func.write_woman_fashions_data(url.womanFashions)
    pass


if __name__ == '__main__':
    sys.exit(main())
