import time
import csv
from itertools import combinations

"""
Goal :
Find every possible combinations of shares for a 500 euros wallet. 
Then choose and display combination of maximum profit shares.
"""
start_time = time.time()

wallet = 500
actions_data_file = 'actions_data.csv'
csv_shares_list = []
shares_list = []

def create_formatted_shares_list(actions_data_file):
    # Create a usable formatted list of the shares form csv file.
    with open (actions_data_file, 'r') as csv_file:
        for elt in csv.reader(csv_file, delimiter=','):
            csv_shares_list.append(elt)
        del csv_shares_list[0]
        for csv_action in csv_shares_list:
            formatted_action = {'share_name':csv_action[0],
                'share_cost':float(csv_action[1]),
                'share_profit':
                    (float(csv_action[1])*float(csv_action[2])/100)
            }
            shares_list.append(formatted_action)
    calculate_and_list_combinations(shares_list)

def add_list_shares_costs(combi):
    # Make the sum of combination actions prices.
    cost_list = []
    for each_share in combi:
        cost_list.append(each_share['share_cost'])
    return sum(cost_list)

def add_list_shares_profit(combi):
    # Make the sum of combination actions profits.
    profit_list = []
    for each_action in combi:
        profit_list.append(each_action['share_profit'])
    return sum(profit_list)

def calculate_and_list_combinations(shares_list):
    """
    Create combinations of actions.
    Choose thoses matching criteria (wallet <= 500 €, maximum profit).
    """
    profits = 0
    for iter in range(1, (len(shares_list) + 1)):
        shares_combinations = combinations(shares_list, iter)
        for combi in shares_combinations:
            combi_costs_sum = add_list_shares_costs(combi)
            if combi_costs_sum <= wallet:
                combi_profits_sum = add_list_shares_profit(combi)
                if combi_profits_sum > profits:  # sorts by profit
                    profits = combi_profits_sum  # keeps highest profit
                    best_combi = combi  # highest profit combination = best combination
    display_best_combination(best_combi, profits)

def display_best_combination(best_combi, profits):
    print("Meilleure combinaison d'actions pour un portefeuille de 500 euros:")
    print("- Nom des actions : ")
    for share in best_combi:
        print((share['share_name']))
    best_combi_cost = add_list_shares_costs(best_combi)
    print("- Coût total des actions (€): "+str(best_combi_cost))
    print("- Bénéfices (€): "+str(round(profits, 2)))

create_formatted_shares_list(actions_data_file)

# Processing time.
duration = time.time() - start_time
print("durée d'exécution du programme : %s secondes" %(duration))
