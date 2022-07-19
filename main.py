from multiprocessing import Process
import src.functions as func
import src.api as url
import sys


def main():
    try:
        # write Man Fashion Category Data
        func.get_data_and_write(url.man_fashions)
        # # write Woman Fashion Category Data
        func.get_data_and_write(url.woman_fashions)
        # # write Electronic Category Data
        func.get_data_and_write(url.electronics)
        # Try to Filter the Price for the Man Fashions
        func.create_graph(url.man_fashions, 4000, 5000)
        # Try to Filter the Price for the Woman Fashions
        func.create_graph(url.woman_fashions, 4000, 5000)
        func.elbow_range(url.woman_fashions)
    except:
        print(f'Error on {sys.exc_info()}')
    else:
        print('Done')

    pass


if __name__ == '__main__':
    sys.exit(main())
