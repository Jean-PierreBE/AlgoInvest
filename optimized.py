from prettytable import PrettyTable
import pandas as pd
import dask.dataframe as dd


def knapsack(v, w, W):
    # `T[i][j]` stocke la valeur maximale du sac à dos ayant un poids inférieur
    # supérieur à `j` avec seulement les premiers éléments `i` considérés.
    T = [[0 for x in range(W + 1)] for y in range(len(v) + 1)]

    # faire pour le ième article
    for i in range(1, len(v) + 1):

        # considère tous les poids de 0 à la capacité maximale `W`
        for j in range(W + 1):

            # ne pas inclure le ième élément si `j-w[i-1]` est négatif
            if w[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                print("i : " + str(i))
                print("j : " + str(j))
                print("T[i - 1][j] : " + str(T[i - 1][j]))
                print("j - w[i - 1] : " + str(j - w[i - 1]))
                print("v[i - 1] : " + str(v[i - 1]))
                # trouver la valeur maximale que nous obtenons en excluant ou en incluant le ième élément
                T[i][j] = max(T[i - 1][j], T[i - 1][int(j - w[i - 1])] + v[i - 1])

    # renvoie la valeur maximale
    return T[len(v)][W]

#ddf = dd.read_csv("bruteforce/*.csv")
ddf_data = dd.read_csv("*.csv")

df_data = ddf_data.compute()

##print(df_data)

"""create array"""
array_weight = df_data['price'].to_list()
#print(len(array_weight))
array_value = df_data['profit'].to_list()
#print(len(array_value))

print('Knapsack value is', knapsack(array_value, array_weight, 500))