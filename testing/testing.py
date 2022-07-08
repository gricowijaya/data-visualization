from multiprocessing import Process
import src.functions as func
import src.api as url
import sys


def testing():
    # write Man Fashion Category Data
    func.get_data_and_write(url.manFashions)
    # write Woman Fashion Category Data
    func.get_data_and_write(url.womanFashions)
    # Try to Filter the Price for the Man Fashions
    func.filter_data_by_price(url.manFashions, 4000, 5000)
    # Try to Filter the Price for the Woman Fashions
    func.filter_data_by_price(url.womanFashions, 4000, 5000)
    pass


if __name__ == '__testing__':
    sys.exit(testing())
