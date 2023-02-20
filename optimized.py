from prettytable import PrettyTable
import dask.dataframe as dd
import ObjectActions as obj

COL_RESULTS = ['Combinaison', 'Prix total', 'Profit']
max_price = 500

def getValeurMax(name, poids, profits, capacite):
    tableauTrie = []
    bestRepartition = []
    results = []
    cost = 0
    nombre_resultat = 0
    for i in range(len(poids)):
        tableauTrie.append(obj.ObjetAction(name[i], poids[i], profits[i], i))

        # Trier les éléments du sac par leur rapport
    tableauTrie.sort(reverse=True)

    compteurValeur = 0
    for objet in tableauTrie:
        poidsCourant = objet.poids
        valeurCourante = objet.profit
        if capacite - poidsCourant >= 0:
            # on ajoute l'objet dans le sac
            # On soustrait la capacité
            capacite -= poidsCourant
            compteurValeur += valeurCourante
            cost += poidsCourant
            # On ajoute la valeur dans le sac
            bestRepartition.append(objet.name)
        else:
            nombre_resultat += 1
            #capacite = int(capacite - (poidsCourant * fraction))
            capacite = max_price
            result = []
            result.append(tuple(bestRepartition))
            result.append(cost)
            result.append(compteurValeur)
            results.append(result)
            cost = 0
            bestRepartition = []
            compteurValeur = 0
            if nombre_resultat == 20:
                break
    return results

ddf_data = dd.read_csv("files_optimized/*2.csv")

df_data = ddf_data.compute()

df_data['Profit'] = df_data['price']*df_data['profit']/100
##print(df_data)
"""create array"""
name = df_data['name'].to_list()
poids = df_data['price'].to_list()
valeurs = df_data['Profit'].to_list()


OptimalRepartition = getValeurMax(name, poids, valeurs, max_price)

table_result = PrettyTable()
table_result.title = "10 Meilleures combinaisons"
table_result.field_names = COL_RESULTS
for i in range(len(OptimalRepartition)):
    table_result.add_row([OptimalRepartition[i][0],
                               OptimalRepartition[i][1],
                               OptimalRepartition[i][2]])

print(table_result)

