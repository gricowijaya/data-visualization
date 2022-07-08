from multiprocessing import Process
import src.functions as func
import src.api as url
import sys


def main():
    # func.write_woman_fashions_data(url.womanFashions)
    # func.write_man_fashions_data(url.manFashions)
    func.read_woman_fashions_data()
    func.read_man_fashions_data()
    # func.create_table()
    pass


if __name__ == '__main__':
    sys.exit(main())
