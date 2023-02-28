import pandas as pd
import time
from tools import print_result, max_price, getValeurMax

DATA_FILES = {"File_Test": "files_bruteforce/ActionData.csv",
              "File_01": "files_optimized/ActionData1.csv",
              "File_02": "files_optimized/ActionData2.csv"}
DATA_DELIMETER = ","
TITLE_RESULTS = "Meilleure combinaison solution optimisée fichier {}"

for key, value in DATA_FILES.items():
    """begin time"""
    tps1 = time.time()
    """read file"""
    df_data = pd.read_csv(value, delimiter=DATA_DELIMETER,
                          encoding='unicode_escape')

    """select records if only price > 0"""
    df_data_ok = df_data.loc[df_data['price'] > 0]
    """compute column gain"""
    df_data_ok['gain'] = df_data_ok['price']*df_data_ok['profit']/100
    """create array"""
    noms_action = df_data_ok['name'].to_list()
    prix = df_data_ok['price'].to_list()
    taux_profits = df_data_ok['profit'].to_list()
    montant_profits = df_data_ok['gain'].to_list()

    OptimalRepartition = getValeurMax(noms_action, prix, taux_profits,
                                      montant_profits,  max_price)
    """finish time"""
    tps2 = time.time()
    tpstot = tps2 - tps1
    print_result(OptimalRepartition, TITLE_RESULTS.format(key), tpstot)
