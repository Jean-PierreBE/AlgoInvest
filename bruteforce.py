from itertools import combinations
import pandas as pd
import time
from tools import print_result, max_price

"""constants"""
DATA_FILE = "files_bruteforce/ActionData.csv"
DATA_DELIMETER = ","
TITLE_RESULTS = "Meilleure combinaison solution brute"

"""variables"""
combinaison_opt = []
data_dict = {}

"""begin time"""
tps1 = time.time()
"""read file"""
df_data = pd.read_csv(DATA_FILE, delimiter=DATA_DELIMETER,
                      encoding='unicode_escape')
"""add colum """
df_data["Profit"] = df_data["price"]*df_data["profit"]/100
"""create dictionnary"""
for row in df_data.itertuples():
    tab = []
    tab.append(row[2])
    tab.append(row[4])
    data_dict[row[1]] = tab
"""array """
array_actions = df_data['name'].to_list()

comb = []
nb_comb = 0
for n in range(1, len(array_actions)+1):
    comb.append([i for i in combinations(array_actions, n)])

"""calcul for each combinaison"""
for ind in range(0, len(comb)):
    nb_comb = nb_comb + len(comb[ind])
    for jnd in range(0, len(comb[ind])):
        tab_detail = []
        total_price = 0
        total_profit = 0
        for knd in range(0, len(comb[ind][jnd])):
            total_price = total_price + data_dict[comb[ind][jnd][knd]][0]
            total_profit = total_profit + data_dict[comb[ind][jnd][knd]][1]
        if total_price <= max_price:
            tab_detail.append(tuple(comb[ind][jnd]))
            tab_detail.append(round(total_price, 2))
            tab_detail.append(round(total_profit, 2))
            combinaison_opt.append(tab_detail)

print("nb_comb : " + str(nb_comb))
print("len(combinaison_opt) : " + str(len(combinaison_opt)))

combinaison_opt_sort = sorted(combinaison_opt,
                              key=lambda x: x[2], reverse=True)
tps2 = time.time()
tpstot = tps2 - tps1
print_result(combinaison_opt_sort[0], TITLE_RESULTS, tpstot)
