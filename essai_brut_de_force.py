import csv
from itertools import combinations
from pickletools import float8

"""
CdC : le programme doit lire un fichier contenant des info sur les actions
d'où le fichier actions_data.csv constitué au préalable avec les données du CdC
"""
# Creation de la liste des actions à partir du csv ; liste = [{}, {}, ...]

csv_shares_list = []
shares_list = []
with open ('actions_data.csv', 'r') as csv_file:
    for elt in csv.reader(csv_file, delimiter=';'):
        csv_shares_list.append(elt)
    del csv_shares_list[0]
    for csv_action in csv_shares_list:
        formatted_action ={'action_name':csv_action[0], 
                        'action_cost':float(csv_action[1]),
                        'action_profit':float(csv_action[2])}
        shares_list.append(formatted_action)

    #print(actions_list)
    #print(actions_list[14]['action_cost']) # EXPL : récupère le prix de Action-15

""" 
obj : trouver toutes les combinaisons d'actions pour un portefeuille de 500 Euro MAX
puis tester calculer et trier par ordre décroissant leur bénéfice, afin d'afficher 
la meilleure combinaison
"""

""" 1_combinaison de toutes actions entre elles:
"""
test_shares_list =[] # liste pour tests (petit nbr d'actions)

test_shares_list.append(shares_list[0])
test_shares_list.append(shares_list[1])
test_shares_list.append(shares_list[2])
#print(test_actions_list)


combinations_list = [] # liste de toutes les combinaisons
ok_cost_combi_list = [] # liste des combinaisons dont le coût total <100 (peuvent entrer ds portefeuille)
multi_cost_list = [] # liste des coûts des actions d'une combinaison


shares_qty = len(test_shares_list) # nbr d'actions ds la liste (3)
for iter in range(1, (shares_qty+1)):
    shares_combi = combinations(test_shares_list, iter) # = 'liste' de 7 combinaisons/tuples
    # pour chacune de ces combinaisons :     
    for combi in shares_combi:  # combi = tuple contenant 1 ou +sieurs actions différentes
        #print(combi)
        combinations_list.append(combi)
        
#print(combinations_list)
#print(len(combinations_list))

#print(combinations_list[6])
#print(combinations_list[6][0]) # 1er dico du 7e tuple de la liste

"""
SI tuple contient plusieurs dicos : faire somme des dico['action_cost'] 
Si tuple contient 1 seul dico :
pour chq dico de chq tuple, vérifier ['action_cost'] < 100

"""
for n in range(0, (len(combinations_list))):
    if len(combinations_list[n]) == 1:
        if (combinations_list[n][0]['action_cost']) < 100: 
            ok_cost_combi_list.append(combinations_list[n])
        else :
            pass
    elif len(combinations_list[n]) > 1:
        for m in range(0, (len(combinations_list[n]))):
            multi_cost_list.append(combinations_list[n][m]['action_cost'])
            print('sum(multi_cost_list) :')
            print(sum(multi_cost_list))
        if sum(multi_cost_list) < 100: 
            ok_cost_combi_list.append(combinations_list[n])
            multi_cost_list.clear()
        else:
            pass
print('****************')
print(len(ok_cost_combi_list))
print(ok_cost_combi_list) # liste des combinaisons dt coût < 100

print('****************')
profit_list = []
multi_profit_list = [multi_cost_list]

# calculer benef total de chq combi puis trier benef
for o in range(0,(len(ok_cost_combi_list))):
    if len(ok_cost_combi_list[o]) == 1:
        profit_list.append(ok_cost_combi_list[o])
        
    """ 
    calcul benefices d'une combi de +sieurs actions
    
    elif len(ok_cost_combi_list[o]) > 1:
        for p in range (0, len(ok_cost_combi_list[o])):
            print(ok_cost_combi_list[o][p])
            print(ok_cost_combi_list[o][p]['action_profit'])
            print(ok_cost_combi_list[o][p]['action_cost'])
            combi_action_profit = ok_cost_combi_list[o][p]['action_profit']
            combi_action_cost = ok_cost_combi_list[o][p]['action_cost']
            combi_total_profit = combi_action_profit * combi_action_cost
            print(combi_total_profit)
            
            multi_profit_list.append(combi_total_profit)
            print(multi_profit_list)
            
            print('sum(multi_profit_list) : ')
            print(sum(multi_profit_list)) 
            
        profit_list.append()
        """
        


