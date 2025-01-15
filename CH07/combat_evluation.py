def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if (player_power > enemy_defense):
        advantage = True
    elif (player_power == enemy_defense):
        evenly_matched = True
    else:
        disadvantage = True

    return advantage, disadvantage, evenly_matched
