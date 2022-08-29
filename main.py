import src.functions as func
import testing.kmeans as km
import testing.knn as knn
import src.api as url
import sys


def main():
    try:
        # func.get_data_and_write(url.woman_fashions)
        # km.create_data()
        km.dummy_data()
        # km.create_data()
        # knn.run()
    except:
        print(f'Error on {sys.exc_info()}')
    else:
        print('Done')

    pass

if __name__ == '__main__':
    sys.exit(main())
