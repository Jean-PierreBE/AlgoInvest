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
    noms_action = df_data['name'].to_list()
    prix = df_data['price'].to_list()
    taux_profits = df_data['profit'].to_list()
    montant_profits = df_data['gain'].to_list()

    OptimalRepartition = getValeurMax(noms_action, prix, taux_profits,
                                      montant_profits,  max_price)

    print_result(OptimalRepartition, TITLE_RESULTS.format(key))
