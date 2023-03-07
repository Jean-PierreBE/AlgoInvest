from prettytable import PrettyTable
import ObjectActions as obj
COL_RESULTS = ['Combinaison', 'Prix total', 'Profit', 'temps total']
max_price = 500

'''Algorithme glouton'''


def getValeurMax(name, prices, profits, gains, capacite):
    tableauTrie = []
    bestRepartition = []
    result = []
    coutTotal = 0
    gainTotal = 0
    prixUnitaire = 0
    gainUnitaire = 0

    for i in range(len(prices)):
        tableauTrie.append(obj.Actions(name[i], prices[i], profits[i], gains[i], i))
    # Trier les éléments du sac par profits
    tableauTrie.sort(reverse=True)

    for objet in tableauTrie:
        prixUnitaire = objet.price
        gainUnitaire = objet.gain
        if capacite - prixUnitaire >= 0:
            # on ajoute l'objet dans le sac
            # On soustrait la capacité
            capacite -= prixUnitaire
            gainTotal += gainUnitaire
            coutTotal += prixUnitaire
            # On ajoute la valeur dans le sac
            bestRepartition.append(objet.name)

    result.append(tuple(bestRepartition))
    result.append(round(coutTotal, 2))
    result.append(round(gainTotal, 2))
    return result


"""Affichage des résultats"""


def print_result(data_input, title, temps):
    table_result = PrettyTable()
    table_result.title = title
    table_result.field_names = COL_RESULTS
    table_result.add_row([data_input[0],
                          data_input[1],
                          data_input[2],
                          round(temps, 4)])

    print(table_result)
