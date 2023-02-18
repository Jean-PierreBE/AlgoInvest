from itertools import combinations
from prettytable import PrettyTable
import pandas as pd

"""constants"""
data_file = "files_bruteforce/ActionData.csv"
data_delimeter = ";"
max_price = 500
COL_RESULTS = ['Combinaison', 'Prix total', 'Profit']

"""variables"""
combinaison_opt = []
data_dict = {}

"""read file"""
df_data = pd.read_csv(data_file, delimiter= data_delimeter, encoding= 'unicode_escape')
"""add colum """
df_data["Profit"] = df_data["Coût par action (en euros)"]*df_data["Bénéfice (après 2 ans)"]/100
"""create dictionnary"""
for row in df_data.itertuples():
    tab = []
    tab.append(row[2])
    tab.append(row[4])
    data_dict[row[1]] = tab
"""array """
array_actions = df_data['Actions #'].to_list()

comb = []
for n in range(1,len(array_actions)+1):
    comb.append([i for i in combinations(array_actions,n)])

"""calcul for each combinaison"""
for ind in range(0,len(comb)):
    for jnd in range(0,len(comb[ind])):
        tab_detail = []
        total_price = 0
        total_profit = 0
        for knd in range(0,len(comb[ind][jnd])):
            total_price = total_price + data_dict[comb[ind][jnd][knd]][0]
            total_profit = total_profit + data_dict[comb[ind][jnd][knd]][1]
        if total_price <= max_price:
            tab_detail.append(comb[ind][jnd])
            tab_detail.append(round(total_price,2))
            tab_detail.append(round(total_profit,2))
            combinaison_opt.append(tab_detail)

combinaison_opt_sort = sorted(combinaison_opt, key=lambda x: x[2], reverse=True)

table_result = PrettyTable()
table_result.title = "10 Meilleures combinaisons"
table_result.field_names = COL_RESULTS
for i in range(0,9):
    table_result.add_row([combinaison_opt_sort[i][0],
                               combinaison_opt_sort[i][1],
                               combinaison_opt_sort[i][2]])

print(table_result)
