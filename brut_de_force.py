import time
import csv
from itertools import combinations

start_time = time.time()
"""
Objectif : trouver toutes les combinaisons d'actions pour un portefeuille de 500 Euro MAX
puis tester calculer et trier par ordre décroissant leur bénéfice, afin d'afficher
la meilleure combinaison
"""

wallet = 500
actions_data_file = 'actions_data.csv'

csv_shares_list = []
shares_list = []
combinations_list = []
ok_cost_combi_list = []
multi_cost_list = []
one_share_list = []
multi_shares_list = []
multi_names_list = []
multi_profit_list = []
share_dict = {}


multi_one_dict_list = []
combi_dict_list = []

# Creation de la liste des actions à partir du csv ; liste = [{}, {}, ...]
def create_formatted_shares_list(actions_data_file):

    with open (actions_data_file, 'r') as csv_file:
        for elt in csv.reader(csv_file, delimiter=';'):
            csv_shares_list.append(elt)
        del csv_shares_list[0]
        for csv_action in csv_shares_list:
            formatted_action = {'action_name':csv_action[0], 
                'action_cost':float(csv_action[1]),
                'action_profit':
                    (float(csv_action[1])*float(csv_action[2])/100)
            }
            shares_list.append(formatted_action)
    #del shares_list[14: 20]
    #print(shares_list)
    print("Nombre d'actions : "+ str(len(shares_list)))
    calculate_and_list_combinations(shares_list)

def add_list_shares_costs(combi):
    cost_list = []
    for each_share in combi:
        cost_list.append(each_share['action_cost'])
    return sum(cost_list)

def add_list_shares_profit(combi):
    profit_list = []
    for each_action in combi:
        profit_list.append(each_action['action_profit'])
    return sum(profit_list)

def calculate_and_list_combinations(shares_list):
    profits = 0
    for iter in range(1, (len(shares_list) + 1)):
        shares_combinations = combinations(shares_list, iter)
        for combi in shares_combinations:
            combi_costs_sum = add_list_shares_costs(combi)
            if combi_costs_sum <= wallet:
                combi_profits_sum = add_list_shares_profit(combi)
                if combi_profits_sum > profits:
                    profits = combi_profits_sum
                    best_combi = combi
    
    #print(best_combi)
    print('')
    print("Meilleure combinaison d'actions :")
    print("- Nom des actions : ")
    for share in best_combi:
        print((share['action_name']))
    best_combi_cost = add_list_shares_costs(best_combi)
    print("- Coût total des actions (€): "+str(best_combi_cost))
    print("- Bénéfices par action (€): "+str(profits))
    #
    
create_formatted_shares_list(actions_data_file)

# Temps d'exécution
duration = time.time() - start_time
print("durée d'exécution du programme : %s secondes" %(duration))
