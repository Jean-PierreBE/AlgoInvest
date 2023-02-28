from prettytable import PrettyTable
import ObjectActions as obj
COL_RESULTS = ['Combinaison', 'Prix total', 'Profit', 'temps total']
max_price = 500

'''Algorithme glouton'''


def getValeurMax(name, prices, profits, gains, capacite):
    tableauTrie = []
    bestRepartition = []
    result = []
    cost = 0
    for i in range(len(prices)):
        tableauTrie.append(obj.Actions(name[i], prices[i],
                                       profits[i], gains[i], i))

        # Trier les éléments du sac par leur rapport
    tableauTrie.sort(reverse=True)

    compteurValeur = 0
    for objet in tableauTrie:
        poidsCourant = objet.price
        valeurCourante = objet.gain
        #if poidsCourant > 0:
        if capacite - poidsCourant >= 0:
            # on ajoute l'objet dans le sac
            # On soustrait la capacité
            capacite -= poidsCourant
            compteurValeur += valeurCourante
            cost += poidsCourant
            # On ajoute la valeur dans le sac
            bestRepartition.append(objet.name)

    result.append(tuple(bestRepartition))
    result.append(round(cost, 2))
    result.append(round(compteurValeur, 2))
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
