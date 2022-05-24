import time
import csv

"""
Objectif : trouver toutes les combinaisons d'actions pour un portefeuille de 500 Euro MAX
puis selectionner et afficher la meilleure combinaison.
OPtimisation : utilisation de la  méthode du sac à dos par programmation dynamique
les valeurs du portefeuille, le prix et le bénéfice par action sont exprimés en centimes
"""
start_time = time.time()

wallet = 50000 # en centimes ( 500 euros x 100)
actions_data_file = 'actions_data.csv'
csv_shares_list = []
shares_list = []

def create_formatted_shares_list(actions_data_file):
    # Creation de la liste des actions à partir du fichier csv.
    with open (actions_data_file, 'r') as csv_file:
        for elt in csv.reader(csv_file, delimiter=';'):
            csv_shares_list.append(elt)
        del csv_shares_list[0]
        for csv_action in csv_shares_list:
            formatted_action = {'action_name':csv_action[0],
                'action_cost':round(float(csv_action[1])*100),
                'action_profit':
                    (float(csv_action[1])*round(float(csv_action[2])))
            }
            shares_list.append(formatted_action)
    print(shares_list)
    calculate_best_combination(wallet, shares_list)

def calculate_best_combination(wallet, shares_list):
    s_len = len(shares_list)
    # initialisation de la matrice "sac à dos" (share, wallet)
    matrice = [[0 for x in range(wallet + 1)] for x in range(s_len + 1)]

    for action in range(1, len(shares_list) + 1):
        for w in range(1, wallet + 1):
            if shares_list[action - 1]['action_cost'] <= wallet:
                matrice[action][w] = max(shares_list[action - 1]['action_profit'])
                + matrice[action - 1][w - shares_list[action - 1]['action_cost']],
                matrice[action - 1][w]
            else:
                matrice[action][w] = matrice[action - 1][w]

    # identification des meilleures actions
    best_shares = []

    while wallet >=0 and s_len >= 0:
        s = shares_list[s_len - 1]
        if matrice[s_len][w] == matrice[s_len - 1][w - s[1]] + s[2]:
            best_shares.append(s)
            w -= s[1]
        s_len -= 1
    print(best_shares)
    return matrice[-1][-1], best_shares

create_formatted_shares_list(actions_data_file)

# Temps d'exécution
duration = time.time() - start_time
print("durée d'exécution du programme : %s secondes" %(duration))