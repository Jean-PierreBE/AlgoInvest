import pandas as pd
from tools import print_result, max_price, getValeurMax

DATA_FILES = {"File_01": "files_optimized/ActionData1.csv",
              "File_02": "files_optimized/ActionData2.csv"}
DATA_DELIMETER = ","
TITLE_RESULTS = "Meilleure combinaison solution optimisée fichier {}"

for key, value in DATA_FILES.items():
    """read file"""
    df_data = pd.read_csv(value, delimiter=DATA_DELIMETER,
                          encoding='unicode_escape')

    df_data['gain'] = df_data['price']*df_data['profit']/100
    """create array"""
    names = df_data['name'].to_list()
    prices = df_data['price'].to_list()
    profits = df_data['profit'].to_list()
    gains = df_data['gain'].to_list()

    OptimalRepartition = getValeurMax(names, prices, profits,
                                      gains,  max_price)

    print_result(OptimalRepartition, TITLE_RESULTS.format(key))
