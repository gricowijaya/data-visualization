from multiprocessing import Process
import src.functions as func
import src.api as url
import sys


# def main():
#     # func.write_woman_fashions_data(url.womanFashions)
#     # func.write_man_fashions_data(url.manFashions)
#     func.read_woman_fashions_data()
#     func.read_man_fashions_data()
#     pass


if __name__ == '__main__':
    process1 = Process(target=func.read_man_fashions_data())
    process1.start()
    process2 = Process(target=func.read_woman_fashions_data())
    process2.start()
    # sys.exit(main())
