import pandas as pd

def run():
    filename = "./resource/csv/woman-fashions.csv"

    WOMAN_FASHIONS = pd.read_csv(filename)

    corr_matrix = WOMAN_FASHIONS.loc[:,2].corr()
    print(corr_matrix)
    pass
