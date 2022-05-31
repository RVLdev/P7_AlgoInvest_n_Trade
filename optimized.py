import time
import csv

"""
Objectif : trouver la combinaison d'actions affichant le meilleur bénéfice,
pour un portefeuille de 500 Euro MAX,
sans parcourir toutes les combinaisons possibles,
et en moins d'une seconde. 
"""
start_time = time.time()

wallet = 500
actions_data_file = 'actions_data.csv'
csv_shares_list = []
basic_shares_list = []
shares_list = []
best_combi = []
best_shares_costs_list = []
best_shares_profits_list = []

def create_formatted_shares_list(actions_data_file):
    # Creation de la liste des actions à partir du fichier csv.
    with open (actions_data_file, 'r') as csv_file:
        for elt in csv.reader(csv_file, delimiter=';'):
            csv_shares_list.append(elt)
        del csv_shares_list[0]
        for csv_action in csv_shares_list:
            formatted_action = {'action_name':csv_action[0],
                'action_cost':float(csv_action[1]),
                'action_profit_rate' : float(csv_action[2])
            }
            basic_shares_list.append(formatted_action)
    sort_basic_shares_list_by_profit(basic_shares_list)

def sort_basic_shares_list_by_profit(basic_shares_list):
    shares_list = sorted(basic_shares_list, 
                        key=lambda k: k['action_profit_rate'],
                        reverse=True)
    print(shares_list)
    list_best_profit_shares(shares_list)

def list_best_profit_shares(shares_list):
    cost_list = []
    costs_sum = 0
    for share in shares_list:
        cost_list.append(share['action_cost'])
        costs_sum = sum(cost_list)
        if costs_sum <= wallet:
            best_combi.append(share)
    display_best_combination(best_combi)

def display_best_combination(best_combi):
    # Affiche le résultat
    print("Meilleure combinaison d'actions pour un portefeuille de 500 euros:")
    print("- Nom des actions : ")
    for share in best_combi:
        print((share['action_name']))
        best_shares_costs_list.append(share['action_cost'])
        profit_amount = share['action_cost']*share['action_profit_rate']/100
        best_shares_profits_list.append((profit_amount))    
    print("- Coût total des actions (€): "+str(sum(best_shares_costs_list)))
    print("- Bénéfices (€): "+str(round(sum(best_shares_profits_list), 2)))

create_formatted_shares_list(actions_data_file)

# Temps d'exécution
duration = time.time() - start_time
print("durée d'exécution du programme : %s secondes" %(duration))
