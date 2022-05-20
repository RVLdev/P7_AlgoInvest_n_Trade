import time
import csv
from itertools import combinations
from tqdm import tqdm

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
    del shares_list[12 : 19]
    print("Nombre d'actions : "+ str(len(shares_list)))
    calculate_and_list_combinations(shares_list)

def calculate_and_list_combinations(shares_list):
    for iter in range(1, (len(shares_list) + 1)):
        shares_combi = combinations(shares_list, iter)
        for combi in shares_combi:  # combi = 1 tuple of 1 or several shares
            combinations_list.append(combi)
    print('')
    print('NOMBRE DE COMBI POSSIBLES :')
    print(len(combinations_list))
    print('')
    separate_mono_n_multi_shares_combinations(combinations_list)

def separate_mono_n_multi_shares_combinations(combinations_list):
    for each_combi in range(0,(len(combinations_list))):
        # Selection des combinaisons mono-action
        if len(combinations_list[each_combi]) == 1:
            one_share_list.append(combinations_list[each_combi])
        # Selection des combinaisons multi-actions
        elif len(combinations_list[each_combi]) > 1:
            multi_shares_list.append(combinations_list[each_combi])
    list_ok_cost_mono_share_combi(one_share_list)

def list_ok_cost_mono_share_combi(one_share_list):
    for mono_share in one_share_list:
        if mono_share[0]['action_cost'] <= wallet:
            ok_cost_combi_list.append(mono_share[0])
        else:
            pass
    list_ok_cost_multi_shares_combi(multi_shares_list, wallet)

def format_combi(multi_names_list, multi_cost_sum, multi_profit_sum):
    share_dict = {
        'action_name': multi_names_list,
        'action_cost': multi_cost_sum,
        'action_profit': multi_profit_sum
        }
    return share_dict

def list_ok_cost_multi_shares_combi(multi_shares_list, wallet):
    for multi_share in tqdm((multi_shares_list), desc="COST MULTI_COMBI"):
        multi_names_list = []
        for each_dict in multi_share:
            multi_names_list.append(each_dict['action_name'])
            multi_profit_list.append(each_dict['action_profit'])
            multi_profit_sum = sum(multi_profit_list)
            multi_cost_list.append(each_dict['action_cost'])
            multi_cost_sum = sum(multi_cost_list)
        if sum(multi_cost_list) <= wallet:
            share_dict = format_combi(multi_names_list,
                                    multi_cost_sum,
                                    multi_profit_sum)
            ok_cost_combi_list.append(share_dict)
            multi_profit_list.clear()
            multi_cost_list.clear()
            multi_names_list = []
        else:
            pass
    sort_combi_list_by_profit(ok_cost_combi_list)

def sort_combi_list_by_profit(ok_cost_combi_list):
    best_combi_list = sorted(ok_cost_combi_list,
                                key=lambda k: k['action_profit'],
                                reverse=True)
    display_best_combination(best_combi_list)

def display_best_combination(best_combi_list):
    print('')
    print("La meilleure combinaison d'actions est :")
    print("- Nom des actions : "+str(best_combi_list[0]['action_name']))
    print("- Coût total des actions : "+str(best_combi_list[0]['action_cost']))
    print("- Bénéfices par action (€): "+str(best_combi_list[0]['action_profit']))
    print('')
    calculate_stock_portfolio_profit(best_combi_list)

def calculate_stock_portfolio_profit(best_combi_list):
    qty_of_shares = int(len(best_combi_list[0]['action_name']))
    print("Nombre d'actions : " + str(qty_of_shares))
    combi_profit_amount = best_combi_list[0]['action_profit']
    print("Montant total des bénéfices d'un portefeuille de 500 euros:")
    print(str((qty_of_shares*combi_profit_amount))+' €')
    print('')

create_formatted_shares_list(actions_data_file)

# Temps d'exécution
duration = time.time() - start_time
print("durée d'exécution du programme : %s secondes" %(duration))
