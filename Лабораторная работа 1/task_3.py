list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
number_of_players=len(list_players) # количество игроков в списке
middle_index=number_of_players // 2 # индекс середины списка
team_1=list_players[:middle_index] # команда 1
team_2=list_players[middle_index:] # команда 2
print(team_1)
print(team_2)
# TODO Разделите участников на две команды
